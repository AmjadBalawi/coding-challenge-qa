import logging
from typing import Awaitable, Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from codingchallenge_qa_service._version import __version__
from codingchallenge_qa_service.logging import getLogger
from codingchallenge_qa_service.measure import Measure
from codingchallenge_qa_service.transaction import Transaction
logger = getLogger(name=__name__)


class TransactionMiddleware(BaseHTTPMiddleware):
    """
    Middleware class for handling transactions in the FastAPI application.

    This middleware is responsible for recording transaction information, such as the duration of requests,
    creating and updating transactions, and logging transaction-related information.

    Args:
        app: The FastAPI application.

    Attributes:
        app: The FastAPI application.

    """

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        """
        Dispatch method called for each incoming request.

        This method handles the transaction related tasks for each request.
        It records the start time of the request, calls the next middleware or endpoint handler,
        calculates the request duration, records the transaction information, and stores or updates the transaction.

        Args:
            request: The incoming request.
            call_next: The callable for calling the next middleware or endpoint handler.

        Returns:
            The response from the next middleware or endpoint handler.

        Raises:
            Exception: If an exception occurs during request handling.

        """
        transaction = Transaction()
        request.state.transaction = transaction
        request.state.transaction.time_request = Measure.start_clock()  # Set the time_request attribute

        try:
            response = await call_next(request)
        except Exception as e:
            transaction.record_exception(e)
            raise
        else:
            duration = Measure.stop_clock(transaction.time_request)

            with transaction.record({
                "request_time": Measure.current_time(),
                "duration_request_total": duration,
                "transaction_id": transaction.transaction_id,
                "codingchallenge_qa_service_release_version": __version__,
            }):
                transaction_service = request.app.state.services.transaction_service
                if transaction.should_store:
                    try:
                        transaction_service.create(transaction)
                        logger_level = logger.level
                        if logger_level <= logging.INFO:
                            logger.info("[Transaction_Middleware] Transaction created")
                    except Exception as e:
                        logger.error("[Transaction_Middleware] exception thrown in create transaction", exc_info=e)

                if transaction.should_update:
                    try:
                        transaction_service.update(transaction)
                        logger_level = logger.level
                        if logger_level <= logging.DEBUG:
                            logger.debug("[Transaction_Middleware] Transaction updated")
                    except Exception as e:
                        logger.error("[Transaction_Middleware] exception thrown in update transaction", exc_info=e)

        return response

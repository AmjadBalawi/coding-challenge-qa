from unittest.mock import MagicMock
from fastapi import Request, Response
from app.codingchallenge_qa_service.middlewares.transaction_middleware import *
import asyncio


def test_dispatch():
    # Create a mock FastAPI application and the middleware instance
    app = MagicMock()
    middleware = TransactionMiddleware(app)

    # Create a mock scope with the required attributes
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "headers": [],
        "scheme": "http",
        "path": "/",
        "query_string": b"",
        "root_path": "",
        "client": None,
        "server": None,
        "app": app,  # Set the 'app' attribute in the scope
    }

    # Create a mock request object with the scope
    request = Request(scope)

    # Create a mock response object
    response = Response("OK")

    # Set the transaction attribute in request.state
    setattr(request.state, "transaction", None)

    # Patch the transaction_service
    transaction_service = MagicMock()
    app.state.services.transaction_service = transaction_service

    # Define a mock coroutine function for call_next
    async def call_next(req):
        return response

    # Call the dispatch method of the middleware using asyncio.run
    result = asyncio.run(middleware.dispatch(request, call_next))

    # Assertions
    assert result == response
    assert hasattr(request.state, "transaction")
    assert transaction_service.create.called or not transaction_service.update.called


def test_dispatch_exception():
    # Create a mock FastAPI application and the middleware instance
    app = MagicMock()
    middleware = TransactionMiddleware(app)

    # Create a mock scope with the required attributes
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "headers": [],
        "scheme": "http",
        "path": "/",
        "query_string": b"",
        "root_path": "",
        "client": None,
        "server": None,
        "app": app,  # Set the 'app' attribute in the scope
    }

    # Create a mock request object with the scope
    request = Request(scope)

    # Create a mock response object
    response = Response("OK")

    # Set the transaction attribute in request.state
    setattr(request.state, "transaction", None)

    # Patch the transaction_service
    transaction_service = MagicMock()
    app.state.services.transaction_service = transaction_service

    # Define a mock exception
    exception = Exception("Test exception")

    # Define a mock coroutine function for call_next that raises an exception
    async def call_next(req):
        raise exception

    # Call the dispatch method of the middleware using asyncio.run and handle the raised exception
    try:
        asyncio.run(middleware.dispatch(request, call_next))
    except Exception as e:
        assert e is exception

    # Assertions
    assert hasattr(request.state, "transaction")
    assert transaction_service.create.called or not transaction_service.update.called
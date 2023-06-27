from codingchallenge_qa_service.logging import getLogger
from codingchallenge_qa_service.transaction import Transaction
logger = getLogger(__name__)


class TransactionService:
    """
    Handles the storage and updating of transactions

    Methods
    -------
    create(transaction: Transaction)
        Stores a transaction
    update(transaction: Transaction)
        Updates a transaction
    """

    def log_transaction(self, transaction: Transaction, action: str):
        logger.debug(f"{action.upper()} transaction: '{transaction.transaction_id}'", extra={
            "transaction_data": transaction.to_dict(include_id=False)
        })

    def create(self, transaction: Transaction):
        self.log_transaction(transaction, "create")

    def update(self, transaction: Transaction):
        self.log_transaction(transaction, "update")

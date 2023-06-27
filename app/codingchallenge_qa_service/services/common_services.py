from codingchallenge_qa_service.services.infer_service import InferService
from codingchallenge_qa_service.services.paraphrase_service import ParaphraseService
from codingchallenge_qa_service.services.prefiltering_service import PrefilteringService
from codingchallenge_qa_service.services.sensitive_content_detection_service import SensitiveContentDetectionService
from codingchallenge_qa_service.services.transaction_service import TransactionService


class CommonServices:
    """
    Singleton class that provides access to common services used in the application.
    """

    _instance = None

    def __new__(cls):
        """
        Creates a single instance of CommonServices or returns the existing instance if it already exists.

        Returns:
            CommonServices: The CommonServices instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.transaction_service = TransactionService()
            cls._instance.sensitive_content_detection_service = SensitiveContentDetectionService()
            cls._instance.prefiltering_service = PrefilteringService()
            cls._instance.infer_service = InferService()
            cls._instance.paraphrase_service = ParaphraseService()
        return cls._instance

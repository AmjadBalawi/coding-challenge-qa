from pydantic import BaseModel
from uuid import UUID


class InferResponse(BaseModel):
    """
    Model representing the response from the inference process.

    This model defines the structure of the response returned after performing inference.
    It includes the answer, question, answer validity, flag indicating if it's a ground truth answer,
    question UUID, and transaction UUID.

    Attributes:
        answer (str): The answer generated from the inference.
        question (str): The original question.
        answer_validity (str): The validity of the answer.
        is_gs_answer (bool): Flag indicating if the answer is a ground truth answer.
        question_uuid (UUID): The UUID of the question.
        transaction_id (UUID): The UUID of the transaction.

    """

    answer: str
    question: str
    answer_validity: str
    is_gs_answer: bool
    question_uuid: UUID
    transaction_id: UUID

from typing import Any, Dict
from uuid import UUID
from pydantic import BaseModel


class ParaphraseServiceRequest(BaseModel):
    """
    Model representing the request sent to the paraphrase service.

    This model defines the structure of the request sent to the paraphrase service.
    It includes the question content string and the course ID.

    Attributes:
        question_content_str (str): The content of the question to be paraphrased.
        course_id (str): The ID of the course associated with the question.

    """

    question_content_str: str
    course_id: str


class ParaphraseServiceResponse(BaseModel):
    """
    Model representing the response from the paraphrase service.

    This model defines the structure of the response returned by the paraphrase service.
    It includes the UUID of the original question, the content of the original question,
    the course ID, the UUID of the ground truth answer, the content of the ground truth answer,
    and additional meta data.

    Attributes:
        question_origin_uuid (UUID): The UUID of the original question.
        question_origin_content_str (str): The content of the original question.
        course_id (str): The ID of the course associated with the question.
        gs_answer_uuid (UUID): The UUID of the ground truth answer.
        gs_answer_content_str (str): The content of the ground truth answer.
        meta_data (Dict[str, Any]): Additional meta data associated with the paraphrase service response.

    """

    question_origin_uuid: UUID
    question_origin_content_str: str
    course_id: str
    gs_answer_uuid: UUID
    gs_answer_content_str: str
    meta_data: Dict[str, Any]

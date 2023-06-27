from pydantic import BaseModel, validator
from codingchallenge_qa_service.models.qa_models import Client, Language, User
from fastapi import HTTPException


class InferRequest(BaseModel):
    """
    Model representing the request for performing inference.

    This model defines the structure and validation for the request parameters needed to perform inference.
    It includes the query text, user information, course ID, client information, language, and annotation allowance.

    Attributes:
        query (str): The query text.
        user (User): The user information.
        course_id (str): The course ID.
        client (Client): The client information.
        language (Language): The language.
        allow_annotation (bool): Flag indicating whether annotation is allowed.

    """

    query: str
    user: User
    course_id: str
    client: Client
    language: Language
    allow_annotation: bool

    @validator("query")
    def query_cannot_be_empty(cls, v):
        """
        Validator to ensure the query parameter is not empty.

        Args:
            v: The value of the query parameter.

        Raises:
            HTTPException: If the query parameter is empty.

        Returns:
            The value of the query parameter.

        """
        if v == "":
            raise HTTPException(status_code=422, detail="Query parameter cannot be empty.")
        return v

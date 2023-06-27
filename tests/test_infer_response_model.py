import pytest
from pydantic import ValidationError
from uuid import UUID
from app.codingchallenge_qa_service.models.infer_response import *


def test_infer_response_model():
    # Valid test data
    answer = "Test answer"
    question = "Test question"
    answer_validity = "valid"
    is_gs_answer = False
    question_uuid = UUID("12345678-1234-1234-1234-123456789abc")
    transaction_id = UUID("abcdef12-3456-7890-abcd-ef1234567890")

    # Try to create a valid instance of the InferResponse model
    try:
        infer_response = InferResponse(
            answer=answer,
            question=question,
            answer_validity=answer_validity,
            is_gs_answer=is_gs_answer,
            question_uuid=question_uuid,
            transaction_id=transaction_id,
        )
        # Assert that the instance was created without raising an exception
        assert isinstance(infer_response, InferResponse)
    except ValidationError as e:
        # Handle any validation exception that may occur
        pytest.fail(f"An unexpected validation error occurred: {repr(e)}")

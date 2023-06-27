import pytest
from pydantic import ValidationError
from uuid import UUID
from app.codingchallenge_qa_service.models.paraphrase_models import *


def test_paraphrase_service_response_model():
    # Valid test data
    data = {
        "question_origin_uuid": UUID("123e4567-e89b-12d3-a456-426614174000"),
        "question_origin_content_str": "Original question",
        "course_id": "course123",
        "gs_answer_uuid": UUID("123e4567-e89b-12d3-a456-426614174001"),
        "gs_answer_content_str": "Ground truth answer",
        "meta_data": {"key": "value"}
    }

    response = ParaphraseServiceResponse(**data)

    # Assert individual attributes
    assert response.question_origin_uuid == UUID("123e4567-e89b-12d3-a456-426614174000")
    assert response.question_origin_content_str == "Original question"
    assert response.course_id == "course123"
    assert response.gs_answer_uuid == UUID("123e4567-e89b-12d3-a456-426614174001")
    assert response.gs_answer_content_str == "Ground truth answer"
    assert response.meta_data == {"key": "value"}

    # Assert the serialized representation of the response
    assert response.dict() == data

    # Assert invalid UUID format for question_origin_uuid
    invalid_data = data.copy()
    invalid_data["question_origin_uuid"] = "invalid-uuid"
    with pytest.raises(ValidationError):
        ParaphraseServiceResponse(**invalid_data)

    # Assert missing required attribute gs_answer_content_str
    invalid_data = data.copy()
    del invalid_data["gs_answer_content_str"]
    with pytest.raises(ValidationError):
        ParaphraseServiceResponse(**invalid_data)

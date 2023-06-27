import sys

for path in sys.path:
    print(path)
from app.codingchallenge_qa_service.models.infer_request import *
import pytest
from fastapi import HTTPException
from pydantic import ValidationError


def test_infer_request_model():
    # Valid test data
    query = "Test query"
    user = User(id="user123", type="student")
    course_id = "course123"
    client = Client(name="client_name", version="1.0", code="ms_teams", details={"key": "value"})
    language = Language(Language.EN)
    allow_annotation = True

    # Try to create a valid instance of the InferRequest model
    try:
        infer_request = InferRequest(
            query=query,
            user=user,
            course_id=course_id,
            client=client,
            language=language,
            allow_annotation=allow_annotation,
        )
        # Assert that the instance was created without raising an exception
        assert isinstance(infer_request, InferRequest)
    except (ValidationError, HTTPException) as e:
        # Handle any validation or HTTP exception that may occur
        pytest.fail(f"An unexpected exception occurred: {repr(e)}")
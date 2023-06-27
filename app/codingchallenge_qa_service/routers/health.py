from fastapi import APIRouter
router = APIRouter()


@router.get("/")
@router.get("/health")
def health():
    """
    Health endpoint.

    This endpoint returns the status of the application, indicating that it is running.

    Returns:
        dict: A dictionary containing the status of the application.
            Example: {"status": "running"}

    """
    return {"status": "running"}

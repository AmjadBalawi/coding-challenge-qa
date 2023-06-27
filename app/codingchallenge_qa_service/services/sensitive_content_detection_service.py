from typing import Any, Dict
from random import randint
from codingchallenge_qa_service.logging import getLogger
logger = getLogger(name=__name__)


class SensitiveContentDetectionService:
    """Service for checking queries for sensitive content."""

    @staticmethod
    async def run(query: str, user_id: str) -> Dict[str, Any]:
        sensitivity = "UNSAFE" if randint(0, 1) == 0 else "SAFE"
        model_name = "SCD_MODEL"
        if sensitivity == "UNSAFE":
            logger.warning("Sensitive content detected")

        return {"sensitivity": sensitivity, "model_name": model_name}

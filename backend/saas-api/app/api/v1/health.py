"""
Platform health endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.db.health import check_database_connection
from app.shared.responses import ApiResponse

router = APIRouter()


@router.get(
    "/health",
    summary="Application Health",
)
async def health() -> ApiResponse[dict]:
    """
    Platform health endpoint.

    Returns application status together with database connectivity.
    """

    try:
        database_status = "healthy" if check_database_connection() else "unhealthy"

    except SQLAlchemyError:
        database_status = "unhealthy"

    return {
        "success": True,
        "message": "Platform healthy",
        "data": {
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "database": database_status,
            "status": ("healthy" if database_status == "healthy" else "degraded"),
        },
    }  # type: ignore

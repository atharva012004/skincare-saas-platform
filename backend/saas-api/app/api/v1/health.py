"""
Platform health endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import settings
from app.db.health import check_database_connection
from app.shared.response_factory import ResponseFactory
from app.shared.responses import ApiResponse

router = APIRouter()


@router.get(
    "/health",
    summary="Application Health",
    response_model=ApiResponse[dict],
)
async def health() -> ApiResponse[dict]:
    """
    Platform health endpoint.

    Returns application status together with database connectivity.
    """

    database_healthy = await check_database_connection()
    database_status = "healthy" if database_healthy else "unhealthy"
    platform_status = "healthy" if database_healthy else "degraded"

    return ResponseFactory.success(
        message=f"Platform {platform_status}",
        data={
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "database": database_status,
            "status": platform_status,
        },
    )

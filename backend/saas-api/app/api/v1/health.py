from fastapi import APIRouter

from app.core.config import settings
from app.shared.responses import ApiResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=ApiResponse,
    summary="Health Check",
)
async def health_check() -> ApiResponse:
    """
    Health endpoint.

    Used by
    - Load Balancer
    - Docker
    - Kubernetes
    - Monitoring
    """

    return ApiResponse(
        success=True,
        message="Platform healthy",
        data={
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "healthy",
        },
    )
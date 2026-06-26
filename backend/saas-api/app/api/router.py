"""
Central API router.

All API versions are registered here.

Application entrypoint -> router -> version -> endpoint.
"""

from fastapi import APIRouter

from app.api.v1.health import router as health_router

api_router = APIRouter(
    responses={
        500: {
            "description": "Internal server error.",
        },
    },
)

api_router.include_router(
    health_router,
    tags=["Health"],
)

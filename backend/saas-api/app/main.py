"""
Skincare SaaS Platform.

Application entrypoint.
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.middleware.exception_handler import register_exception_handlers
from app.shared.response_factory import ResponseFactory
from app.shared.responses import ApiResponse


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Enterprise Multi-Tenant SaaS Platform",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    register_exception_handlers(app)

    app.include_router(
        api_router,
        prefix=settings.API_PREFIX,
    )

    @app.get("/", tags=["Root"])
    async def root() -> ApiResponse[dict]:
        """
        Root endpoint.
        """

        return ResponseFactory.success(
            message="Application is running.",
            data={
                "application": settings.APP_NAME,
                "version": settings.APP_VERSION,
                "environment": settings.ENVIRONMENT,
            },
        )

    return app


app = create_app()

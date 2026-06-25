"""
Skincare SaaS Platform.

Application entry point.
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Multi-Tenant SaaS Platform",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)


@app.get(
    "/",
    tags=["Root"],
)
async def root():
    """
    Root endpoint.
    """

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
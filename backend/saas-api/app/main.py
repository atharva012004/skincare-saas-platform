from fastapi import FastAPI

from app.api.v1 import api_router
from app.core.config import settings
from app.core.startup import lifespan

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Multi Tenant SaaS Platform",
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)


@app.get("/")
async def root():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
"""
Application lifespan management.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import get_logger
from app.core.startup import startup
from app.db.engine import engine

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    FastAPI lifespan context.
    """

    await startup(app)

    yield

    logger.info("Shutting down application.")

    if app.state.platform.http_client:
        await app.state.platform.http_client.aclose()

    engine.dispose()

    logger.info("Application shutdown completed.")

"""
Application startup lifecycle.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import configure_logging
from app.core.logging import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan.
    """

    configure_logging()

    logger.info("Starting Skincare SaaS Platform")

    app.state.version = "0.1.0"

    yield

    logger.info("Shutting down Skincare SaaS Platform")
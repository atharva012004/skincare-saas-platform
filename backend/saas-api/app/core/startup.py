"""
Application startup initialization.
"""

from __future__ import annotations

import httpx
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging
from app.core.logging import get_logger
from app.core.state import ApplicationState


logger = get_logger(__name__)


async def startup(app: FastAPI) -> None:
    """
    Initialize application resources.
    """

    configure_logging()

    logger.info("Initializing platform...")

    http_client = httpx.AsyncClient(
        timeout=30.0,
        follow_redirects=True,
    )

    app.state.platform = ApplicationState(
        settings=settings,
        logger=logger,
        http_client=http_client,
    )

    logger.info("Platform initialized successfully.")
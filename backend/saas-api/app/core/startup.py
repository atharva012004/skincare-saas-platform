"""
Application startup.

Responsible for initializing all long-lived resources.
"""

from __future__ import annotations

import httpx
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import configure_logging, get_logger
from app.core.state import ApplicationState
from app.db.engine import engine
from app.db.health import check_database_connection
from app.db.session import SessionLocal

logger = get_logger(__name__)


async def startup(app: FastAPI) -> None:
    """
    Initialize application resources.
    """

    configure_logging()

    logger.info(
        "Starting %s (%s)",
        settings.APP_NAME,
        settings.ENVIRONMENT,
    )

    await check_database_connection()

    http_client = httpx.AsyncClient(
        timeout=httpx.Timeout(30.0),
        follow_redirects=True,
    )

    app.state.platform = ApplicationState(
        settings=settings,
        logger=logger,
        db_engine=engine,
        session_factory=SessionLocal,
        http_client=http_client,
    )

    logger.info("Application startup completed successfully.")

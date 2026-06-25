"""
Application state.

This module defines the strongly typed shared state attached to the
FastAPI application instance.

Only long-lived application resources should be stored here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import TYPE_CHECKING

import httpx
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from structlog.typing import FilteringBoundLogger

if TYPE_CHECKING:
    from app.core.config import Settings


@dataclass(slots=True)
class ApplicationState:
    """
    Shared application resources.

    This object is attached to:

        app.state.platform

    and remains alive for the entire application lifecycle.
    """

    settings: Settings

    logger: FilteringBoundLogger

    db_engine: Engine | None = None

    session_factory: sessionmaker | None = None

    http_client: httpx.AsyncClient | None = None

    started_at: datetime = field(default_factory=lambda: datetime.now(UTC))

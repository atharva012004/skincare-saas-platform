"""
Application state management.

This module defines the shared application state stored on
the FastAPI application instance.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from app.core.config import Settings


@dataclass(slots=True)
class ApplicationState:
    """
    Shared application state.

    Objects stored here live for the lifetime of the
    FastAPI application.
    """

    settings: Settings

    logger: Any

    http_client: httpx.AsyncClient
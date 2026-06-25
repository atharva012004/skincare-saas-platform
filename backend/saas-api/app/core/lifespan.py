"""
Application lifespan events.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.startup import startup


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan handler.
    """

    await startup(app)

    yield

    await app.state.platform.http_client.aclose()
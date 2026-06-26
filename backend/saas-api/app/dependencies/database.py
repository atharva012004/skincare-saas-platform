"""
Database dependencies.

Provides reusable FastAPI dependencies for database access.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db


async def get_database() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency wrapper for obtaining a database session.
    """

    async for session in get_db():
        yield session

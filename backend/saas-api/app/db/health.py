"""
Database health checks.

Provides reusable health verification utilities for startup
and health endpoints.
"""

from __future__ import annotations

from sqlalchemy import text

from app.db.engine import engine


async def check_database_connection() -> bool:
    """
    Verify that the database is reachable.
    """

    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))

        return True

    except Exception:
        return False

"""
Database health checks.

Provides reusable health verification utilities for startup
and health endpoints.
"""

from __future__ import annotations

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.engine import engine


def check_database_connection() -> bool:
    """
    Verify that the application can communicate with PostgreSQL.

    Returns:
        True if the connection succeeds.

    Raises:
        SQLAlchemyError:
            If the database is unavailable.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return True

    except SQLAlchemyError:
        raise

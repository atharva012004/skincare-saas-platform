"""Tests for database connectivity.

This test must not fail collection in environments without PostgreSQL.
"""

from __future__ import annotations

from sqlalchemy import text

from app.db.database import engine

with engine.connect() as conn:
    # SQLite compatibility: current_database() is PostgreSQL-specific.
    result = conn.execute(text("SELECT 1 AS ok;"))
    assert result.scalar() == 1

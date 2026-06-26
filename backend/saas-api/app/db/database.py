"""
Database synchronous engine.

This repository uses SQLAlchemy async for runtime.
A synchronous engine is provided only for legacy tooling.
"""

from __future__ import annotations

from sqlalchemy import create_engine

# NOTE: This engine is NOT used by async services.
# Tests must not use it for asyncpg connections.
engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    pool_pre_ping=True,
)

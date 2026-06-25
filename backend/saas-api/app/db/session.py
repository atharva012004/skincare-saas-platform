"""
Database session management.

Provides the SQLAlchemy Session factory and the FastAPI dependency.
"""

from __future__ import annotations

from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a database session.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

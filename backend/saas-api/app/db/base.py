"""
SQLAlchemy declarative base.

This module defines the application's declarative base and metadata
configuration. Every ORM model must inherit from Base.

The naming convention ensures deterministic constraint and index names,
which keeps Alembic migrations stable across environments.
"""

from __future__ import annotations

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Enterprise naming convention used by Alembic
NAMING_CONVENTION: dict[str, str] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": ("fk_%(table_name)s_" "%(column_0_name)s_" "%(referred_table_name)s"),
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(
    naming_convention=NAMING_CONVENTION,
)


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.
    """

    metadata = metadata

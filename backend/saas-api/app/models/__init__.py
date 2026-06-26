"""
Application ORM models.

Import SQLAlchemy models so they are registered with Base.metadata.
"""

from app.models.merchant import Merchant

__all__ = [
    "Merchant",
]

"""
FastAPI dependency providers.
"""

from app.dependencies.config import get_app_settings
from app.dependencies.database import get_database
from app.dependencies.repositories import get_merchant_repository
from app.dependencies.services import get_merchant_service

__all__ = [
    "get_app_settings",
    "get_database",
    "get_merchant_repository",
    "get_merchant_service",
]

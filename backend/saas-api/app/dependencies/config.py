"""
Configuration dependency providers.
"""

from __future__ import annotations

from app.core.config import Settings, settings


def get_app_settings() -> Settings:
    """
    Return application settings for FastAPI dependency injection.
    """

    return settings

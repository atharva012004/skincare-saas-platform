"""
Application configuration.

Centralized configuration management using Pydantic Settings.

All configuration must come from environment variables.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    Values are loaded from `.env`.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ---------------------------------------------------------
    # Application
    # ---------------------------------------------------------

    APP_NAME: str = Field(default="Skincare SaaS Platform")

    APP_VERSION: str = Field(default="0.1.0")

    ENVIRONMENT: Literal[
        "development",
        "testing",
        "staging",
        "production",
    ] = "development"

    DEBUG: bool = True

    # ---------------------------------------------------------
    # API
    # ---------------------------------------------------------

    API_PREFIX: str = "/api/v1"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    # ---------------------------------------------------------
    # Database
    # ---------------------------------------------------------

    DATABASE_URL: str

    DATABASE_ECHO: bool = False

    DATABASE_POOL_SIZE: int = 10

    DATABASE_MAX_OVERFLOW: int = 20

    DATABASE_POOL_TIMEOUT: int = 30

    DATABASE_POOL_RECYCLE: int = 1800

    DATABASE_POOL_PRE_PING: bool = True

    # ---------------------------------------------------------
    # Authentication Service
    # ---------------------------------------------------------

    AUTH_SERVICE_URL: str

    # ---------------------------------------------------------
    # JWT
    # ---------------------------------------------------------

    JWT_SECRET: str

    JWT_ALGORITHM: str = "HS256"

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    LOG_LEVEL: str = "INFO"

    # ---------------------------------------------------------
    # CORS
    # ---------------------------------------------------------

    ALLOWED_ORIGINS: str = "http://localhost:3000"


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """

    return Settings()  # type: ignore


settings = get_settings()

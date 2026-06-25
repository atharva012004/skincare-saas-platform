"""
Application-wide constants.
"""

from __future__ import annotations


class ErrorCodes:
    """Standard API error codes."""

    INTERNAL_ERROR = "internal_error"

    VALIDATION_ERROR = "validation_error"

    AUTHENTICATION_ERROR = "authentication_error"

    AUTHORIZATION_ERROR = "authorization_error"

    NOT_FOUND = "not_found"

    CONFLICT = "conflict"

    BUSINESS_ERROR = "business_error"

    DATABASE_ERROR = "database_error"

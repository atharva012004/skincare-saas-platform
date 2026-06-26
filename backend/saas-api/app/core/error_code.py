"""
Application error codes.
"""

from __future__ import annotations

from enum import StrEnum


class ErrorCode(StrEnum):
    """
    Machine-readable application error codes.
    """

    VALIDATION_ERROR = "validation_error"

    NOT_FOUND = "not_found"

    CONFLICT = "conflict"

    UNAUTHORIZED = "unauthorized"

    FORBIDDEN = "forbidden"

    INTERNAL_ERROR = "internal_error"

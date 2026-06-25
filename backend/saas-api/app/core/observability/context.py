"""
Request context.

Stores request specific information using ContextVar.
"""

from __future__ import annotations

from contextvars import ContextVar

request_id: ContextVar[str | None] = ContextVar(
    "request_id",
    default=None,
)

merchant_id: ContextVar[str | None] = ContextVar(
    "merchant_id",
    default=None,
)

user_id: ContextVar[str | None] = ContextVar(
    "user_id",
    default=None,
)
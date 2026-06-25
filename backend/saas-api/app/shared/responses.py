"""
Standard API response models.

These models define the single response contract used across the
Skincare SaaS Platform.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationMeta(BaseModel):
    """Pagination metadata."""

    page: int = Field(..., ge=1)
    page_size: int = Field(..., ge=1)
    total_items: int = Field(..., ge=0)
    total_pages: int = Field(..., ge=0)


class ResponseMeta(BaseModel):
    """Metadata returned with every response."""

    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))

    request_id: str | None = None

    execution_time_ms: float | None = None

    pagination: PaginationMeta | None = None


class ApiResponse(BaseModel, Generic[T]):
    """
    Generic successful API response.
    """

    success: bool = True

    message: str

    data: T | None = None

    meta: ResponseMeta = Field(default_factory=ResponseMeta)


class ErrorDetail(BaseModel):
    """Single validation or business error."""

    field: str | None = None
    message: str


class ErrorInfo(BaseModel):
    """Machine-readable error information."""

    code: str
    details: list[ErrorDetail] = Field(default_factory=list)


class ErrorResponse(BaseModel):
    """Standard API error response."""

    success: bool = False
    message: str
    error: ErrorInfo
    meta: ResponseMeta = Field(default_factory=ResponseMeta)

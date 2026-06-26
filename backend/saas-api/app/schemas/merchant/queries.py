"""Merchant list query schemas.

These schemas support pagination, search, sorting, and filtering.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class MerchantListQuery(BaseModel):
    """Query parameters for listing merchants."""

    page: int = Field(
        default=1,
        ge=1,
        description="Page number (1-indexed).",
    )

    page_size: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Number of items per page.",
    )

    search: str | None = Field(
        default=None,
        description="Search string applied to supported merchant fields.",
    )

    sort_by: str = Field(
        default="created_at",
        description="Field name to sort by.",
    )

    sort_order: str = Field(
        default="desc",
        description="Sort order: asc or desc.",
    )

    status: str | None = None
    merchant_type: str | None = None
    category: str | None = None
    country: str | None = None
    currency: str | None = None
    locale: str | None = None

    model_config = ConfigDict(extra="forbid")

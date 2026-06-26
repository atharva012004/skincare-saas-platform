"""
Common pagination schemas.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationMeta(BaseModel):
    """
    Pagination metadata.
    """

    page: int = Field(
        ...,
        ge=1,
        description="Current page number.",
    )

    page_size: int = Field(
        ...,
        ge=1,
        description="Number of items per page.",
    )

    total_items: int = Field(
        ...,
        ge=0,
        description="Total number of items.",
    )

    total_pages: int = Field(
        ...,
        ge=0,
        description="Total number of pages.",
    )

    has_next: bool = Field(
        ...,
        description="Whether another page exists.",
    )

    has_previous: bool = Field(
        ...,
        description="Whether a previous page exists.",
    )


class PageResponse(BaseModel, Generic[T]):
    """
    Standard paginated API response.
    """

    success: bool = Field(
        default=True,
    )

    message: str = Field(
        default="Request completed successfully.",
    )

    data: list[T]

    meta: PaginationMeta

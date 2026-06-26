"""
Common API response schemas.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    Standard API response.
    """

    success: bool = Field(
        default=True,
        description="Indicates whether the request succeeded.",
    )

    message: str = Field(
        default="Request completed successfully.",
        description="Human-readable response message.",
    )

    data: T | None = Field(
        default=None,
        description="Response payload.",
    )


class CreatedResponse(ApiResponse[T], Generic[T]):
    """
    Response returned after successful resource creation.
    """

    message: str = Field(
        default="Resource created successfully.",
    )


class EmptyResponse(BaseModel):
    """
    Response returned when no response payload is required.
    """

    success: bool = Field(
        default=True,
    )

    message: str = Field(
        default="Operation completed successfully.",
    )

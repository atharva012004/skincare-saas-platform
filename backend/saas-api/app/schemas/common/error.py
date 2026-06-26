"""
Common API error schemas.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    """
    Represents a single API error.
    """

    field: str | None = Field(
        default=None,
        description="Field associated with the error.",
    )

    code: str = Field(
        ...,
        description="Machine-readable error code.",
    )

    message: str = Field(
        ...,
        description="Human-readable error message.",
    )


class ErrorResponse(BaseModel):
    """
    Standard API error response.
    """

    success: bool = Field(
        default=False,
        description="Indicates request failure.",
    )

    message: str = Field(
        ...,
        description="Summary of the error.",
    )

    errors: list[ErrorDetail] = Field(
        default_factory=list,
        description="Detailed validation or business errors.",
    )

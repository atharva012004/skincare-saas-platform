"""
Merchant request schemas.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl

from app.models.enums import MerchantCategory, MerchantType
from app.schemas.merchant.base import MerchantBase


class MerchantCreateRequest(MerchantBase):
    """
    Request payload for creating a merchant.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    merchant_code: str

    slug: str


class MerchantUpdateRequest(BaseModel):
    """
    Request payload for updating a merchant.

    All fields are optional because PATCH requests support
    partial updates.
    """

    display_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )

    legal_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
    )

    email: EmailStr | None = None

    phone: str | None = Field(
        default=None,
        max_length=25,
    )

    website_url: HttpUrl | None = None

    country: str | None = Field(
        default=None,
        max_length=100,
    )

    currency: str | None = Field(
        default=None,
        max_length=10,
    )

    locale: str | None = Field(
        default=None,
        max_length=20,
    )

    timezone: str | None = Field(
        default=None,
        max_length=100,
    )

    merchant_type: MerchantType | None = None

    category: MerchantCategory | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )

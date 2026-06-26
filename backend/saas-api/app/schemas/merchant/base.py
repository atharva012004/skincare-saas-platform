"""
Base Merchant schemas.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl

from app.models.enums import MerchantCategory, MerchantType


class MerchantBase(BaseModel):
    """
    Shared merchant fields.
    """

    display_name: str = Field(
        ...,
        min_length=2,
        max_length=150,
    )

    legal_name: str = Field(
        ...,
        min_length=2,
        max_length=200,
    )

    email: EmailStr

    phone: str | None = Field(
        default=None,
        max_length=25,
    )

    website_url: HttpUrl | None = None

    country: str = Field(
        default="India",
        max_length=100,
    )

    currency: str = Field(
        default="INR",
        max_length=10,
    )

    locale: str = Field(
        default="en-IN",
        max_length=20,
    )

    timezone: str = Field(
        default="Asia/Kolkata",
        max_length=100,
    )

    merchant_type: MerchantType = MerchantType.BUSINESS

    category: MerchantCategory = MerchantCategory.SKINCARE

    model_config = ConfigDict(
        from_attributes=True,
    )

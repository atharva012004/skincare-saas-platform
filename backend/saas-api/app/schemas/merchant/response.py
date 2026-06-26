"""Merchant response schemas.

This module defines Pydantic v2 response DTOs for the Merchant REST API.
"""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl

from app.models.enums import MerchantCategory, MerchantStatus, MerchantType


class MerchantResponse(BaseModel):
    """Full merchant representation returned by the API."""

    id: UUID
    merchant_code: str
    slug: str

    display_name: str
    legal_name: str
    email: EmailStr

    phone: str | None
    website_url: HttpUrl | None
    logo_url: HttpUrl | None

    country: str
    currency: str
    locale: str
    timezone: str

    status: MerchantStatus
    merchant_type: MerchantType
    category: MerchantCategory

    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)


class MerchantCreateResponse(MerchantResponse):
    """Response DTO for merchant creation."""


class MerchantUpdateResponse(MerchantResponse):
    """Response DTO for merchant update."""


class MerchantDeleteResponse(BaseModel):
    """Response DTO for merchant deletion."""

    id: UUID
    is_deleted: bool
    deleted_at: datetime | None

    model_config = ConfigDict(from_attributes=True)

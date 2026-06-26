"""Merchant list response schemas.

These schemas describe the payload for listing merchants.
"""

from __future__ import annotations

from pydantic import BaseModel

from app.schemas.common.pagination import PaginationMeta
from app.schemas.merchant.response import MerchantResponse


class MerchantListResponse(BaseModel):
    """List endpoint response payload."""

    data: list[MerchantResponse]
    meta: PaginationMeta

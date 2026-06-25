"""
Merchant domain enumerations.
"""

from __future__ import annotations

from enum import StrEnum


class MerchantStatus(StrEnum):
    """
    Current lifecycle status of a merchant.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    ARCHIVED = "ARCHIVED"


class MerchantType(StrEnum):
    """
    Type of merchant account.
    """

    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"
    ENTERPRISE = "ENTERPRISE"


class MerchantCategory(StrEnum):
    """
    Business category of the merchant.
    """

    SKINCARE = "SKINCARE"
    COSMETICS = "COSMETICS"
    PHARMACY = "PHARMACY"
    SALON = "SALON"
    SPA = "SPA"
    DERMATOLOGY = "DERMATOLOGY"
    OTHER = "OTHER"

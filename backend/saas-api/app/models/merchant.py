"""
Merchant domain model.

Represents a tenant in the SaaS platform.
"""

from __future__ import annotations

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, BaseModelMixin
from app.models.enums import (
    MerchantCategory,
    MerchantStatus,
    MerchantType,
)


class Merchant(BaseModelMixin, Base):
    """
    Merchant (Tenant) entity.
    """

    __tablename__ = "merchants"

    merchant_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    display_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    legal_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(25),
        nullable=True,
    )

    website_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="India",
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="INR",
    )

    locale: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="en-IN",
    )

    timezone: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="Asia/Kolkata",
    )

    status: Mapped[MerchantStatus] = mapped_column(
        Enum(MerchantStatus, name="merchant_status"),
        nullable=False,
        default=MerchantStatus.ACTIVE,
    )

    merchant_type: Mapped[MerchantType] = mapped_column(
        Enum(MerchantType, name="merchant_type"),
        nullable=False,
        default=MerchantType.BUSINESS,
    )

    category: Mapped[MerchantCategory] = mapped_column(
        Enum(MerchantCategory, name="merchant_category"),
        nullable=False,
        default=MerchantCategory.SKINCARE,
    )

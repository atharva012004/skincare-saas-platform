"""
Merchant ownership mixin.

Provides a reusable merchant relationship for all tenant-owned entities.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.merchant import Merchant


class MerchantOwnedMixin:
    """
    Adds merchant ownership to a model.

    Any entity that belongs to a merchant should inherit this mixin.
    """

    merchant_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("merchants.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    @declared_attr.directive
    def merchant(self) -> Mapped[Merchant]:
        """
        Relationship to the owning merchant.
        """
        return relationship(
            "Merchant",
            lazy="selectin",
        )

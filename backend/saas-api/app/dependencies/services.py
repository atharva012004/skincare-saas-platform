"""
Service dependency providers.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from app.dependencies.repositories import DatabaseSession

if TYPE_CHECKING:
    from app.services.merchant_service import MerchantService


def get_merchant_service(
    session: DatabaseSession,
) -> MerchantService:
    """
    Provide a merchant service bound to the request database session.
    """

    from app.services.merchant_service import MerchantService

    return MerchantService(session)

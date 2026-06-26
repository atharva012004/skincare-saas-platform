"""
Merchant business validator.
"""

from __future__ import annotations

from app.repositories.merchant_repository import MerchantRepository
from app.shared.exceptions import ConflictException


class MerchantValidator:
    """
    Performs business validation for merchants.
    """

    def __init__(
        self,
        repository: MerchantRepository,
    ) -> None:
        self._repository = repository

    @property
    def repository(self) -> MerchantRepository:
        """
        Return the merchant repository.
        """

        return self._repository

    async def validate_create(
        self,
        *,
        email: str,
        slug: str,
        merchant_code: str,
    ) -> None:
        """
        Validate merchant creation.
        """

        if await self.repository.exists_by_email(email):
            raise ConflictException(
                "Merchant with this email already exists.",
            )

        if await self.repository.exists_by_slug(slug):
            raise ConflictException(
                "Merchant with this slug already exists.",
            )

        if await self.repository.exists_by_merchant_code(
            merchant_code,
        ):
            raise ConflictException(
                "Merchant with this merchant code already exists.",
            )

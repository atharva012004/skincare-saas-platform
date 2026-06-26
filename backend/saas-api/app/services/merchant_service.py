"""
Merchant service.

Contains business logic for merchant management.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.merchant import Merchant
from app.repositories.merchant_repository import MerchantRepository
from app.schemas.merchant.request import MerchantCreateRequest
from app.services.validators.merchant_validator import MerchantValidator
from app.shared.exceptions import ConflictException


class MerchantService:
    """
    Service for managing merchants.
    """

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session
        self._repository = MerchantRepository(session)
        self._validator = MerchantValidator(self._repository)

    @property
    def session(self) -> AsyncSession:
        """
        Return the active database session.
        """

        return self._session

    @property
    def repository(self) -> MerchantRepository:
        """
        Return the merchant repository.
        """

        return self._repository

    @property
    def validator(self) -> MerchantValidator:
        """
        Return the merchant validator.
        """

        return self._validator

    async def get_by_id(
        self,
        merchant_id: UUID,
    ) -> Merchant | None:
        """
        Retrieve a merchant by its unique identifier.
        """

        return await self.repository.get_by_id(merchant_id)

    async def get_by_slug(
        self,
        slug: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by slug.
        """

        return await self.repository.get_by_slug(slug)

    async def get_by_merchant_code(
        self,
        merchant_code: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by merchant code.
        """

        return await self.repository.get_by_merchant_code(
            merchant_code,
        )

    async def get_by_email(
        self,
        email: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by email.
        """

        return await self.repository.get_by_email(email)

    async def create_merchant(
        self,
        request: MerchantCreateRequest,
    ) -> Merchant:
        """
        Create a new merchant.
        """

        if await self.repository.exists_by_email(request.email):
            raise ConflictException(
                "Merchant with this email already exists.",
            )

        if await self.repository.exists_by_slug(request.slug):
            raise ConflictException(
                "Merchant with this slug already exists.",
            )

        if await self.repository.exists_by_merchant_code(
            request.merchant_code,
        ):
            raise ConflictException(
                "Merchant with this merchant code already exists.",
            )

        merchant = Merchant(
            merchant_code=request.merchant_code,
            slug=request.slug,
            display_name=request.display_name,
            legal_name=request.legal_name,
            email=request.email,
            phone=request.phone,
            website_url=request.website_url,
            country=request.country,
            currency=request.currency,
            locale=request.locale,
            timezone=request.timezone,
            merchant_type=request.merchant_type,
            category=request.category,
        )

        merchant = await self.repository.add_merchant(
            merchant,
        )

        await self.session.commit()

        await self.repository.refresh_merchant(
            merchant,
        )

        return merchant

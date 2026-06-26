"""
Merchant repository.

Provides merchant-specific database operations.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import cast
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.merchant import Merchant
from app.repositories.base import BaseRepository


class MerchantRepository(BaseRepository[Merchant]):
    """Merchant persistence repository."""

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        super().__init__(
            session=session,
            model=Merchant,
        )

    async def get_by_id(
        self,
        merchant_id: UUID,
    ) -> Merchant | None:
        """
        Retrieve a merchant by its unique identifier.
        """

        statement = self.query.where(
            Merchant.id == merchant_id,
            Merchant.is_deleted.is_(False),
        )

        result = await self._execute(statement)

        return cast(
            Merchant | None,
            result.scalar_one_or_none(),
        )

    async def get_by_slug(
        self,
        slug: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by slug.
        """

        statement = self.query.where(
            Merchant.slug == slug,
            Merchant.is_deleted.is_(False),
        )

        result = await self._execute(statement)

        return cast(
            Merchant | None,
            result.scalar_one_or_none(),
        )

    async def get_by_merchant_code(
        self,
        code: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by its merchant code.
        """

        statement = self.query.where(
            Merchant.merchant_code == code,
            Merchant.is_deleted.is_(False),
        )

        result = await self._execute(statement)

        return cast(
            Merchant | None,
            result.scalar_one_or_none(),
        )

    async def get_by_email(
        self,
        email: str,
    ) -> Merchant | None:
        """
        Retrieve a merchant by email.
        """

        statement = self.query.where(
            Merchant.email == email,
            Merchant.is_deleted.is_(False),
        )

        result = await self._execute(statement)

        return cast(
            Merchant | None,
            result.scalar_one_or_none(),
        )

    async def list_merchants(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Merchant]:
        """
        Return a paginated list of active merchants.
        """

        statement = (
            self.query.where(
                Merchant.is_deleted.is_(False),
            )
            .offset(offset)
            .limit(limit)
        )

        result = await self._execute(statement)

        return list(result.scalars().all())

    async def exists_by_slug(
        self,
        slug: str,
    ) -> bool:
        """
        Check whether a merchant slug exists.
        """

        return await self.get_by_slug(slug) is not None

    async def exists_by_merchant_code(
        self,
        code: str,
    ) -> bool:
        """
        Check whether a merchant code exists.
        """

        return await self.get_by_merchant_code(code) is not None

    async def exists_by_email(
        self,
        email: str,
    ) -> bool:
        """
        Check whether a merchant email exists.
        """

        return await self.get_by_email(email) is not None

    async def add_merchant(
        self,
        merchant: Merchant,
    ) -> Merchant:
        """
        Add a merchant.

        Transaction management is handled by the service layer.
        """

        return await self.add(merchant)

    async def refresh_merchant(
        self,
        merchant: Merchant,
    ) -> None:
        """
        Refresh a merchant from the database.
        """

        await self.refresh(merchant)

    async def soft_delete(
        self,
        merchant: Merchant,
    ) -> None:
        """
        Soft delete a merchant.

        Transaction management is handled by the service layer.
        """

        merchant.is_deleted = True
        merchant.deleted_at = datetime.now(UTC)

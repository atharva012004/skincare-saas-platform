"""Tests for MerchantRepository query behavior."""

from __future__ import annotations

from datetime import UTC, datetime

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.models.merchant import Merchant
from app.repositories.merchant_repository import MerchantRepository


@pytest.mark.asyncio
async def test_merchant_repository_list_and_soft_delete_exclusion() -> None:
    """Validate repository list behavior and default exclusion of soft-deleted rows."""

    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        echo=False,
        future=True,
    )

    async with engine.begin() as conn:
        await conn.execute(text("PRAGMA foreign_keys=ON;"))
        await conn.run_sync(Merchant.metadata.create_all)

    async with AsyncSession(engine) as session:
        repo = MerchantRepository(session)

        merchant1 = Merchant(
            merchant_code="M-CODE-1",
            slug="slug-one",
            display_name="Alpha Skin",
            legal_name="Alpha Legal",
            email="alpha@example.com",
            phone=None,
            website_url=None,
            country="India",
            currency="INR",
            locale="en-IN",
            timezone="Asia/Kolkata",
            merchant_type="BUSINESS",  # type: ignore[arg-type]
            category="SKINCARE",  # type: ignore[arg-type]
            status="ACTIVE",  # type: ignore[arg-type]
        )
        merchant2 = Merchant(
            merchant_code="M-CODE-2",
            slug="slug-two",
            display_name="Beta Shop",
            legal_name="Beta Legal",
            email="beta@example.com",
            phone=None,
            website_url=None,
            country="USA",
            currency="USD",
            locale="en-US",
            timezone="America/New_York",
            merchant_type="BUSINESS",  # type: ignore[arg-type]
            category="SKINCARE",  # type: ignore[arg-type]
            status="ACTIVE",  # type: ignore[arg-type]
        )

        session.add_all([merchant1, merchant2])
        await session.flush()

        merchant2.is_deleted = True
        merchant2.deleted_at = datetime.now(UTC)
        await session.flush()

        merchants = await repo.list_merchants(offset=0, limit=10)
        assert len(merchants) == 1
        assert merchants[0].slug == "slug-one"

    await engine.dispose()

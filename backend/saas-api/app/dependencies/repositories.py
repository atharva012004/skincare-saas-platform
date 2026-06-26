"""
Repository dependency providers.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.database import get_database
from app.repositories.merchant_repository import MerchantRepository

DatabaseSession = Annotated[AsyncSession, Depends(get_database)]


def get_merchant_repository(
    session: DatabaseSession,
) -> MerchantRepository:
    """
    Provide a merchant repository bound to the request database session.
    """

    return MerchantRepository(session)

"""
Generic SQLAlchemy repository.

Provides reusable asynchronous CRUD operations for all domain repositories.
"""

from __future__ import annotations

import uuid
from typing import Generic, TypeVar, cast

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.protocols import EntityProtocol

ModelType = TypeVar(
    "ModelType",
    bound=EntityProtocol,
)


class BaseRepository(Generic[ModelType]):
    """
    Generic repository for SQLAlchemy models.
    """

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        self.session = session
        self.model = model

    @property
    def query(self) -> Select[tuple[ModelType]]:
        """
        Base SELECT query.
        """

        return select(self.model)

    async def get_by_id(
        self,
        entity_id: uuid.UUID,
        *,
        include_deleted: bool = False,
    ) -> ModelType | None:
        """
        Retrieve an entity by its primary key.
        """

        statement = self.query.where(self.model.id == entity_id)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            statement = statement.where(self.model.is_deleted.is_(False))

        result = await self.session.execute(statement)

        return cast(ModelType | None, result.scalar_one_or_none())

    async def get_all(
        self,
        *,
        offset: int = 0,
        limit: int = 100,
        include_deleted: bool = False,
    ) -> list[ModelType]:
        """
        Return a paginated list of entities.
        """

        statement = self.query.offset(offset).limit(limit)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            statement = statement.where(self.model.is_deleted.is_(False))

        result = await self.session.execute(statement)

        return cast(list[ModelType], result.scalars().all())

    async def count(
        self,
        *,
        include_deleted: bool = False,
    ) -> int:
        """
        Count repository entities.
        """

        statement = select(func.count()).select_from(self.model)

        if hasattr(self.model, "is_deleted") and not include_deleted:
            statement = statement.where(self.model.is_deleted.is_(False))

        result = await self.session.execute(statement)

        return int(result.scalar_one())

    async def exists(
        self,
        entity_id: uuid.UUID,
    ) -> bool:
        """
        Check whether an entity exists.
        """

        return await self.get_by_id(entity_id) is not None

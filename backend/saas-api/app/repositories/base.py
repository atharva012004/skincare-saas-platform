"""
Generic SQLAlchemy repository.

Provides the base infrastructure for all repositories.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from sqlalchemy import Select, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Base repository providing common SQLAlchemy functionality.
    """

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        self._session = session
        self._model = model

    @property
    def session(self) -> AsyncSession:
        """
        Return the active database session.
        """

        return self._session

    @property
    def model(self) -> type[ModelType]:
        """
        Return the SQLAlchemy model handled by this repository.
        """

        return self._model

    @property
    def query(self) -> Select[tuple[ModelType]]:
        """
        Return the base SELECT query for the repository model.
        """

        return select(self.model)

    async def _execute(
        self,
        statement: Select,
    ) -> Result:
        """
        Execute a SQLAlchemy SELECT statement.
        """

        return await self.session.execute(statement)

    async def add(
        self,
        entity: ModelType,
    ) -> ModelType:
        """
        Add an entity to the current session.

        The entity is flushed so database-generated values become available.
        Transaction commit is managed by the service layer.
        """

        self.session.add(entity)
        await self.session.flush()

        return entity

    async def refresh(
        self,
        entity: ModelType,
    ) -> None:
        """
        Refresh an entity from the database.
        """

        await self.session.refresh(entity)

    async def delete(
        self,
        entity: ModelType,
    ) -> None:
        """
        Delete an entity from the current session.

        Transaction commit is managed by the service layer.
        """

        await self.session.delete(entity)
        await self.session.flush()

    async def commit(self) -> None:
        """
        Commit the active transaction.
        """

        await self.session.commit()

    async def rollback(self) -> None:
        """
        Roll back the active transaction.
        """

        await self.session.rollback()

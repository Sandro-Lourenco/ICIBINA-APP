from __future__ import annotations

from types import TracebackType
from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction, async_sessionmaker

from icibina.modules.courses.infrastructure.repositories import SQLAlchemyCourseRepository


class SQLAlchemyUnitOfWork:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory
        self._session: AsyncSession | None = None
        self._transaction: AsyncSessionTransaction | None = None
        self.courses: SQLAlchemyCourseRepository

    async def __aenter__(self) -> Self:
        self._session = self._session_factory()
        self._transaction = await self._session.begin()
        self.courses = SQLAlchemyCourseRepository(self._session)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        try:
            if self._transaction is not None and self._transaction.is_active:
                await self._transaction.rollback()
        finally:
            if self._session is not None:
                await self._session.close()

    async def commit(self) -> None:
        if self._transaction is None:
            raise RuntimeError("UnitOfWork has not been entered")
        await self._transaction.commit()

    async def rollback(self) -> None:
        if self._transaction is None:
            raise RuntimeError("UnitOfWork has not been entered")
        if self._transaction.is_active:
            await self._transaction.rollback()

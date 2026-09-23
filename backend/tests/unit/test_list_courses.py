from datetime import UTC, datetime
from types import TracebackType
from typing import Self
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from icibina.modules.courses.application.list_courses import ListCourses
from icibina.modules.courses.domain.entities import Course, CourseStatus


class FakeUnitOfWork:
    def __init__(self) -> None:
        self.courses = AsyncMock()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        return None

    async def commit(self) -> None:
        return None

    async def rollback(self) -> None:
        return None


@pytest.mark.parametrize(("requested", "expected"), [(0, 1), (50, 50), (5000, 50)])
async def test_list_courses_normalizes_limit(requested: int, expected: int) -> None:
    uow = FakeUnitOfWork()
    uow.courses.list_published.return_value = []

    result = await ListCourses(lambda: uow).execute(limit=requested)

    assert result == []
    uow.courses.list_published.assert_awaited_once_with(limit=expected)


async def test_list_courses_returns_domain_entities() -> None:
    now = datetime.now(UTC)
    course = Course(
        id=uuid4(),
        slug="fundamentos",
        title="Fundamentos",
        summary="Introdução",
        price_cents=0,
        currency="BRL",
        status=CourseStatus.PUBLISHED,
        published_at=now,
        created_at=now,
        updated_at=now,
    )
    uow = FakeUnitOfWork()
    uow.courses.list_published.return_value = [course]

    assert await ListCourses(lambda: uow).execute() == [course]

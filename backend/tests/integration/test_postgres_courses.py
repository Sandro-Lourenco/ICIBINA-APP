from datetime import UTC, datetime
from uuid import uuid4

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from icibina.infrastructure.database.uow import SQLAlchemyUnitOfWork
from icibina.modules.courses.domain.entities import CourseStatus
from icibina.modules.courses.infrastructure.models import CourseModel


@pytest.mark.integration
async def test_repository_lists_only_published_courses(
    integration_engine: AsyncEngine, clean_courses: None
) -> None:
    factory = async_sessionmaker(integration_engine, expire_on_commit=False)
    marker = uuid4().hex
    now = datetime.now(UTC)
    async with factory() as session:
        async with session.begin():
            session.add_all(
                [
                    CourseModel(
                        id=uuid4(),
                        slug=f"published-{marker}",
                        title="Published",
                        summary="Visible",
                        price_cents=100,
                        currency="BRL",
                        status=CourseStatus.PUBLISHED.value,
                        published_at=now,
                    ),
                    CourseModel(
                        id=uuid4(),
                        slug=f"draft-{marker}",
                        title="Draft",
                        summary="Hidden",
                        price_cents=100,
                        currency="BRL",
                        status=CourseStatus.DRAFT.value,
                    ),
                ]
            )

    async with SQLAlchemyUnitOfWork(factory) as uow:
        courses = await uow.courses.list_published(limit=50)

    assert f"published-{marker}" in {course.slug for course in courses}
    assert f"draft-{marker}" not in {course.slug for course in courses}


@pytest.mark.integration
async def test_unit_of_work_rolls_back_uncommitted_changes(
    integration_engine: AsyncEngine, clean_courses: None
) -> None:
    factory = async_sessionmaker(integration_engine, expire_on_commit=False)
    marker = uuid4().hex
    now = datetime.now(UTC)

    async with SQLAlchemyUnitOfWork(factory) as uow:
        assert uow._session is not None
        uow._session.add(
            CourseModel(
                id=uuid4(),
                slug=f"rollback-{marker}",
                title="Rollback",
                summary="Must not persist",
                price_cents=0,
                currency="BRL",
                status=CourseStatus.DRAFT.value,
                published_at=now,
            )
        )

    async with factory() as session:
        persisted = await session.scalar(
            CourseModel.__table__.select()
            .with_only_columns(CourseModel.id)
            .where(CourseModel.slug == f"rollback-{marker}")
        )
    assert persisted is None


@pytest.mark.integration
async def test_database_rejects_published_course_without_publication_time(
    integration_engine: AsyncEngine, clean_courses: None
) -> None:
    factory = async_sessionmaker(integration_engine, expire_on_commit=False)
    async with factory() as session:
        session.add(
            CourseModel(
                id=uuid4(),
                slug=f"invalid-published-{uuid4().hex}",
                title="Invalid",
                summary="Missing publication time",
                price_cents=0,
                currency="BRL",
                status=CourseStatus.PUBLISHED.value,
                published_at=None,
            )
        )
        with pytest.raises(IntegrityError):
            await session.commit()
        await session.rollback()

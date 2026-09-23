from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from icibina.modules.courses.domain.entities import Course, CourseStatus
from icibina.modules.courses.infrastructure.mapper import course_to_domain
from icibina.modules.courses.infrastructure.models import CourseModel


class SQLAlchemyCourseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def list_published(self, *, limit: int) -> list[Course]:
        statement = (
            select(CourseModel)
            .where(CourseModel.status == CourseStatus.PUBLISHED.value)
            .order_by(CourseModel.published_at.desc(), CourseModel.title.asc())
            .limit(limit)
        )
        result = await self._session.scalars(statement)
        return [course_to_domain(model) for model in result]

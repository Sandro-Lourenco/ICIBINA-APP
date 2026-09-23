from typing import Protocol

from icibina.modules.courses.domain.entities import Course


class CourseRepository(Protocol):
    async def list_published(self, *, limit: int) -> list[Course]: ...

from collections.abc import Callable

from icibina.application.unit_of_work import UnitOfWork
from icibina.modules.courses.domain.entities import Course


class ListCourses:
    def __init__(self, uow_factory: Callable[[], UnitOfWork]) -> None:
        self._uow_factory = uow_factory

    async def execute(self, *, limit: int = 50) -> list[Course]:
        safe_limit = max(1, min(limit, 50))
        async with self._uow_factory() as uow:
            return await uow.courses.list_published(limit=safe_limit)

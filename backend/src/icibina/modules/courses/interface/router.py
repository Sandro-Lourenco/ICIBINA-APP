from collections.abc import Callable
from typing import Annotated, cast

from fastapi import APIRouter, Depends, Query, Request

from icibina.application.unit_of_work import UnitOfWork
from icibina.errors import ErrorBody
from icibina.modules.courses.application.list_courses import ListCourses
from icibina.modules.courses.interface.schemas import CourseResponse

router = APIRouter(prefix="/api/v1/courses", tags=["courses"])


def get_uow_factory(request: Request) -> Callable[[], UnitOfWork]:
    return cast(Callable[[], UnitOfWork], request.app.state.uow_factory)


@router.get(
    "",
    response_model=list[CourseResponse],
    responses={422: {"model": ErrorBody, "description": "Request validation failed"}},
)
async def list_courses(
    uow_factory: Annotated[Callable[[], UnitOfWork], Depends(get_uow_factory)],
    limit: Annotated[int, Query()] = 50,
) -> list[CourseResponse]:
    courses = await ListCourses(uow_factory).execute(limit=limit)
    return [CourseResponse.model_validate(course) for course in courses]

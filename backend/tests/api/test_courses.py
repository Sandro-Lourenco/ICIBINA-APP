from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from types import TracebackType
from typing import Self
from unittest.mock import AsyncMock
from uuid import uuid4

from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from pydantic import SecretStr

from icibina.config import Settings
from icibina.main import create_app
from icibina.modules.courses.domain.entities import Course, CourseStatus
from icibina.modules.courses.interface.router import router


class FakeUnitOfWork:
    def __init__(self, courses: list[Course]) -> None:
        self.courses = AsyncMock()
        self.courses.list_published.return_value = courses

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


async def test_list_courses_api_serializes_catalog() -> None:
    now = datetime.now(UTC)
    course = Course(
        id=uuid4(),
        slug="fundamentos",
        title="Fundamentos",
        summary="Introdução",
        price_cents=12900,
        currency="BRL",
        status=CourseStatus.PUBLISHED,
        published_at=now,
        created_at=now,
        updated_at=now,
    )
    uow = FakeUnitOfWork([course])

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        app.state.uow_factory = lambda: uow
        yield

    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    async with app.router.lifespan_context(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/api/v1/courses", params={"limit": 5000})

    assert response.status_code == 200
    assert response.json()[0]["slug"] == "fundamentos"
    assert response.json()[0]["price_cents"] == 12900
    uow.courses.list_published.assert_awaited_once_with(limit=50)


async def test_validation_error_matches_openapi_contract() -> None:
    app = create_app(
        Settings(
            app_env="test",
            database_url=SecretStr(
                "postgresql+asyncpg://icibina_app:placeholder@localhost:5432/ICIBINA_test"
            ),
            database_migration_url=SecretStr(
                "postgresql+asyncpg://icibina_migrator:placeholder@localhost:5432/ICIBINA_test"
            ),
        )
    )
    async with app.router.lifespan_context(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get(
                "/api/v1/courses",
                params={"limit": "not-an-integer"},
                headers={"X-Request-ID": "test-request-id"},
            )

    assert response.status_code == 422
    assert response.json()["code"] == "validation_error"
    assert response.json()["request_id"] == "test-request-id"
    assert isinstance(response.json()["details"], list)
    response_schema = app.openapi()["paths"]["/api/v1/courses"]["get"]["responses"]["422"]
    assert response_schema["content"]["application/json"]["schema"]["$ref"].endswith("/ErrorBody")

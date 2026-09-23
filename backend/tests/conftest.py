from collections.abc import AsyncIterator

import pytest
import pytest_asyncio
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from test_support.database import IntegrationDatabaseSettings

from icibina.modules.courses.infrastructure.models import CourseModel


@pytest.fixture(scope="session")
def integration_database_settings() -> IntegrationDatabaseSettings:
    return IntegrationDatabaseSettings()  # type: ignore[call-arg]


@pytest_asyncio.fixture
async def integration_engine(
    integration_database_settings: IntegrationDatabaseSettings,
) -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(
        integration_database_settings.test_database_url.get_secret_value(),
        pool_pre_ping=True,
        connect_args={"ssl": integration_database_settings.database_ssl},
    )
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture
async def clean_courses(integration_engine: AsyncEngine) -> AsyncIterator[None]:
    async with integration_engine.begin() as connection:
        await connection.execute(delete(CourseModel))
    yield
    async with integration_engine.begin() as connection:
        await connection.execute(delete(CourseModel))

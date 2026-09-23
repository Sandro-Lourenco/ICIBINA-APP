import pytest
from httpx import ASGITransport, AsyncClient
from pydantic import SecretStr
from test_support.database import IntegrationDatabaseSettings

from icibina.config import Settings
from icibina.main import create_app

pytestmark = pytest.mark.integration


async def test_real_database_readiness_and_courses_api(
    integration_database_settings: IntegrationDatabaseSettings,
    clean_courses: None,
) -> None:
    app = create_app(
        Settings(
            app_env="test",
            database_url=SecretStr(
                integration_database_settings.test_database_url.get_secret_value()
            ),
            database_migration_url=SecretStr(
                integration_database_settings.test_database_migration_url.get_secret_value()
            ),
        )
    )
    async with app.router.lifespan_context(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            readiness = await client.get("/health/ready")
            courses = await client.get("/api/v1/courses")

    assert readiness.status_code == 200
    assert readiness.json() == {"status": "ready"}
    assert courses.status_code == 200
    assert isinstance(courses.json(), list)

from __future__ import annotations

from typing import Self

from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL, make_url


def assert_test_database_url(value: SecretStr, *, variable_name: str) -> URL:
    url = make_url(value.get_secret_value())
    database = url.database or ""
    if not database.lower().endswith("_test"):
        raise ValueError(f"{variable_name} must target an explicit *_test database")
    return url


class IntegrationDatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None, extra="ignore", case_sensitive=False)

    test_database_url: SecretStr
    test_database_migration_url: SecretStr
    test_mcp_database_url: SecretStr
    database_ssl: bool = False

    @model_validator(mode="after")
    def validate_test_databases_and_roles(self) -> Self:
        runtime = assert_test_database_url(
            self.test_database_url, variable_name="TEST_DATABASE_URL"
        )
        migration = assert_test_database_url(
            self.test_database_migration_url,
            variable_name="TEST_DATABASE_MIGRATION_URL",
        )
        mcp = assert_test_database_url(
            self.test_mcp_database_url, variable_name="TEST_MCP_DATABASE_URL"
        )
        expected_roles = (
            (runtime, "icibina_app", "TEST_DATABASE_URL"),
            (migration, "icibina_migrator", "TEST_DATABASE_MIGRATION_URL"),
            (mcp, "icibina_mcp_reader", "TEST_MCP_DATABASE_URL"),
        )
        for url, expected, variable_name in expected_roles:
            if url.username != expected:
                raise ValueError(f"{variable_name} must use role {expected}")
        if not (runtime.database == migration.database == mcp.database):
            raise ValueError("all test database URLs must target the same database")
        return self

    def asyncpg_dsn(self, value: SecretStr) -> str:
        url = make_url(value.get_secret_value()).set(drivername="postgresql")
        return url.render_as_string(hide_password=False)

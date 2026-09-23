import pytest
from pydantic import ValidationError
from test_support.database import IntegrationDatabaseSettings


def test_test_database_configuration_is_required(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in (
        "TEST_DATABASE_URL",
        "TEST_DATABASE_MIGRATION_URL",
        "TEST_MCP_DATABASE_URL",
    ):
        monkeypatch.delenv(key, raising=False)

    with pytest.raises(ValidationError):
        IntegrationDatabaseSettings()  # type: ignore[call-arg]


def test_normal_database_is_rejected_before_connection(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(
        "TEST_DATABASE_URL",
        "postgresql+asyncpg://icibina_app:placeholder@localhost:5432/ICIBINA",
    )
    monkeypatch.setenv(
        "TEST_DATABASE_MIGRATION_URL",
        "postgresql+asyncpg://icibina_migrator:placeholder@localhost:5432/ICIBINA_test",
    )
    monkeypatch.setenv(
        "TEST_MCP_DATABASE_URL",
        "postgresql://icibina_mcp_reader:placeholder@localhost:5432/ICIBINA_test",
    )

    with pytest.raises(ValidationError, match="explicit.*_test"):
        IntegrationDatabaseSettings()  # type: ignore[call-arg]

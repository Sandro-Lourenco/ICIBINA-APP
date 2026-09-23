import logging

from pydantic import SecretStr

from icibina.config import Settings
from icibina.logging_config import configure_logging


def test_logging_configuration_applies_requested_level() -> None:
    configure_logging("DEBUG")

    assert logging.getLogger("icibina").getEffectiveLevel() == logging.DEBUG


def test_settings_normalizes_log_level() -> None:
    settings = Settings(
        database_url=SecretStr(
            "postgresql+asyncpg://icibina_app:placeholder@localhost:5432/ICIBINA"
        ),
        database_migration_url=SecretStr(
            "postgresql+asyncpg://icibina_migrator:placeholder@localhost:5432/ICIBINA"
        ),
        log_level="debug",  # type: ignore[arg-type]
    )

    assert settings.log_level == "DEBUG"

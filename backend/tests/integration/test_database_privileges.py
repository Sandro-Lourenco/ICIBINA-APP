from __future__ import annotations

import asyncpg
import pytest
from test_support.database import IntegrationDatabaseSettings


@pytest.mark.integration
async def test_runtime_role_cannot_create_tables(
    integration_database_settings: IntegrationDatabaseSettings,
) -> None:
    connection = await asyncpg.connect(
        integration_database_settings.asyncpg_dsn(integration_database_settings.test_database_url),
        ssl=integration_database_settings.database_ssl,
    )
    try:
        with pytest.raises(asyncpg.InsufficientPrivilegeError):
            await connection.execute("CREATE TABLE runtime_role_must_not_create (id integer)")
    finally:
        await connection.close()


@pytest.mark.integration
async def test_mcp_role_cannot_read_application_tables(
    integration_database_settings: IntegrationDatabaseSettings,
) -> None:
    connection = await asyncpg.connect(
        integration_database_settings.asyncpg_dsn(
            integration_database_settings.test_mcp_database_url
        ),
        ssl=integration_database_settings.database_ssl,
    )
    try:
        with pytest.raises(asyncpg.InsufficientPrivilegeError):
            await connection.fetch("SELECT id FROM public.courses LIMIT 1")
    finally:
        await connection.close()

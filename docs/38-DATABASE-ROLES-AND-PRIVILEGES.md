# 38 — Database roles and privileges — ICIBINA

## Canonical role model

```text
icibina_owner      -> bootstrap/database owner only; never application traffic
icibina_migrator   -> applies Alembic DDL and owns migration-created objects
icibina_app        -> API/worker runtime DML; no DDL/admin privileges
icibina_mcp_reader -> AI inspection; read-only and agent_inspection only
```

Never use a superuser in the backend or MCP.

## Local development

`docker-compose.target.yml` bootstraps PostgreSQL with `icibina_owner`, then mounts `database/bootstrap/00_roles.sh` into `docker-entrypoint-initdb.d`. On a **fresh volume**, that bootstrap creates the three operational roles and default privileges.

The local `.env` contract is:

```text
DATABASE_URL           -> icibina_app
DATABASE_MIGRATION_URL -> icibina_migrator
MCP                    -> icibina_mcp_reader
```

If an old `pgdata` volume predates this bootstrap, recreate the local volume or apply the bootstrap deliberately; Docker init scripts run only on first database initialization.

## Runtime privilege tests

Before release, prove these invariants against an isolated database:

- `icibina_migrator` can run `alembic upgrade head`;
- `icibina_app` can execute required DML but cannot `CREATE TABLE`/`ALTER TABLE`;
- `icibina_mcp_reader` cannot read application schemas and cannot execute DML;
- `icibina_mcp_reader` can read only approved `agent_inspection` views.

## Default privileges

Objects created by `icibina_migrator` in `public` grant runtime DML to `icibina_app` through `ALTER DEFAULT PRIVILEGES`. If the implementation later adopts per-module schemas, reproduce the same policy per schema through Alembic/bootstrap operations.

## MCP reader

`database/003_mcp_readonly_role.sql` remains an operational hardening reference. The local bootstrap creates the role earlier so the development environment is executable. Production must create credentials out-of-band and use separate secret scopes.

## Migration identity

Deploy pipelines use `DATABASE_MIGRATION_URL`; application processes receive only `DATABASE_URL`. Application startup must not silently run schema migrations.

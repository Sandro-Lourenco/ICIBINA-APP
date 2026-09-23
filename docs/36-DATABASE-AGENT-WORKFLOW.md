# 36 — Database Agent Workflow

```text
persistence task
 -> DATABASE-CONTRACT
 -> inspect model/repository/migration/tests
 -> database-persistence-orchestrator
 -> SQLAlchemy/Alembic implementation
 -> Postgres/SQL specialist only for hard query/tuning
 -> migration/integration tests
 -> MCP read-only verification when useful
```

## DDL source

Nunca:

```text
agent -> MCP modify -> schema
```

Sempre:

```text
agent -> Python model -> Alembic -> review -> test -> upgrade
```

## MCP

Use `icibina-readonly`; se o profile não existir, não improvise credenciais e não trocar para superuser. Reporte o setup pendente.

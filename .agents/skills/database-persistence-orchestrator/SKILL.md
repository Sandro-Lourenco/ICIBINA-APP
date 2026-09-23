---
name: database-persistence-orchestrator
description: Coordena mudanças de persistência ICIBINA envolvendo SQLAlchemy models, repositories, Unit of Work, Alembic migrations, índices, queries ou PostgreSQL.
---

# Database Persistence Orchestrator

## Contexto inicial

Leia somente `docs/contracts/DATABASE-CONTRACT.md`, o model/repository/migration afetado e seus testes.

## Fonte de verdade

```text
Domain entity/value object
       !=
SQLAlchemy persistence model
```

Schema aplicado:

```text
SQLAlchemy typed models
 -> Alembic autogenerate/manual revision
 -> review de DDL/locks/data migration
 -> migration test
 -> upgrade
```

## Especialistas externos sob demanda

- `postgres-pro`: tuning, EXPLAIN/BUFFERS, pg_stat, VACUUM/index strategy.
- `sql-pro`: query/schema SQL complexo.
- Para comportamento específico do PostgreSQL 18, documentação oficial prevalece.
- Não carregar essas skills para um CRUD/model simples sem necessidade.

## MCP policy

- MCP `icibina-postgres` é read-only por padrão.
- Use para introspecção, contexto e diagnóstico; não para DDL/DML.
- Schema change via MCP é proibido neste projeto.

## Transaction policy

- Unit of Work controla commit/rollback.
- Repository recebe session/UoW conforme composição local e não chama commit escondido.
- Operações idempotentes devem possuir constraint/unique key além de checagem em código quando possível.

<!-- Runtime discovery diagnostic; not a product instruction. -->
SMOKE_MARKER: `ICIBINA_SMOKE_DATABASE_ORCHESTRATOR_V5_8`

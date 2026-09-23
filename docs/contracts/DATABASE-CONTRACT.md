# Database Contract — ICIBINA

## Identidade

- Banco de desenvolvimento/produção: **`ICIBINA`**.
- Banco de CI: **`ICIBINA_test`**.
- PostgreSQL 18 é a fonte transacional.

## Fonte de schema

- Models ORM: SQLAlchemy 2 typed ORM (`Mapped`, `mapped_column`, `DeclarativeBase`).
- Driver: `asyncpg` via SQLAlchemy asyncio.
- Migrations: Alembic é a **única** fonte de DDL aplicada pela aplicação.
- `database/*.sql` do blueprint são referência/bootstrap operacional; não substituem Alembic.
- Autogenerate exige revisão; nunca aplicar migration gerada sem inspeção.

## Transações

- Unit of Work delimita `begin/commit/rollback`.
- Repository executa persistência, não decide fronteira transacional.
- Use cases que alteram múltiplos agregados devem declarar atomicidade esperada.

## MCP

- MCP PostgreSQL serve para **inspeção, diagnóstico, schema context e performance**.
- Perfil padrão de agente: `icibina-readonly` usando role `icibina_mcp_reader` e `access_mode=ro`.
- Nunca usar MCP read-only para criar/alterar schema.
- Writes/schema: SQLAlchemy model -> Alembic revision -> review -> migration.
- Nunca conectar agente exploratório como superuser/owner.

## Contexto sob demanda

- modelo: `docs/02-POSTGRESQL-MODELO-DADOS.md`
- migrations: `docs/22-DATABASE-MIGRATION-POLICY.md`
- ORM: `docs/34-ORM-SQLALCHEMY-ALEMBIC.md`
- MCP: `docs/33-MCP-POSTGRESQL-ICIBINA.md`
- performance: `docs/23-PERFORMANCE-CAPACITY-MODEL.md`

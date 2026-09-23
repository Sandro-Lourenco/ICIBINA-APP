# ADR-002 — PostgreSQL + SQLAlchemy async

**Status:** Accepted

## Decision
O banco PostgreSQL oficial da plataforma é `ICIBINA`. PostgreSQL é a fonte transacional. SQLAlchemy 2 async + asyncpg implementam persistence adapters. Alembic é a fonte de schema change.

## Consequences
FK/constraints/transações fortes; migrations e pool precisam disciplina operacional.

## Alternatives
Supabase/PostgREST direto foi rejeitado para o novo core por acoplamento e portabilidade.

## Agent/MCP boundary

MCP PostgreSQL é read-only de inspeção. Models SQLAlchemy + Alembic continuam sendo a única via de alteração de schema.

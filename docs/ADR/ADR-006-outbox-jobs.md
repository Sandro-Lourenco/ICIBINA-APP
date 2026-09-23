# ADR-006 — PostgreSQL Outbox/Jobs como durabilidade inicial

**Status:** Accepted

## Decision
Eventos/jobs críticos são registrados na mesma transação que a mudança de negócio. Workers usam claim atômico/lease/retry. Redis fica para cache/coordenação efêmera inicialmente.

## Consequences
Evita dual-write inconsistente e reduz infraestrutura inicial.

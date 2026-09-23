# Schema source of truth

## Blueprint phase

`database/001_initial_schema.sql` e `002_medical_education_extensions.sql` são **modelagem histórica/referência**, nunca migrations de produção.

## Implementation phase

A autoridade vira:

1. SQLAlchemy typed models aprovados;
2. Alembic revision history;
3. PostgreSQL live schema como evidência do que está aplicado.

O live DB não é editado para “consertar” drift. Drift é resolvido por model/migration revisada.

## Regra para agentes

- não manter manualmente SQL de referência em sincronia depois da primeira baseline Alembic;
- mover referências históricas para archive quando a baseline real existir;
- schema changes via `alembic revision` + review + tests;
- raw SQL em migration só quando necessário e explicado.

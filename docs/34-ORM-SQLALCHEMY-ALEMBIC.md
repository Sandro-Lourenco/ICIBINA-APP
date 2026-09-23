# 34 — ORM SQLAlchemy + Alembic — ICIBINA

## Decisão

A ICIBINA usa ORM em Python com:

```text
SQLAlchemy 2 typed ORM
SQLAlchemy asyncio
asyncpg
Alembic
PostgreSQL 18
```

## Separação

```text
domain/course.py              # entidade/regras, zero SQLAlchemy
infrastructure/db/models.py   # persistence model SQLAlchemy
infrastructure/repositories/  # adapters
application/                  # use cases + UoW port
```

Não transformar entidade de domínio em model ORM só para economizar mapper.

## Base ORM alvo

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

Models novos usam `Mapped[T]` + `mapped_column` e relationships tipadas.

## Async engine

```python
engine = create_async_engine(settings.database_url, pool_pre_ping=True)
SessionFactory = async_sessionmaker(engine, expire_on_commit=False)
```

Configuração de pool é calibrada por carga; não copiar números arbitrários.

## Unit of Work

O UoW é dono de begin/commit/rollback. Repositories não chamam `commit()` escondido.

Pseudo-contrato:

```python
async with uow:
    course = await uow.courses.get(course_id)
    ...
    await uow.commit()
```

## Alembic

- única fonte de schema change da aplicação;
- autogenerate é rascunho, não aprovação automática;
- revisar nullability, FK, defaults, indexes, constraints, locks e data migration;
- schema incompatível usa expand -> migrate/backfill -> contract;
- migration test roda em PostgreSQL real.

## SQL de referência

`database/001_initial_schema.sql` e `002_medical_education_extensions.sql` são documentação/modelagem. Converter para models + revisions reais; não aplicar manualmente em produção.

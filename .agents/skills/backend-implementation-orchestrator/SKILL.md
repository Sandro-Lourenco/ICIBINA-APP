---
name: backend-implementation-orchestrator
description: Coordena implementação FastAPI da ICIBINA quando a tarefa cria ou altera endpoints, use cases, Pydantic schemas, autenticação ou adapters backend, preservando Clean Architecture e Unit of Work.
---

# Backend Implementation Orchestrator

## Carregamento mínimo

1. Leia `docs/contracts/BACKEND-CONTRACT.md`.
2. Inspecione o módulo/código/testes diretamente afetados.
3. Só carregue docs grandes se houver decisão não coberta pelo contrato.

## Uso de especialistas externos

- `fastapi` (skill oficial): mecânica FastAPI/Pydantic/async/OpenAPI e detalhes version-sensitive. Não aceite a preferência genérica por SQLModel; ICIBINA usa SQLAlchemy 2 conforme ADR/contrato local.
- A arquitetura local **sempre prevalece** sobre exemplos genéricos da skill externa.
- Nunca copie o padrão genérico `router -> AsyncSession -> crud -> commit()` para ICIBINA.

## Pipeline

```text
request
 -> router/interface
 -> DTO/Pydantic transport
 -> application use case
 -> domain ports/entities
 -> infrastructure adapter
 -> Unit of Work transaction
```

## Guards

- router não usa SQLAlchemy;
- application não importa infrastructure;
- repository não decide commit arbitrário;
- domain não depende de framework;
- ownership é verificado no use case/authorization policy;
- endpoint novo atualiza OpenAPI/testes.

Se a tarefa tocar schema/repository/query/migration, acione também `$database-persistence-orchestrator`.

<!-- Runtime discovery diagnostic; not a product instruction. -->
SMOKE_MARKER: `ICIBINA_SMOKE_BACKEND_ORCHESTRATOR_V5_8`

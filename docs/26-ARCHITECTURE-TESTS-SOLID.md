# 26 — Architecture Tests + SOLID — ICIBINA

## Dependency rule

```text
interface -> application -> domain
infrastructure -> domain ports/application composition
```

### Proibido

- domain -> FastAPI/SQLAlchemy/Redis/httpx/Pydantic transport;
- application -> infrastructure;
- interface/router -> SQLAlchemy;
- repository adapter -> `commit()`/`rollback()` escondido;
- módulo acessar internals/repository de outro módulo por conveniência.

`scripts/check_architecture.py` fiscaliza as primeiras regras via AST quando `backend/src` existir. Expanda com regras específicas conforme os packages reais forem criados.

## SOLID

- S: use case/componente tem responsabilidade de negócio coerente;
- O/D: providers entram por ports/adapters;
- L: adapters importantes compartilham contract tests;
- I: ports pequenos orientados ao consumidor;
- abstração genérica só quando contrato é estável e reduz duplicação real.

## Transaction ownership

Unit of Work delimita commit/rollback. Repository não esconde transação. Essa regra evita commits parciais e torna teste/rollback previsível.

## Reuse

`colocate first -> share after stable repeated concept`. Evitar `utils.py`, `common.py`, `BaseService` ou `GenericRepository` sem semântica de domínio.

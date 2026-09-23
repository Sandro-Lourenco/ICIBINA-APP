# 35 — Backend Agent Workflow

```text
backend task
 -> BACKEND-CONTRACT
 -> inspect module + tests
 -> backend-implementation-orchestrator
 -> FastAPI expert only for framework mechanics
 -> database orchestrator only if persistence changes
 -> narrow tests
 -> architecture check
 -> quality gate at handoff
```

## Regra crítica sobre FastAPI skill

Exemplos externos de `router -> AsyncSession -> crud -> commit()` não são arquitetura ICIBINA. Router converte HTTP e chama use case. SQLAlchemy fica em infrastructure e transação no UoW.

## Quando chamar Course Platform Architect

Somente quando a mudança altera fronteira, port, transação estrutural, bounded context, auth model ou exige ADR. Não usar em endpoint CRUD comum.

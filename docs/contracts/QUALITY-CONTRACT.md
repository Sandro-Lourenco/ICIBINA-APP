# Quality Contract — ICIBINA

A mudança só está pronta quando há evidência compatível com o risco.

## Sempre

- diff pequeno e relacionado ao objetivo;
- lint/format/typecheck aplicáveis;
- testes afetados;
- `git diff --check`;
- nenhuma alegação de teste/benchmark sem execução.

## Backend

- pytest + autorização negativa quando recurso privado;
- architecture check;
- migration upgrade em Postgres real quando houver schema;
- sem `commit()` escondido em repository;
- sem I/O síncrono acidental no event loop.

## Frontend

- lint/typecheck/test/build;
- loading/error/empty/success;
- teclado/foco/labels/reduced-motion;
- Playwright/axe/visual quando UI substancial;
- design system e page override preservados.

## High risk

Pagamento, sessão, role, migration e webhook exigem regressões negativas, idempotência quando aplicável, audit trail e rollback/reconciliation documentado.

## Final gate

Use `$platform-quality-gate` somente no handoff/milestone. Para revisão/refactor de código use `$code-quality-orchestrator` sob demanda, não em toda edição.

# 37 — Quality Orchestration

## Papéis

- `$code-quality-orchestrator`: review/refactor/smells/SOLID sob demanda.
- `$platform-quality-gate`: agregador final para handoff/milestone/release.
- CI: enforcement determinístico; documentação não substitui automação.

## Não carregar Clean Code externo por padrão

A skill externa é ampla e cara em contexto. Fica classificada como `manual-review-only` no manifest. A política local compacta está no `code-quality-orchestrator`.

## Gates esperados

Backend: Ruff, format, mypy, pytest+coverage, architecture checks, Alembic upgrade quando schema, OpenAPI compatibility quando configurado.

Frontend: lint, typecheck, tests, build, E2E, axe, visual regression, bundle budget quando scripts existirem.

Supply chain: lockfiles, dependency/security scan e secret scan no pipeline real.

## No false green

Gates opcionais ainda não implementados devem aparecer como `PENDING/SKIPPED`, nunca como aprovados.

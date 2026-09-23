---
name: platform-quality-gate
description: Agrega evidência final de mudança substancial, PR, milestone ou release ICIBINA. Use no handoff; não durante cada edição.
---
# Platform Quality Gate

Leia `docs/contracts/QUALITY-CONTRACT.md`, o diff e evidence file quando existir. Não recarregue todas as skills usadas na implementação.

## Por risco
- Backend: lint/format/typecheck, tests/coverage, authz negativa, architecture checks, migration smoke.
- Frontend: lint/typecheck/unit/build, E2E, a11y, visual, bundle quando exigidos.
- Database: Alembic, DB real, transaction ownership, rollback/expand-contract.
- Financeiro: preço server-side, idempotência, webhook auth/replay/out-of-order.
- Security: secrets/SAST/dependencies/container scan conforme release stage.
- Observability/performance: só declare melhoria com baseline/evidência.

## Evidence
`SKIPPED/PENDING != PASS`. `PASS` exige comando/artefato verificável. Registre skills externas efetivamente usadas, não as que apenas estavam instaladas.

<!-- Runtime discovery diagnostic; not a product instruction. -->
SMOKE_MARKER: `ICIBINA_SMOKE_QUALITY_GATE_V5_8`

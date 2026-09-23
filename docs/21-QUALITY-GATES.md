# 21 — Quality Gates — ICIBINA

## Princípio

Documentação define o padrão; CI deve provar o máximo possível. `SKIPPED/PENDING` não é `PASS`.

## Blueprint gates

```bash
python scripts/validate-agent-config.py
python scripts/validate-blueprint.py
python scripts/validate-doc-links.py
python scripts/check-design-tokens.py
python scripts/check-experience-system.py
python scripts/check-uiux-pro-max-bridge.py
python scripts/check-shadcn-bootstrap-contract.py
python scripts/check-database-identity.py
python scripts/check-mcp-config.py
python scripts/check-21st-design-context.py
python scripts/check-context-routing.py
python scripts/check_architecture.py
```

## Backend implementado

- Ruff check + format check;
- mypy;
- pytest com coverage global alvo >= 80%; módulos críticos auth/payments/permissions alvo >= 90% quando a suite estiver categorizada;
- authorization/BOLA regressions;
- architecture fitness functions;
- Alembic upgrade em `ICIBINA_test` quando `alembic.ini` existir;
- OpenAPI compatibility check quando baseline for criada;
- dependency/security/secret scan na pipeline real.

## Frontend implementado

- npm ci + lint + typecheck + tests + build;
- Playwright E2E;
- axe/a11y quando script configurado;
- visual regression quando baseline configurada;
- smoke de forced-colors/high-contrast em rotas críticas e componentes de foco/seleção/status;
- Core Web Vitals/bundle budget em milestone/release.

## High-risk

Pagamento, auth, role, session, migration, webhook: negative tests, idempotency/replay/out-of-order conforme domínio, audit trail e rollback/reconciliation.

## Handoff gate

`$platform-quality-gate` agrega evidência e nunca substitui os comandos acima.


## V5 release semantics
No release, ausência de `test:e2e`, `test:a11y`, `test:visual` ou `check:bundle` em frontend implementado é FAIL. Veja docs/44.


## V5.3 mandatory release evidence

Além dos gates anteriores, release com backend real exige: PostgreSQL isolado, Alembic via `icibina_migrator`, DDL negado ao `icibina_app`, markers `authz` e `payments_security`, export OpenAPI + oasdiff breaking check e SBOM CycloneDX. Frontend real passa também por `check_frontend_architecture.py`.

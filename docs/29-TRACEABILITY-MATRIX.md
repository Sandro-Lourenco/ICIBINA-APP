# 29 — Traceability Matrix

Esta matriz liga intenção → fonte canônica → verificação. Ela existe para impedir que regras importantes permaneçam somente em prosa.

| Concern | Source of truth | Executable evidence |
|---|---|---|
| Module boundaries | ADR-001 + docs/26 | `scripts/check_architecture.py` + tests |
| PostgreSQL/schema | ADR-002 + Alembic + docs/22 | migration CI + integration tests |
| Authentication | ADR-003 + docs/20 | auth/session security suite |
| Payments | ADR-004 + docs/03 | contract + idempotency + state-machine tests |
| Storage/media | ADR-005 | adapter tests + signed URL tests |
| Jobs/outbox | ADR-006 + docs/24 | retry/idempotency/lease tests |
| Public SEO/rendering | ADR-007 + docs/25 | rendered HTML/metadata/structured-data tests |
| Observability | ADR-008 + docs/07 | health/metrics/log smoke |
| Authorization | ADR-009 + docs/20 | BOLA/cross-account tests |
| Design/a11y | ADR-010 + design-system | visual regression + axe + token contrast |
| Medical content governance | docs/27 + docs/28 | publish policy tests + audit logs |
| Performance | docs/23 | k6/Locust + RUM |
| Agent behavior | AGENTS + docs/15/16 | skill evals + diff/gate evidence |

## Change-trigger matrix

Mudou… → revisar também:

```text
public course schema
  → OpenAPI + frontend types + SEO structured data + course detail UI
payment state
  → docs/03 + DB constraint/state machine + frontend PaymentStatus + tests
role/permission
  → authorization matrix + BOLA tests + audit policy
medical review workflow
  → docs/27/28 + DB + professor/admin UI + publish policy tests
design token
  → token contrast + visual snapshots + MASTER
```

## Release evidence

Uma release importante deve conseguir apontar para:

```text
commit/tag
migration head
CI run
security scan
E2E run
release notes
rollback/roll-forward plan
observability dashboard
```


## Frontend agent/tooling traceability

| Regra | Fonte | Verificação |
|---|---|---|
| Nova página/redesign consulta UI/UX Pro Max sem substituir o Master | `AGENTS.md`, `docs/31-FRONTEND-AGENT-WORKFLOW.md` | `scripts/check-frontend-agent-stack.py --strict` + handoff |
| Novo padrão visual genérico sem equivalente local pesquisa 21st.dev antes de hand-code | `frontend-experience-orchestrator`, `docs/31-FRONTEND-AGENT-WORKFLOW.md` | handoff + UI review |
| Animação não trivial usa motion-experience-orchestrator/Motion MCP e respeita reduced motion | `docs/04-FRONTEND-REACT.md`, `docs/31-FRONTEND-AGENT-WORKFLOW.md` | visual/a11y gate + handoff |
| Implementação React usa arquitetura por feature e skill React quando instalada | `docs/04-FRONTEND-REACT.md`, `AGENTS.md` | lint/typecheck/test/build + skill readiness |
| Agente não pode alegar skill externa ausente | `frontend-experience-orchestrator` | `scripts/validate-agent-config.py` + `check-frontend-agent-stack.py` |

## V4 — Context, ORM and MCP traceability

| Regra | Fonte | Verificação |
|---|---|---|
| Banco oficial é `ICIBINA` / CI `ICIBINA_test` | `DATABASE-CONTRACT`, docs/33/34 | `scripts/check-database-identity.py` |
| Schema muda somente por SQLAlchemy + Alembic | ADR-002, docs/22/34 | migration CI + architecture/code review |
| MCP PostgreSQL é read-only | docs/33 + `.agents/mcp_config.json` + `.codex/config.toml` | `scripts/check-mcp-config.py` + profile runtime check |
| 21st context deriva do Master | `.21st/*` + design-system Master | `scripts/check-21st-design-context.py` |
| Agente inicia por contrato curto | AGENTS + docs/32 + `docs/contracts/*` | `scripts/check-context-routing.py` |
| FastAPI generic skill não decide arquitetura/transação | BACKEND-CONTRACT + backend orchestrator | architecture check + review |
| Repository não esconde commit/rollback | DATABASE/BACKEND contracts | `scripts/check_architecture.py` |
| Clean Code/Software Architect externos não autoativam | docs/12/32/37 + manifest | manifest/installer review |


## V5 — Enforcement additions

| Regra | Fonte | Gate/evidência |
|---|---|---|
| GitHub skills usam commit auditado | docs/40 + external-skills-lock | check-external-skills-lock |
| MCP vê somente agent_inspection | docs/46 | check-mcp-data-boundary |
| Actions externas pinadas por SHA | docs/40 | check-github-actions-pins |
| frontend release scripts obrigatórios | docs/44 | check-release-contracts + release-gates |
| skill usage fica auditável | docs/48 | TASK_EVIDENCE_TEMPLATE + validate-task-evidence |
| segurança CI | docs/41 | security-gates workflow |
| a11y WCAG 2.2 AA | docs/43 | axe/Playwright/manual evidence |


## V5.5 — Experience System traceability

| Regra | Fonte | Gate/evidência |
|---|---|---|
| Toda rota visual usa surface profile | `MASTER.md` + `SURFACES.md` + page override | `check-experience-system.py` + task evidence |
| Student dashboard/player podem usar `Student Immersive` | `SURFACES.md` + page overrides | token contrast + visual regression |
| UI/UX Pro Max é usado em nova página/redesign | `FRONTEND-CONTRACT`, recipes, frontend orchestrator | skill routing evals + task evidence |
| 21st é search/build/review, não autoridade visual | `21ST-WORKFLOW.md`, `.21st/*` | `check-21st-design-context.py` + review evidence |
| Motion Tier 2/3 carrega `/motion` e reduced-motion | `MOTION.md` | routing evals + visual/a11y evidence |
| Student Immersive tokens não divergem do 21st context | `tokens.json` + `.21st/design.json` | `check-design-tokens.py` + `check-21st-design-context.py` |
| UI substancial não fecha sem review visual | `VISUAL-QA.md` + PR/task templates | Playwright/axe/visual evidence |

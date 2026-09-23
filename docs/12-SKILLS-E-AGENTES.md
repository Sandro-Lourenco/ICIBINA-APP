# 12 — Skills e agentes — ICIBINA V5

## Princípio

Skills não são carregadas em bloco. O fluxo é:

```text
AGENTS/rule -> contrato curto -> código real -> orquestrador local -> especialista necessário -> quality gate
```

A lista auditada/pinada está em `external-skills-lock.json`. O racional de seleção está em `docs/42-SKILLS-CATALOG-V5.md`.

## Orquestradores locais

| Skill | Quando entra |
|---|---|
| `frontend-experience-orchestrator` | UI/React/interação/a11y/motion |
| `backend-implementation-orchestrator` | endpoint/use case/FastAPI/auth/backend |
| `database-persistence-orchestrator` | SQLAlchemy/Alembic/repository/query/Postgres |
| `qa-test-orchestrator` | test strategy/coverage/E2E/flaky/regression |
| `security-assurance-orchestrator` | authz/security-sensitive/audit/release |
| `observability-performance-orchestrator` | OTel/metrics/logs/traces/load/capacity |
| `course-platform-architect` | fronteira/ADR/ports/decisão estrutural |
| `asaas-payments` | checkout/webhook/refund/reconciliation |
| `code-quality-orchestrator` | review/refactor/SOLID/smells |
| `platform-quality-gate` | handoff/milestone/release |

## Especialistas e ferramentas sob demanda

- UI/UX Pro Max: nova página/redesign/auditoria UX.
- 21st.dev: search/build/review quando componente local não resolve.
- React: implementação React; docs oficiais da versão prevalecem.
- Motion: animação não trivial passa pelo `motion-experience-orchestrator` local + Motion MCP público; CSS para microinteração simples. O upstream `motiondivision/ai-kit` permanece apenas referência auditável e não é redistribuído.
- Web Accessibility: semântica, teclado/foco/forms/ARIA/a11y audit.
- FastAPI oficial (`fastapi`): mecânica atual de FastAPI/Pydantic/async/OpenAPI. **Não redefine ORM/arquitetura**.
- PostgreSQL Pro / SQL Pro: tuning/EXPLAIN/SQL avançado.
- Test Master: estratégia de testes/coverage/QA ampla.
- Playwright Expert: E2E/visual/flaky browser tests.
- Security Reviewer: auditoria/release/security milestone.
- Grafana skills: OpenTelemetry, Prometheus, Loki, Tempo e k6 somente em observabilidade/performance.

## Manual/review-only

- `clean-code`: auditoria/cleanup grande.
- `software-architect`: ADR/decomposição/consistência/bounded context.
- `fastapi-expert`: fallback/manual; a skill oficial FastAPI é a padrão.

## Supply chain

Skills externas com `redistribution=allowed` são resolvidas pelo commit exato auditado em `external-skills-lock.json` e empacotadas por `scripts/build-agent-cli-bundles.py`. Codex instala o bundle pelo plugin marketplace da CLI; Antigravity 2.0 valida o bundle por `agy plugin install` e ativa a versão final no workspace em `.agents/plugins/icibina-engineering`. **UI/UX Pro Max** segue esse fluxo e usa o bridge portátil `scripts/uiux-pro-max.py`. O repositório upstream **`motiondivision/ai-kit` não é redistribuído**: permanece `reference-only`, `license=NOASSERTION` e `redistribution=blocked` até existir licença verificável no commit pinado. A ICIBINA usa `motion/react`, o `motion-experience-orchestrator` local e o Motion MCP público; Motion+ é opt-in. O `21st` CLI permanece dependência de runtime.

## Readiness

```bash
python scripts/validate-agent-config.py
python scripts/check-external-skills-lock.py
python scripts/check-context-routing.py
python scripts/check-mcp-config.py
python scripts/check-mcp-data-boundary.py
python scripts/check-21st-design-context.py
python scripts/check-frontend-agent-stack.py --strict
```

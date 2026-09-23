# AGENTS.md — ICIBINA V5.8

## Projeto

- Backend: FastAPI + SQLAlchemy 2 async + PostgreSQL 18.
- Frontend: React + TypeScript.
- Banco: `ICIBINA`; CI: `ICIBINA_test`.
- Schema authority: SQLAlchemy typed ORM + Alembic.
- `.agents/skills/`: orquestradores locais curtos + skills externas revisadas/sob demanda.
- `docs/contracts/`: primeiro contexto; não leia `docs/` inteiro.

## Task router

- UI/React/interação -> `$frontend-experience-orchestrator` + `FRONTEND-CONTRACT.md`
- endpoint/use case/FastAPI -> `$backend-implementation-orchestrator` + `BACKEND-CONTRACT.md`
- SQLAlchemy/Alembic/Postgres -> `$database-persistence-orchestrator` + `DATABASE-CONTRACT.md`
- testes/coverage/E2E/flaky -> `$qa-test-orchestrator` + `QA-CONTRACT.md`
- segurança/authz/audit/security milestone -> `$security-assurance-orchestrator` + `SECURITY-CONTRACT.md`
- observabilidade/load/capacity -> `$observability-performance-orchestrator` + `OBSERVABILITY-CONTRACT.md`
- checkout/webhook/refund -> `$asaas-payments`
- fronteira/ADR/ports -> `$course-platform-architect`
- refactor/code review/smells -> `$code-quality-orchestrator`
- handoff/release/milestone -> `$platform-quality-gate`

## Context budget

1. Leia só o contrato curto aplicável.
2. Inspecione código/testes diretamente afetados.
3. Carregue **uma skill externa por necessidade concreta**, não por precaução.
4. Não carregue especialistas redundantes simultaneamente.
5. Documentação longa só entra quando o contrato não resolve a decisão.

## Invariants

- `interface -> application -> domain`; infrastructure implementa ports.
- Domain não importa framework, ORM, HTTP, cache ou transporte.
- SQLAlchemy somente infrastructure; Unit of Work controla commit/rollback.
- Schema muda somente por Alembic; SQL/MCP ad hoc não altera schema.
- MCP PostgreSQL: diagnóstico read-only + least-data (`agent_inspection`).
- Browser nunca decide preço, confirma pagamento ou recebe segredo.
- Role != ownership; teste BOLA em recursos privados.
- I/O em `async def` deve ser async ou explicitamente isolada.
- Webhooks/jobs são idempotentes; dinheiro em centavos inteiros.
- Sem console SQL/shell arbitrário no admin.
- Não reverta mudança desconhecida de outro humano/agente.

## External specialists

- UI/UX Pro Max: nova página, redesign, UX audit.
- 21st.dev: procurar/build/review de componente quando primitivo local não resolve.
- React: código React.
- Motion: animação não trivial -> `$motion-experience-orchestrator`; Motion MCP público é ferramenta, Motion+ é opt-in.
- Web accessibility: interação/semântica/a11y ou audit.
- Playwright Expert: E2E/visual/flaky browser tests.
- Test Master: estratégia QA, coverage, test architecture, load/security test planning.
- Security Reviewer: auditoria/release/security milestone; não para cada feature.
- Grafana/OTel/k6 skills: observabilidade, tracing, métricas e load test.
- Postgres/SQL Pro: tuning/EXPLAIN/SQL complexo; não para CRUD comum.
- Clean Code/Software Architect: somente revisão manual profunda.

## Precedência

Requisito local/segurança/contratos > docs oficiais da versão > skills locais > skills externas. Skill externa nunca redefine arquitetura ICIBINA.

## Evidência

Não declare `PASS` sem execução. Para tarefa substancial registre skills carregadas e gates no formato de `docs/tasks/TASK_EVIDENCE_TEMPLATE.json`. `SKIPPED/PENDING != PASS`.

## Runtime agent readiness

Após instalar/atualizar plugins, valide descoberta real com `python scripts/smoke-agent-skills.py --agent both`. Para milestones importantes use `--all`. Falha ou ausência de autenticação é `PENDING/FAIL`, nunca PASS.


## Experience System V5.8

Frontend visual importante segue `FRONTEND-CONTRACT` -> page override -> `frontend-experience-orchestrator`. Nova página/redesign deve classificar surface profile e usar progressivamente UI/UX Pro Max, 21st.dev e Motion conforme `docs/60-FRONTEND-DESIGN-EXCELLENCE-PIPELINE.md`; não carregar todos os especialistas antecipadamente.

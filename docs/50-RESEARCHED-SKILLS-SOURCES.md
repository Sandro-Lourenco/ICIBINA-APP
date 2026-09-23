# 50 — Skills pesquisadas e selecionadas

Seleção feita para maximizar especialização sem inflar contexto. O commit efetivamente revisado fica em `external-skills-lock.json`.

## Frontend

- **UI/UX Pro Max** — `nextlevelbuilder/ui-ux-pro-max-skill`: design intelligence, design-system generation, React/Tailwind/shadcn guidance. Skill pinada por commit e empacotada nos plugins nativos de Codex/Antigravity.
- **21st.dev** — `21st-dev/skill`: CLI/search/build/review de componentes. Skills pinadas por commit; CLI pinado.
- **React** — `Spardutti/claude-skills`: padrões modernos React. Docs oficiais React prevalecem em comportamento version-sensitive.
- **Motion AI Kit** — `motiondivision/ai-kit`: commit mantido como referência auditável. Na V5.8 o repositório não apresenta licença verificável no commit pinado, portanto a skill upstream fica `NOASSERTION` e não é redistribuída; a execução usa orquestrador Motion local + Motion MCP público, com Motion+ opt-in.
- **Web Accessibility** — `agents-inc/skills`: WCAG 2.2 AA, semantic HTML, focus, keyboard, ARIA e reduced motion.

## Backend / database

- **FastAPI oficial** — skill do próprio repositório `fastapi/fastapi`; usada para mecânica atual de framework. A preferência genérica por SQLModel não substitui a decisão ICIBINA por SQLAlchemy 2/Alembic.
- **PostgreSQL Pro / SQL Pro** — `Jeffallan/claude-skills`: tuning, EXPLAIN, indexes e SQL complexo; não entram em CRUD normal.

## QA / segurança

- **Test Master** — estratégia de testes, coverage, regression e test architecture.
- **Playwright Expert** — E2E, visual regression e flaky browser tests.
- **Security Reviewer** — auditoria, SAST/secrets/dependencies e review manual; somente em milestone/release/audit.

## Observabilidade/performance

- **Grafana official skills** — `grafana/skills`: OpenTelemetry, Prometheus, Loki, Tempo e k6. A escolha oficial do ecossistema reduz risco de guidance genérico desatualizado.

## Skills deliberadamente fora do caminho normal

- `clean-code`: útil, porém ampla; manual review only.
- `software-architect`: útil, porém pesada; somente decisões arquiteturais profundas.
- `fastapi-expert` genérica: fallback manual; a skill oficial FastAPI é preferida.

## Política

“Mais skills” não significa “mais qualidade”. Skills são instaladas pelos CLIs nativos de Codex/Antigravity para descoberta, mas orquestradores locais limitam ativação. Upgrades exigem revisão de diff e atualização do lock.


## V5.5 visual stack usage

A integração frontend usa recursos observados nas skills pinadas e auditadas:

- UI/UX Pro Max: design-system mode, domains, stack guidance e variance/motion/density dials;
- 21st.dev: design context, search, explore, build e review;
- Motion: `motion/react` + orquestrador local + Motion MCP público; Motion+ adiciona tooling premium somente quando habilitado/autenticado.

Esses recursos são roteados sob demanda pelo `frontend-experience-orchestrator`; a documentação local prevalece sobre recomendações genéricas.

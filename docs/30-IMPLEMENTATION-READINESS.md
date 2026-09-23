# 30 — Implementation Readiness — V5

Este pacote é um engineering blueprint executável; a aplicação real ainda precisa ser implementada/migrada.

## Blueprint ready

- banco `ICIBINA` / `ICIBINA_test`;
- SQLAlchemy 2 async + asyncpg + Alembic como autoridade de schema;
- PostgreSQL MCP pinado, read-only e least-data via `agent_inspection`;
- contratos curtos e progressive disclosure;
- orquestradores de frontend, backend, database, QA, security, observability, arquitetura, pagamentos, code-quality e handoff;
- skills externas GitHub pinadas por commit e licença registrada;
- UI/UX Pro Max, Motion e 21st versionados;
- design system médico + `.21st` derivado;
- ASVS/security, accessibility, performance/capacity, resilience, SEO e medical governance;
- CI blueprint, security gates, release gates e actions pinadas por SHA;
- skill-routing fixtures e task evidence contract.

## Ainda depende do ambiente/código real

- instalar skills externas pinadas e confirmar Motion MCP;
- criar profile `icibina-readonly` no keyring;
- criar as views sanitizadas `agent_inspection` depois do schema real;
- implementar backend/frontend e migrations;
- gerar lockfiles reais da aplicação;
- coverage, visual baselines, RUM/load benchmarks;
- restore drill, pentest e ASVS evidenciado;
- executar eval harness real contra Codex/Antigravity e medir ativações.

## Preflight blueprint

```bash
python scripts/validate-blueprint.py
python scripts/validate-agent-config.py
python scripts/check-context-routing.py
python scripts/check-skill-policy.py
python scripts/check-external-skills-lock.py
python scripts/check-database-identity.py
python scripts/check-mcp-config.py
python scripts/check-mcp-data-boundary.py
python scripts/check-21st-design-context.py
python scripts/check-design-tokens.py
python scripts/check-github-actions-pins.py
python scripts/check-release-contracts.py
python scripts/validate-skill-evals.py
python scripts/validate-doc-links.py
```

## Depois de instalar skills

```bash
python scripts/validate-agent-config.py --require-external
python scripts/check-frontend-agent-stack.py --strict
```

## Quando o código real existir

Os mesmos checks passam a exigir Alembic, lockfiles, scripts de release, architecture fitness functions, tests, coverage e security/release workflows. `SKIPPED/PENDING` não deve ser promovido a `PASS`.

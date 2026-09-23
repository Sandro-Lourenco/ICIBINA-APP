# Catálogo de skills V5 — seleção sênior

Critério: complementar a arquitetura ICIBINA sem criar context bloat.

## Caminho normal

| Skill | Quando entra | Não usar para |
|---|---|---|
| UI/UX Pro Max | nova página, redesign, UX audit | padding trivial |
| React | escrever/alterar React | backend |
| 21st CLI/build/review | falta primitivo local, build/review UI | substituir design system |
| Motion | animação não trivial | hover/fade simples CSS |
| web-accessibility | semântica, forms, keyboard, focus, a11y audit | mudança sem impacto UI |
| FastAPI official (`fastapi`) | mecânica FastAPI/Pydantic/async e detalhes atuais | definir arquitetura/transação/ORM |
| Postgres Pro | EXPLAIN/index/maintenance | CRUD comum |
| SQL Pro | SQL complexo/tuning | repository simples ORM |
| Test Master | estratégia QA ampla/coverage/load/security testing | cada unit test |
| Playwright Expert | E2E/visual/flaky browser | unit tests |
| Security Reviewer | auditoria/milestone/release | toda feature |
| Grafana OTel/Prometheus/Loki/Tempo | observabilidade específica | lógica de negócio |
| k6 | load/perf test | unit/integration |

## Manual only

`clean-code` e `software-architect` continuam disponíveis apenas em revisão profunda/decisão arquitetural. Eles são grandes e não pertencem ao caminho crítico.

## Por que não instalar “tudo”

Skills têm custo de descoberta e, quando ativadas, custo de contexto. O objetivo é **especialista certo no momento certo**, não maior catálogo possível.


## Skill FastAPI oficial
A V5 prefere a skill mantida no repositório oficial `fastapi/fastapi` para mecânica/version-sensitive. A recomendação genérica dela por SQLModel é explicitamente sobreposta pela arquitetura ICIBINA, que padroniza SQLAlchemy 2 + Alembic. `fastapi-expert` permanece manual/fallback, não default.

## Instalação

A descoberta final é nativa do host: Codex recebe `icibina-engineering` pelo marketplace/plugin da Codex CLI; Antigravity 2.0/CLI valida o bundle por `agy plugin install`, remove a cópia global de validação e usa o plugin final project-scoped em `.agents/plugins/icibina-engineering`. Consulte `docs/51-CLI-NATIVE-SKILL-INSTALLATION.md`.

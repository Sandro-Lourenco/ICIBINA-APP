# 32 — Context Engineering e Skill Routing — V5

## Modelo

```text
task
 -> AGENTS (router)
 -> 1 contrato curto
 -> código/testes afetados
 -> 1 orquestrador local
 -> 0–1 especialista por necessidade concreta
 -> especialistas adicionais somente se cross-cutting e justificados
 -> quality gate no handoff
```

## Budget operacional

- não carregar docs longos antes de inspecionar código;
- task local: normalmente 1 orquestrador + 0–1 external specialist;
- task cross-cutting: no máximo os especialistas necessários por subproblema;
- `platform-quality-gate` entra no final;
- `clean-code`, `software-architect` e `fastapi-expert` genérico são manual-only.

## Roteamento

- frontend orchestrator: React/UIUX/21st/Motion/accessibility;
- backend orchestrator: skill oficial `fastapi` para mecânica atual; arquitetura local prevalece;
- database orchestrator: ORM/Alembic e, só em tuning, Postgres/SQL specialists;
- QA orchestrator: Test Master/Playwright;
- security orchestrator: Security Reviewer em auditoria/milestone;
- observability orchestrator: OTel/Prometheus/Loki/Tempo/k6;
- course-platform-architect: fronteiras/ADR;
- code-quality: review/refactor;
- quality gate: evidence aggregation.

## Regra de contexto

Não carregue especialista porque “pode ajudar”. Carregue porque uma decisão concreta exige o conhecimento daquela skill. Registre no evidence file as skills realmente carregadas.

## Evals

`evals/skill-routing.jsonl` contém required/optional/forbidden. `docs/48-AGENT-EVAL-HARNESS.md` define como transformar fixtures em regressão real contra modelos/agentes.

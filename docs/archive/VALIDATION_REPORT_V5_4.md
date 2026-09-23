# Validation Report — ICIBINA V5.4

Data da validação: **2026-09-23**.

## Resultado

A V5.4 fecha os 12 pontos levantados na auditoria da V5.3. O pacote permanece em **blueprint mode**: não declara como PASS aquilo que depende do backend/frontend reais, dos CLIs autenticados ou de medições de capacidade ainda inexistentes.

## Fechamento dos 12 pontos

| # | Ponto | Estado V5.4 | Evidência principal |
|---|---|---|---|
| 1 | Roadmap duplicado | PASS | `Fase 0.5` ocorre exatamente uma vez; `check-canonical-invariants.py` fiscaliza |
| 2 | Drift 5.2/5.3 em plugins | PASS | bundles `5.4.0`; smoke markers `V5_4` |
| 3 | Imagens mutáveis em release | PASS | `release-images-lock.json`; workflow usa `@sha256`; `check-release-image-lock.py` |
| 4 | Owner divergente do schema MCP | PASS | `agent_inspection AUTHORIZATION icibina_migrator` em bootstrap e referência operacional |
| 5 | Cache ativo Codex fora do integrity check | PASS | `check-installed-skills-integrity.py` cobre `~/.codex/plugins/cache/.../local/skills` e plugin Antigravity ativo |
| 6 | Skill React baseada em 19.2 | PASS documental | `docs/59-REACT-19.3-DELTA.md`; docs oficiais React prevalecem em comportamento version-sensitive |
| 7 | Smoke externo frágil | PASS | respostas externas em JSON semântico/tolerante, sem depender de string exata |
| 8 | Link validator parcial | PASS | `validate-doc-links.py` percorre recursivamente todo Markdown; 127 arquivos validados |
| 9 | Capacity Model `TBD` | PASS de governança / PENDING de evidência | `capacity-baseline.json` substitui TBD; status `unverified`; strict gate falha até medição real |
| 10 | Compliance médico Brasil | PASS documental | `docs/56-BRASIL-COMPLIANCE-MEDICAL-CONTENT.md` com LGPD/ANPD/CFM |
| 11 | Dados identificáveis de pacientes | PASS documental | `docs/57...`, `PatientDataWarning`, erro estável e controles backend/moderação |
| 12 | MinIO/local images envelhecendo | PASS de governança | `development-images-lock.json`, revisão a cada 90 dias, upstream MinIO arquivado registrado |

## Gates executados nesta sessão

- `validate-blueprint.py`: PASS — 80 arquivos críticos V5.4.
- `validate-agent-config.py`: PASS local; 19 skills externas corretamente `EXTERNAL-MISSING` antes da instalação.
- `validate-doc-links.py`: PASS — 127 Markdown recursivos.
- contraste light + dark: PASS; dark focus/surface **6.27:1**, border/surface **3.36:1**.
- identidade PostgreSQL: PASS — `ICIBINA` / `ICIBINA_test`.
- MCP config/profile isolation/least-data: PASS.
- 21st design context: PASS.
- context routing: PASS — 7 contratos.
- skill-routing eval definitions: PASS — 16 fixtures / 32 skills conhecidas.
- external skills lock: PASS.
- GitHub Actions pinning: PASS.
- toolchain pinning: PASS.
- release contracts: PASS em blueprint mode.
- database role bootstrap: PASS.
- release image lock: PASS.
- development image review `--strict`: PASS.
- JSON/YAML parse: PASS.
- Python compile + shell syntax: PASS.

## Estados intencionalmente PENDING

1. `capacity-baseline.json` = `unverified`: só muda depois de k6/DB/observability evidence reproduzível.
2. plugins/skills externos: precisam ser instalados no computador com Codex/Antigravity autenticados.
3. smoke runtime de Codex/Antigravity: não executável neste container porque `codex`/`agy` não estão presentes.
4. `backend/src`, migrations e `uv.lock`: ainda não existem no blueprint.
5. frontend real e `package-lock.json`: ainda não existem no blueprint.
6. OpenAPI real: `contracts/openapi/baseline.json` é placeholder explícito; release falha quando backend existir até uma baseline real ser revisada.
7. manifests de produção: o digest gate entra em vigor quando existirem.

## Supply chain revisada

- PostgreSQL release: `postgres@sha256:86c951e05bf56c93d95d397747fb8820ac76cc3bedb78f43abd83eedbe3666ae`.
- oasdiff release: `tufin/oasdiff@sha256:c1200e64fa9b2229b7aee39fe389bd5b49c7cb955923f8a6b20791a6dcf1deed`, ligado à baseline verificada `v1.30.0`. Upgrade exige resolver e revisar o digest exato da versão-alvo.
- imagens locais: governadas separadamente por `development-images-lock.json`; nunca contam como evidência de produção.

## Conclusão

A V5.4 trata regra escrita como insuficiente sem fonte canônica e, quando possível em blueprint mode, um validator/gate correspondente. O produto ainda não é “10/10” até código, testes, carga, pentest, restore drills e produção existirem; a documentação, porém, fecha os 12 drifts identificados sem inventar evidência ausente.

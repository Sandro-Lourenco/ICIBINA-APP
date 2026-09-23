# Validation Report — ICIBINA V5.8

**Release:** Documentation Consistency Hardening  
**Scope:** correções objetivas encontradas na auditoria geral da V5.7.  
**Architecture impact:** none. V5.8 não altera stack, boundaries, Experience System, banco ou políticas funcionais.

## 1. Correções aplicadas

### Motion upstream / supply chain

- `docs/12-SKILLS-E-AGENTES.md` e `docs/14-INTEGRACAO-BACKEND-FRONTEND.md` não afirmam mais que `motiondivision/ai-kit` é empacotado.
- O upstream permanece `reference-only`, `license=NOASSERTION`, `redistribution=blocked`.
- O caminho operacional continua: `motion/react` + `motion-experience-orchestrator` local + Motion MCP público; Motion+ é opt-in.

### SMOKE_MARKER / release consistency

- Todos os 11 skills locais possuem exatamente um `SMOKE_MARKER` com sufixo `V5_8`.
- `smoke-agent-skills.py --all` descobre dinamicamente todos os `.agents/skills/*/SKILL.md`; não existe mais lista local incompleta hardcoded.
- `scripts/check-release-version-consistency.py` falha em marker ausente, duplicado ou de release antiga.

### Frontend legacy dependency pointer

- `frontend/package-target.legacy.json` não referencia mais o inexistente `dependency-policy.json`.
- O aviso deprecated aponta para fontes reais: `toolchain-lock.json`, `supply-chain-policy.json` e `docs/40-SUPPLY-CHAIN-AND-LOCKFILES.md`.

### Release metadata

- README, AGENTS, bootstrap, `architecture-invariants.json`, bundle builder e fontes visuais correntes identificam V5.8.
- Bundle/plugin version e `bundle_version` usam `5.8.0`.
- V5.7 changelog/report foram arquivados em `docs/archive/`.

## 2. Novo gate de regressão

`scripts/check-release-version-consistency.py` verifica:

1. `architecture-invariants.json.blueprint_version == 5.8.0`;
2. bundle builder gera apenas `5.8.0`;
3. todo skill local possui marker único `*_V5_8`;
4. smoke harness descobre todas as skills locais dinamicamente;
5. claims antigos de redistribuição Motion não reaparecem;
6. target frontend legacy só aponta para políticas existentes;
7. changelog e validation report da release corrente existem.

O gate roda em `quality-gates.yml` e `release-gates.yml`.

## 3. Resultados executados

```text
validate-blueprint                  PASS — 96 arquivos críticos V5.8
validate-agent-config               PASS — 11 locais / 18 externos PENDING esperados
validate-doc-links                  PASS — 147 Markdown recursivos
canonical invariants                PASS
release version consistency         PASS — 11 skills locais / V5.8
database role bootstrap             PASS
design token contrast               PASS — light + dark + studentImmersive
experience system                   PASS — 4 profiles
UI/UX Pro Max bridge                PASS
shadcn bootstrap contract           PASS — blueprint mode
database identity                   PASS — ICIBINA / ICIBINA_test
MCP configuration                   PASS
MCP least-data                      PASS
PostgreSQL MCP profile isolation    PASS
21st design context                 PASS
context routing                     PASS — 7 contracts / 0 warnings
skill routing evals                 PASS — 19 fixtures / 33 known skills
skill policy                        PASS
backend architecture                PASS — blueprint mode
frontend architecture               PASS — blueprint mode
external skills lock                PASS
github actions pins                 PASS
toolchain pins                      PASS
release contracts                   PASS
reproducible release                BLUEPRINT PASS / runtime locks PENDING
release image lock                  PASS
development image review            PASS
agent CLI bundles                   BLUEPRINT PASS / runtime build PENDING
installed skills integrity          PENDING — bundles ainda não construídos
frontend agent stack                BLUEPRINT READY / CLI install PENDING
JSON parse                          PASS — 17 arquivos
YAML parse                          PASS — 4 arquivos
Python compile                      PASS
Shell syntax                        PASS
```

## 4. Estados que permanecem corretamente PENDING

- Codex/Antigravity runtime installation and authentication;
- external reviewed skill runtime installation;
- plugin bundle build/activation;
- frontend real `package.json`, `package-lock.json`, `components.json`;
- backend real `pyproject.toml`, `uv.lock`, migrations e OpenAPI;
- capacity/load evidence;
- production manifests and runtime evidence.

`PENDING` não é tratado como `PASS`.

## 5. Parecer

**GO para implementação.** Os quatro drifts objetivos da auditoria V5.7 foram corrigidos e transformados em regressions gates. V5.8 é um hardening de consistência; não introduz nova arquitetura.

# ICIBINA V5.2 — Validation Report

## Resultado

A V5.2 passou em todos os **gates estáticos do blueprint** executáveis neste ambiente. Os únicos estados `PENDING` são deliberados e dependem de recursos que não existem dentro do blueprint: CLIs Codex/Antigravity autenticados, frontend/backend reais e manifests de produção reais.

## PASS

- blueprint critical files: **66 arquivos V5.2 presentes**;
- local skills: **10**, sem erros/warnings;
- context routing: **7 contratos curtos**, sem warnings;
- skill routing fixtures: **16**;
- external skills lock: commit-pin válido;
- PostgreSQL identity: `ICIBINA` / `ICIBINA_test`;
- PostgreSQL MCP: pacote pinado, Codex + Antigravity configs válidas;
- MCP privacy boundary: somente `agent_inspection`;
- 21st design context: sincronizado com o design system;
- design-token contrast: todos os pares críticos passaram;
- GitHub Actions: referências por SHA imutável;
- reviewed toolchain pins: Node `24.21.0`, Python `3.13.15`, uv `0.12.17`;
- release contract checker: válido em blueprint mode;
- docs links: válidos;
- JSON/YAML: parse válido;
- Python scripts: compilam;
- shell scripts: sintaxe válida;
- stale-instruction scan: sem `|| true`, silent Codex marketplace catches ou caminho Antigravity global permanente.

## Hardening V5.2 comprovado estaticamente

### Antigravity project scope

O plugin ICIBINA final é ativado em:

```text
.agents/plugins/icibina-engineering
```

`agy plugin install` é usado apenas com uma cópia temporária de validação. Essa cópia é removida antes da ativação final do workspace.

### Codex fail-closed

`scripts/configure-codex-marketplace.py` decide `add` versus `upgrade` e falha imediatamente quando a CLI retorna erro ou o marketplace não aparece após a operação. Não há `|| true`/catch silencioso.

### Runtime skill smoke harness

`scripts/smoke-agent-skills.py` usa:

- `codex exec --json`;
- `agy -p ... --output-format json`.

Os markers de diagnóstico existem somente dentro dos orquestradores locais, permitindo testar discovery real depois da instalação.

### Reproducible release

`scripts/check-reproducible-release.py` exige quando o código real existir:

- `backend/uv.lock` + `.python-version`;
- `frontend/package-lock.json`;
- ausência de `latest`/`*` no package real;
- imagens de produção por digest `@sha256:`.

## PENDING legítimo

- 19 skills externas ainda não materializadas: serão baixadas dos commits auditados pelos instaladores no computador alvo;
- Codex plugin bundle ainda não construído/registrado neste ambiente;
- Antigravity workspace plugin ainda não construído/validado neste ambiente;
- runtime smoke tests não foram executados porque `codex` e `agy` não estão instalados/autenticados neste container;
- frontend real ausente: lock/release gates de npm aguardam implementação;
- backend real ausente: `uv.lock`, Alembic e architecture fitness em código aguardam implementação;
- deploy de produção ausente: digest pinning de imagens aguarda manifests reais.

Esses estados **não são tratados como PASS**.

## Inventário

Arquivos no pacote antes da compactação: **205**.

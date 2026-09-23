# Runtime skill smoke tests

## Objetivo

Existência de `SKILL.md` não prova que o host realmente descobriu a skill. A V5.8 mantém o smoke test real nos modos não interativos dos dois agentes e exige marker de release em todos os skills locais.

## Codex

O harness usa `codex exec --json`. No modo padrão valida o primeiro skill local; com `--all`, descobre automaticamente todos os `.agents/skills/*/SKILL.md` e valida o `SMOKE_MARKER` de cada um.

## Antigravity

O harness usa `agy -p ... --output-format json` no workspace e aplica o mesmo conjunto descoberto de skills/markers.

## Comandos

```bash
python scripts/smoke-agent-skills.py --agent codex
python scripts/smoke-agent-skills.py --agent antigravity
python scripts/smoke-agent-skills.py --agent both --all
```

Esses testes requerem autenticação local dos CLIs e podem consumir uso do modelo. Eles não devem ser mascarados como `PASS` em ambientes onde os CLIs não estão autenticados.

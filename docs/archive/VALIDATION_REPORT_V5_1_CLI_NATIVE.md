# ICIBINA V5.1 CLI-native — Validation Report

Generated from the packaged blueprint before machine-specific CLI installation.

## Static blueprint status

- blueprint structure: PASS
- local ICIBINA orchestrator skills/frontmatter: PASS
- context routing/contracts: PASS
- skill policy: PASS
- external skill lock uses exact reviewed commits: PASS
- UI/UX Pro Max source pin: PASS
- Motion `/motion` source pin: PASS
- Codex repo marketplace definition: PASS
- Codex project plugin enablement definition: PASS
- Antigravity native plugin build/install scripts: PASS
- CLI plugin bundle builder: PASS (network fetch happens only during local install)
- plugin bundle runtime build: PENDING until installer runs on the user machine
- PostgreSQL MCP config pin: PASS
- PostgreSQL MCP least-data boundary: PASS
- Motion MCP host schemas documented for both agents: PASS
- 21st design context: PASS
- design token contrast: PASS
- GitHub Actions SHA pinning: PASS
- release contract checker: PASS in blueprint mode
- skill routing fixtures: PASS
- architecture code checks: PENDING because `backend/src` is not implemented yet

## Canonical installation path

```text
reviewed Git commits
        ↓
build-agent-cli-bundles.py
        ↓
Codex CLI plugin marketplace    Antigravity CLI plugin
        ↓                                ↓
Codex skill discovery            agy plugin install
```

`npx skills`, `uipro init`, and `npx motion-ai` are not the canonical ICIBINA skill installation path.

The `21st` CLI remains a runtime dependency for 21st skills. PostgreSQL credentials/profile remain machine-local.

## Runtime checks after extraction

```powershell
.\scripts\install-skills-codex.ps1
.\scripts\install-skills-antigravity.ps1
python scripts\check-agent-cli-bundles.py --runtime
python scripts\check-frontend-agent-stack.py --strict
```

Inside Antigravity CLI also inspect `/skills` and `/mcp`.

`PENDING` is deliberately not reported as `PASS`.

## Executed static validation summary

Validated in the packaged blueprint environment:

- `validate-blueprint.py`: PASS (55 required files)
- `validate-agent-config.py`: PASS for 10 local skills; 19 external skills correctly PENDING until CLI install
- context routing: PASS
- skill policy: PASS
- external lock refs: PASS
- database identity: PASS
- PostgreSQL MCP config/data boundary: PASS
- 21st design context: PASS
- design-token contrast: PASS
- GitHub Actions SHA pins: PASS
- release contracts: PASS in blueprint mode
- skill-routing fixtures: PASS (16 fixtures)
- Codex/Antigravity CLI bundle definitions: PASS; generated bundles PENDING runtime install
- documentation links: PASS (96 Markdown files)
- JSON parse: PASS
- GitHub Actions YAML parse: PASS
- Python compilation: PASS
- shell syntax: PASS

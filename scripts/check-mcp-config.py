#!/usr/bin/env python3
from __future__ import annotations
import json,sys,tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; errors=[]
for p in [ROOT/'.agents/mcp_config.json',ROOT/'.codex/config.toml']:
 if not p.exists(): errors.append(f'missing {p.relative_to(ROOT)}')
if (ROOT/'.agents/mcp_config.json').exists():
 d=json.loads((ROOT/'.agents/mcp_config.json').read_text()); s=(d.get('mcpServers') or {}).get('icibina-postgres')
 if not s: errors.append('Antigravity icibina-postgres missing')
 elif s.get('command')!='python' or 'scripts/postgres-mcp-wrapper.py' not in (s.get('args') or []): errors.append('Antigravity MCP must use project-isolated wrapper')
if (ROOT/'.codex/config.toml').exists():
 d=tomllib.loads((ROOT/'.codex/config.toml').read_text()); s=(d.get('mcp_servers') or {}).get('icibina-postgres')
 if not s: errors.append('Codex icibina-postgres missing')
 elif s.get('command')!='python' or 'scripts/postgres-mcp-wrapper.py' not in (s.get('args') or []): errors.append('Codex MCP must use project-isolated wrapper')
wrapper=(ROOT/'scripts/postgres-mcp-wrapper.py').read_text() if (ROOT/'scripts/postgres-mcp-wrapper.py').exists() else ''
for token in ['@microsoft/postgres-mcp@0.1.0-rc.10',"'.icibina' / 'mcp-home'"]:
 if token not in wrapper: errors.append('wrapper missing '+token)
if errors:
 for e in errors: print('ERROR:',e)
 raise SystemExit(1)
print('mcp-config-check: OK (pinned + project-isolated profile store)')

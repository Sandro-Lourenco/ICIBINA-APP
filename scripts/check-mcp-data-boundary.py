#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
t=(ROOT/'database/003_mcp_readonly_role.sql').read_text(encoding='utf-8').lower()
errors=[]
for cfg in [ROOT/'.agents/mcp_config.json', ROOT/'.codex/config.toml']:
 txt=cfg.read_text(encoding='utf-8')
 if 'scripts/postgres-mcp-wrapper.py' not in txt: errors.append('MCP config bypasses isolated wrapper: '+str(cfg.relative_to(ROOT)))
required=['agent_inspection','default_transaction_read_only','revoke all on schema public','grant usage on schema agent_inspection']
for x in required:
 if x not in t: errors.append('missing: '+x)
for bad in ['grant select on all tables in schema public','grant select on all sequences in schema public']:
 if bad in t: errors.append('least-data violation: '+bad)
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('mcp-data-boundary-check: OK (agent_inspection only)')

#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('--runtime',action='store_true'); args=parser.parse_args()
errors=[]
wrapper=(ROOT/'scripts/postgres-mcp-wrapper.py').read_text(encoding='utf-8')
for token in ["'.icibina' / 'mcp-home'", "env['HOME']", "env['USERPROFILE']", '@microsoft/postgres-mcp@0.1.0-rc.10']:
    if token not in wrapper: errors.append('wrapper missing isolation token: '+token)
for p in [ROOT/'.agents/mcp_config.json',ROOT/'.codex/config.toml']:
    txt=p.read_text(encoding='utf-8')
    if 'scripts/postgres-mcp-wrapper.py' not in txt: errors.append(f'{p.relative_to(ROOT)} bypasses isolated wrapper')
if args.runtime:
    cfg=ROOT/'.icibina/mcp-home/.postgres-mcp/connections.yaml'
    if not cfg.exists(): errors.append('isolated connections.yaml not found; run setup-postgres-mcp first')
    else:
        txt=cfg.read_text(encoding='utf-8')
        # Profile names in current postgres-mcp YAML appear as id/name-like scalar values.
        candidates=set(re.findall(r'(?mi)^\s*(?:id|name|profileId)\s*:\s*["\']?([A-Za-z0-9_-]+)',txt))
        candidates={x for x in candidates if x not in {'ro','rw'}}
        extras={x for x in candidates if x!='icibina-readonly'}
        if extras: errors.append('unexpected profiles in isolated store: '+', '.join(sorted(extras)))
        if 'icibina-readonly' not in txt: errors.append('icibina-readonly absent from isolated store')
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('postgres-mcp-profile-isolation: OK'+(' (runtime)' if args.runtime else ''))

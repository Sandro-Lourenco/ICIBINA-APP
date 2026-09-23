#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
lock=json.loads((ROOT/'toolchain-lock.json').read_text(encoding='utf-8'))
errors=[]
required=['node','python','uv','postgres_mcp','21st_cli','shadcn_cli']
for k in required:
    v=str(lock.get(k,''))
    if not v or any(x in v.lower() for x in ('latest','main','master','*')):
        errors.append(f'toolchain-lock {k} is not exact: {v!r}')

# Workflow runtime versions must match reviewed toolchain when explicitly set.
for p in (ROOT/'.github/workflows').glob('*.yml'):
    txt=p.read_text(encoding='utf-8')
    for v in re.findall(r"python-version:\s*['\"]([^'\"]+)",txt):
        if v != lock['python']: errors.append(f'{p.name}: python-version {v} != {lock["python"]}')
    for v in re.findall(r"node-version:\s*['\"]([^'\"]+)",txt):
        if v != lock['node']: errors.append(f'{p.name}: node-version {v} != {lock["node"]}')
    for v in re.findall(r'uv==([0-9][0-9A-Za-z.\-]+)',txt):
        if v != lock['uv']: errors.append(f'{p.name}: uv {v} != {lock["uv"]}')
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('toolchain-pin-check: OK')

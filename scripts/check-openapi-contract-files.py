#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
backend=ROOT/'backend'
if not (backend/'pyproject.toml').exists():
 print('openapi-contract-files: BLUEPRINT (backend not implemented)'); raise SystemExit(0)
required=[backend/'scripts/export_openapi.py',backend/'openapi.json',ROOT/'contracts/openapi/baseline.json']
missing=[str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
 for p in missing: print('ERROR: missing',p)
 raise SystemExit(1)
baseline=json.loads((ROOT/'contracts/openapi/baseline.json').read_text(encoding='utf-8'))
if baseline.get('x-icibina-placeholder') is True:
 print('ERROR: OpenAPI baseline is still the blueprint placeholder; establish a reviewed real baseline before release')
 raise SystemExit(1)
print('openapi-contract-files: OK')

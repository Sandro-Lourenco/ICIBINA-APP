#!/usr/bin/env python3
from pathlib import Path
import json,sys,re
ROOT=Path(__file__).resolve().parents[1]; errors=[]; backend=ROOT/'backend'; frontend=ROOT/'frontend'
if (backend/'pyproject.toml').exists():
 for p in [backend/'alembic.ini',backend/'uv.lock',ROOT/'.python-version',backend/'scripts/export_openapi.py',ROOT/'contracts/openapi/baseline.json']:
  if not p.exists(): errors.append('backend release requirement missing: '+str(p.relative_to(ROOT)))
 py=(backend/'pyproject.toml').read_text(encoding='utf-8')
 for marker in ['authz','payments_security']:
  if marker not in py: errors.append('pytest release marker not declared in backend/pyproject.toml: '+marker)
if (frontend/'package.json').exists():
 if not (frontend/'package-lock.json').exists(): errors.append('frontend/package-lock.json missing')
 data=json.loads((frontend/'package.json').read_text()); scripts=data.get('scripts',{})
 for s in ['lint','typecheck','test','build','test:e2e','test:a11y','test:visual','check:bundle']:
  if s not in scripts: errors.append('frontend required release script missing: '+s)
 for group in ['dependencies','devDependencies']:
  for name,v in data.get(group,{}).items():
   if str(v).strip() in ['', '*', 'latest']: errors.append(f'unpinned dependency: {group}.{name}={v}')
if errors:
 for e in errors: print('ERROR:',e)
 raise SystemExit(1)
print('release-contracts-check: OK (or blueprint mode)')

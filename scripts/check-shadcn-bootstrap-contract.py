#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
lock=json.loads((ROOT/'toolchain-lock.json').read_text(encoding='utf-8'))
if lock.get('shadcn_cli')!='4.21.0': errors.append('toolchain-lock shadcn_cli must be reviewed exact version 4.21.0')
for p in ['docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md','design-system/integrative-medicine/21ST-WORKFLOW.md','docs/contracts/FRONTEND-CONTRACT.md']:
 t=(ROOT/p).read_text(encoding='utf-8')
 if 'shadcn' not in t.lower(): errors.append(f'{p}: shadcn bootstrap/intake contract missing')
real_pkg=ROOT/'frontend/package.json'
if real_pkg.exists():
 comp=ROOT/'frontend/components.json'
 if not comp.exists(): errors.append('real frontend exists but frontend/components.json is missing')
 else:
  try: d=json.loads(comp.read_text(encoding='utf-8'))
  except Exception as e: errors.append(f'frontend/components.json invalid JSON: {e}'); d={}
  if d.get('rsc') is not False: errors.append('frontend/components.json must set rsc=false for Vite SPA baseline')
  if d.get('tsx') is not True: errors.append('frontend/components.json must set tsx=true')
  aliases=d.get('aliases',{})
  for k in ['components','ui','lib','hooks','utils']:
   if not aliases.get(k): errors.append(f'frontend/components.json missing alias {k}')
if errors:
 [print('ERROR:',e) for e in errors]; raise SystemExit(1)
print('shadcn-bootstrap-check: OK' + (' — real frontend contract verified' if real_pkg.exists() else ' — blueprint mode'))

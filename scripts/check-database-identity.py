#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
expected={
 'config/.env.example':'/ICIBINA',
 'docker-compose.target.yml':'POSTGRES_DB: ICIBINA',
 '.github/workflows/quality-gates.yml':'POSTGRES_DB: ICIBINA_test',
}
for rel,needle in expected.items():
 p=ROOT/rel
 if not p.exists() or needle not in p.read_text(encoding='utf-8'):
  errors.append(f'{rel} missing expected {needle!r}')
for p in ROOT.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['.git','node_modules']): continue
 try: t=p.read_text(encoding='utf-8')
 except Exception: continue
 if re.search(r'\bcourse_platform\b|\bapp_test\b',t,re.I):
  errors.append(f'legacy DB name remains in {p.relative_to(ROOT)}')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('database-identity-check: OK (ICIBINA / ICIBINA_test)')

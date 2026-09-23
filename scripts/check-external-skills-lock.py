#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
lockp=ROOT/'external-skills-lock.json'
if not lockp.exists(): errors.append('missing external-skills-lock.json')
else:
 data=json.loads(lockp.read_text(encoding='utf-8'))
 names=set()
 for x in data.get('sources',[]):
  for k in ['name','repo','ref','source_path','target_name','mode','license']:
   if not x.get(k): errors.append(f"{x.get('name','?')}: missing {k}")
  if not re.fullmatch(r'[0-9a-f]{40}',x.get('ref','')): errors.append(f"{x.get('name')}: ref must be exact 40-char commit")
  if x.get('target_name') in names: errors.append(f"duplicate target_name: {x.get('target_name')}")
  names.add(x.get('target_name'))
  if x.get('license')=='NOASSERTION':
   if x.get('redistribution')!='blocked': errors.append(f"{x.get('name')}: NOASSERTION requires redistribution=blocked")
   if not x.get('license_status'): errors.append(f"{x.get('name')}: NOASSERTION requires license_status")
  if x.get('redistribution')=='blocked' and x.get('mode') not in ('reference-only','manual'):
   errors.append(f"{x.get('name')}: redistribution-blocked source must not be default-bundled")
manifest=json.loads((ROOT/'skills-manifest.json').read_text(encoding='utf-8'))
if manifest.get('lock_file')!='external-skills-lock.json': errors.append('skills-manifest must point to external-skills-lock.json')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('external-skills-lock-check: OK — exact refs + license/redistribution gates')

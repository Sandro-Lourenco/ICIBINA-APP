#!/usr/bin/env python3
from __future__ import annotations
import re,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'frontend/src'
if not SRC.exists(): print('frontend-architecture-check: frontend/src absent; blueprint mode'); raise SystemExit(0)
policy=json.loads((ROOT/'frontend/architecture-policy.json').read_text())
viol=[]
IMPORT_RE=re.compile(r"(?:from\s+|import\s*\(\s*)[\"']([^\"']+)[\"']")
for p in list(SRC.rglob('*.ts'))+list(SRC.rglob('*.tsx'))+list(SRC.rglob('*.js'))+list(SRC.rglob('*.jsx')):
 txt=p.read_text(encoding='utf-8',errors='ignore'); rel='/' + p.relative_to(SRC).as_posix()
 if policy['forbidRawFetchOutsideTransport'] and re.search(r'\bfetch\s*\(',txt):
  if not any(x in rel.lower() for x in policy['apiTransportAllowedPathFragments']):
   viol.append(f'{p.relative_to(ROOT)}: raw fetch outside API/transport layer')
 parts=p.relative_to(SRC).parts
 if policy['forbidCrossFeatureInternals'] and len(parts)>=2 and parts[0]=='features':
  owner=parts[1]
  for imp in IMPORT_RE.findall(txt):
   m=re.search(r'(?:^|/)features/([^/]+)/(.*)',imp)
   if m and m.group(1)!=owner:
    tail=m.group(2)
    if tail not in policy['featurePublicEntrypoints'] and '/' in tail:
     viol.append(f'{p.relative_to(ROOT)}: imports internals of feature {m.group(1)} via {imp}')
if viol:
 for x in viol: print(x)
 raise SystemExit(1)
print('frontend-architecture-check: OK')

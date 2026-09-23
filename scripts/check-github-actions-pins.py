#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in (ROOT/'.github/workflows').glob('*.yml'):
 for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  m=re.search(r'uses:\s*([^\s]+)',line)
  if not m: continue
  val=m.group(1).strip('"\'')
  if val.startswith('./'): continue
  if '@' not in val or not re.fullmatch(r'.+@[0-9a-f]{40}',val):
   errors.append(f'{p.relative_to(ROOT)}:{i}: unpinned action {val}')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('github-actions-pin-check: OK')

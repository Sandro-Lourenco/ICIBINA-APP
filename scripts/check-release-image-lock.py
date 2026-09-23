#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
lock=json.loads((ROOT/'release-images-lock.json').read_text(encoding='utf-8'))
wf=(ROOT/'.github/workflows/release-gates.yml').read_text(encoding='utf-8')
errors=[]
for name,rec in lock['images'].items():
    ref=rec['reference']
    if not re.fullmatch(r'[^\s]+@sha256:[0-9a-f]{64}',ref): errors.append(f'{name}: invalid digest reference')
    if ref not in wf: errors.append(f'{name}: locked digest not used by release workflow')
for pat in [r'(?<![\w/.-])postgres:[^\s"\']+', r'(?<![\w/.-])tufin/oasdiff:[^\s"\']+']:
    for bad in re.findall(pat,wf): errors.append('mutable release image reference: '+bad)
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('release-image-lock: OK')

#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('--strict',action='store_true'); a=p.parse_args()
lock=json.loads((ROOT/'development-images-lock.json').read_text(encoding='utf-8'))
compose=(ROOT/'docker-compose.target.yml').read_text(encoding='utf-8')
env=(ROOT/'config/.env.example').read_text(encoding='utf-8')
errors=[]; warnings=[]
for name,item in lock['images'].items():
    ref=item['reference']; review_by=date.fromisoformat(item['review_by'])
    if review_by < date.today(): (errors if a.strict else warnings).append(f'{name}: review overdue since {review_by}')
    if name=='minio' and ref not in compose+env: errors.append('minio reference differs from development-images-lock.json')
    if '@sha256:' in ref: warnings.append(f'{name}: dev image is immutable; acceptable but refresh cadence still applies')
for w in warnings: print('WARNING:',w)
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('development-image-review: OK')

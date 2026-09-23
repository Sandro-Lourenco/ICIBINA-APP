#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('--strict',action='store_true'); a=p.parse_args()
data=json.loads((ROOT/'capacity-baseline.json').read_text())
required={'mau','peak_concurrent_sessions','api_rps','write_rps','webhook_burst','jobs_throughput','video_ingest','database_size'}
missing=required-set(data.get('metrics',{})); errors=[]
if missing: errors.append('missing metrics: '+', '.join(sorted(missing)))
verified=data.get('status')=='verified'
if verified:
    for k in required:
        rec=data['metrics'][k]
        for field in ('launch_expected','tested_limit'):
            if not isinstance(rec.get(field),(int,float)) or rec[field] < 0: errors.append(f'{k}.{field} must be numeric when verified')
    if not data.get('last_verified_at') or not data.get('evidence_commit'): errors.append('verified baseline needs timestamp and evidence_commit')
    for k in ('k6_report','database_metrics_snapshot'):
        if not data.get('evidence',{}).get(k): errors.append('verified baseline missing evidence.'+k)
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
if not verified:
    print('capacity-baseline: PENDING (no measured production baseline yet)')
    sys.exit(1 if a.strict else 0)
print('capacity-baseline: VERIFIED')

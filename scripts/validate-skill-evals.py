#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
file=ROOT/'evals/skill-routing.jsonl'
errors=[]; records=[]
for i,line in enumerate(file.read_text(encoding='utf-8').splitlines(),1):
 if not line.strip(): continue
 try: r=json.loads(line)
 except Exception as e: errors.append(f'line {i}: invalid JSON: {e}'); continue
 for k in ('id','prompt','expected','optional','must_not'):
  if k not in r: errors.append(f'line {i}: missing {k}')
 if set(r.get('expected',[])) & set(r.get('must_not',[])): errors.append(f'line {i}: same skill expected and forbidden')
 records.append(r)
local=set()
for p in (ROOT/'.agents/skills').glob('*/SKILL.md'):
 t=p.read_text(encoding='utf-8'); m=re.search(r'^name:\s*(.+)$',t,re.M)
 if m: local.add(m.group(1).strip().strip('"\''))
lock=json.loads((ROOT/'external-skills-lock.json').read_text(encoding='utf-8'))
external={x['target_name'] for x in lock.get('sources',[])}
known=local|external
for r in records:
 for name in r['expected']+r['optional']+r['must_not']:
  if name not in known: errors.append(f"{r['id']}: unknown skill {name}")
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print(f'skill-evals-check: OK ({len(records)} routing fixtures, {len(known)} known skills)')

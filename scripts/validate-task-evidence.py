#!/usr/bin/env python3
import json,sys
from pathlib import Path
p=Path(sys.argv[1]) if len(sys.argv)>1 else None
if not p or not p.exists():
 print('usage: validate-task-evidence.py <evidence.json>'); sys.exit(2)
d=json.loads(p.read_text(encoding='utf-8'))
errors=[]
for k in ['task_id','routing_profile','local_orchestrators','external_skills_loaded','commands_executed','gates','files_changed','residual_risks']:
 if k not in d: errors.append('missing '+k)
for g in d.get('gates',[]):
 if g.get('status')=='PASS' and not str(g.get('evidence','')).strip(): errors.append(f"PASS gate without evidence: {g.get('name')}")
if d.get('routing_profile')=='frontend':
 fx=d.get('frontend_experience')
 if not isinstance(fx,dict): errors.append('frontend routing requires frontend_experience evidence')
 elif not str(fx.get('surface_profile','')).strip(): errors.append('frontend_experience.surface_profile required')
 else:
  allowed={'Editorial Light','Student Immersive','Operational Light','Operational Neutral','N/A'}
  if fx.get('surface_profile') not in allowed: errors.append('frontend_experience.surface_profile must use a canonical ICIBINA profile')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('task-evidence-check: OK')

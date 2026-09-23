#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
lock=json.loads((ROOT/'external-skills-lock.json').read_text(encoding='utf-8'))
by={x['target_name']:x for x in lock['sources']}
for n in ['clean-code','software-architect','fastapi-expert']:
 if by.get(n,{}).get('mode')!='manual': errors.append(n+' must remain manual')
if by.get('motion',{}).get('mode')!='reference-only' or by.get('motion',{}).get('redistribution')!='blocked': errors.append('motion upstream skill must remain reference-only/redistribution-blocked until license verification')
for n in ['fastapi','test-master','playwright-expert','security-reviewer','web-accessibility-web-accessibility','opentelemetry','k6']:
 if by.get(n,{}).get('mode')!='default': errors.append(n+' should be installed but routed on demand')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('skill-policy-check: OK')

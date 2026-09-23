#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
css=(ROOT/'design-system/integrative-medicine/tokens.css').read_text(encoding='utf-8')
design=json.loads((ROOT/'.21st/design.json').read_text(encoding='utf-8'))
checks={'background':'--bg','surface':'--surface','foreground':'--text','primary':'--primary','primaryHover':'--primary-hover','accent':'--accent','border':'--border','muted':'--text-muted'}
errors=[]
for key,var in checks.items():
 m=re.search(rf'{re.escape(var)}:\s*(#[0-9A-Fa-f]{{6}})',css)
 if not m: errors.append(f'token {var} missing in CSS'); continue
 if design.get('tokens',{}).get(key,'').lower()!=m.group(1).lower():
  errors.append(f'.21st {key} drift: {design.get("tokens",{}).get(key)} != {m.group(1)}')
if design.get('sourceOfTruth')!='design-system/integrative-medicine/MASTER.md': errors.append('wrong sourceOfTruth')
profiles=design.get('experienceProfiles',{})
if 'studentImmersive' not in profiles: errors.append('.21st studentImmersive profile missing')
if profiles.get('studentImmersive',{}).get('motion') != 7: errors.append('.21st studentImmersive motion dial drift')

imm=design.get('studentImmersiveTokens',{})
source=json.loads((ROOT/'design-system/integrative-medicine/tokens.json').read_text(encoding='utf-8'))['themes']['studentImmersive']['color']
imm_checks={'background':'background','surface':'surface','surfaceElevated':'surfaceElevated','foreground':'foreground','muted':'mutedForeground','border':'border','primary':'primary','accent':'accent','focus':'focus'}
for key,source_key in imm_checks.items():
 expected=source[source_key]['$value']
 if str(imm.get(key,'')).lower()!=expected.lower(): errors.append(f'.21st immersive {key} drift: {imm.get(key)} != {expected}')

if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
print('21st-design-context-check: OK')

#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('--strict',action='store_true'); args=p.parse_args()
errors=[]; pending=[]
local_required={
 'frontend orchestrator':ROOT/'.agents/skills/frontend-experience-orchestrator/SKILL.md',
 'frontend contract':ROOT/'docs/contracts/FRONTEND-CONTRACT.md',
 'design master':ROOT/'design-system/integrative-medicine/MASTER.md',
 'tokens css':ROOT/'design-system/integrative-medicine/tokens.css',
 '21st design json':ROOT/'.21st/design.json',
 '21st design doc':ROOT/'.21st/DESIGN.md',
 'surface profiles':ROOT/'design-system/integrative-medicine/SURFACES.md',
 'motion system':ROOT/'design-system/integrative-medicine/MOTION.md',
 'UIUX recipes':ROOT/'design-system/integrative-medicine/UIUX-PRO-MAX-RECIPES.md',
 'UIUX portable bridge':ROOT/'scripts/uiux-pro-max.py',
 '21st workflow':ROOT/'design-system/integrative-medicine/21ST-WORKFLOW.md',
 'local Motion orchestrator':ROOT/'.agents/skills/motion-experience-orchestrator/SKILL.md',
 'shadcn bootstrap contract':ROOT/'docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md',
}
print('Frontend agent readiness\n'+'='*28)
for label,path in local_required.items():
 if path.exists(): print(f'OK    {label}: {path.relative_to(ROOT)}')
 else: errors.append(f'{label} missing')
lock=json.loads((ROOT/'external-skills-lock.json').read_text(encoding='utf-8'))
locked={x['target_name'] for x in lock['sources'] if x['mode']=='default'}
needed=['ui-ux-pro-max','react','21st-cli-use','21st-ui-explore','21st-ui-build','21st-ui-review','web-accessibility-web-accessibility']
for name in needed:
 if name in locked: print(f'OK    reviewed/locked: {name}')
 else: errors.append(f'lock missing {name}')
for agent,path in [('Codex',ROOT/'plugins/codex/icibina-engineering/skills'),('Antigravity',ROOT/'plugins/antigravity/icibina-engineering/skills')]:
 if not path.exists():
  pending.append(f'{agent} plugin bundle not built')
  continue
 missing=[n for n in needed if not (path/n/'SKILL.md').exists()]
 if missing: errors.append(f'{agent} bundle missing {missing}')
 else: print(f'OK    {agent} frontend skills bundled')
if shutil.which('21st'): print('OK    21st CLI runtime available')
else: pending.append('21st CLI runtime not installed')
if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
if pending:
 for x in pending: print('PENDING:',x)
 if args.strict: sys.exit(2)
 print('\nSTATUS: BLUEPRINT READY / CLI INSTALL PENDING')
else:
 print('\nSTATUS: FRONTEND AGENT STACK READY')

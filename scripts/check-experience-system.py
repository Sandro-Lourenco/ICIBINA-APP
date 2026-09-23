#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
DS=ROOT/'design-system/integrative-medicine'
required=[
 'design-system/integrative-medicine/MASTER.md','design-system/integrative-medicine/SURFACES.md',
 'design-system/integrative-medicine/MOTION.md','design-system/integrative-medicine/UIUX-PRO-MAX-RECIPES.md',
 'design-system/integrative-medicine/21ST-WORKFLOW.md','design-system/integrative-medicine/VISUAL-QA.md',
 'design-system/integrative-medicine/pages/student-dashboard.md','design-system/integrative-medicine/preview.html',
 'docs/60-FRONTEND-DESIGN-EXCELLENCE-PIPELINE.md','design-system/integrative-medicine/references/student-dashboard-premium-direction.png',
 'scripts/uiux-pro-max.py','scripts/check-uiux-pro-max-bridge.py','docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md','scripts/check-shadcn-bootstrap-contract.py','docs/tasks/TASK_EVIDENCE_TEMPLATE.json']
errors=[]
for p in required:
 if not (ROOT/p).exists(): errors.append('missing '+p)
if errors:
 [print('ERROR:',e) for e in errors]; sys.exit(1)
master=(DS/'MASTER.md').read_text(encoding='utf-8')
surfaces=(DS/'SURFACES.md').read_text(encoding='utf-8')
motion=(DS/'MOTION.md').read_text(encoding='utf-8')
orch=(ROOT/'.agents/skills/frontend-experience-orchestrator/SKILL.md').read_text(encoding='utf-8')
design=json.loads((ROOT/'.21st/design.json').read_text(encoding='utf-8'))
tokens=json.loads((DS/'tokens.json').read_text(encoding='utf-8'))
evidence=(ROOT/'docs/tasks/TASK_EVIDENCE_TEMPLATE.json').read_text(encoding='utf-8')
preview=(DS/'preview.html').read_text(encoding='utf-8')
builder=(ROOT/'scripts/build-agent-cli-bundles.py').read_text(encoding='utf-8')
bridge=(ROOT/'scripts/uiux-pro-max.py').read_text(encoding='utf-8')
allowed=['Editorial Light','Student Immersive','Operational Light','Operational Neutral']
for term in allowed:
 if term not in master: errors.append('MASTER missing canonical surface '+term)
 if term not in surfaces: errors.append('SURFACES missing canonical surface '+term)
 if term not in evidence: errors.append('task evidence missing canonical surface '+term)
 if term not in preview: errors.append('preview missing canonical surface '+term)
if 'Dual Experience' in master or 'dual-surface' in json.dumps(design): errors.append('obsolete dual-surface terminology remains')
expected_profiles={'editorialLight','studentImmersive','operationalLight','operationalNeutral'}
actual_profiles=set(design.get('experienceProfiles',{}))
if actual_profiles!=expected_profiles: errors.append(f'.21st profile mismatch: {sorted(actual_profiles)}')
# Every page override must use exactly one canonical profile.
for p in sorted((DS/'pages').glob('*.md')):
 text=p.read_text(encoding='utf-8')
 m=re.search(r'^\*\*Surface:\*\*\s*`([^`]+)`',text,re.M)
 if not m: errors.append(f'{p.name}: missing canonical Surface declaration'); continue
 if m.group(1) not in allowed: errors.append(f'{p.name}: invalid surface {m.group(1)!r}')
# Numbered H2 headings must be unique and strictly increasing.
nums=[int(x) for x in re.findall(r'^##\s+(\d+)\.',master,re.M)]
if len(nums)!=len(set(nums)) or nums!=sorted(nums): errors.append(f'MASTER numbered H2 headings are duplicated/out of order: {nums}')
if nums and nums!=list(range(nums[0],nums[-1]+1)): errors.append('MASTER numbered H2 headings contain gaps')
if 'studentImmersive' not in tokens.get('themes',{}): errors.append('studentImmersive tokens missing')
for term in ['StudentHero','JourneyProgress','ImmersiveCourseCard']:
 if term not in (DS/'pages/student-dashboard.md').read_text(encoding='utf-8'): errors.append('student override missing '+term)
if 'Tier 3' not in motion or 'prefers-reduced-motion' not in motion: errors.append('motion grammar incomplete')
if '--include-motion-plus' not in builder: errors.append('builder lacks explicit Motion+ opt-in')
# Default plugin must not unconditionally register Motion+.
if 'if args.include_motion_plus' not in builder: errors.append('Motion+ is not conditionally registered')
if 'scripts/uiux-pro-max.py' not in orch or 'CLAUDE_PLUGIN_ROOT' not in orch: errors.append('frontend orchestrator must mandate portable UIUX bridge and forbid CLAUDE_PLUGIN_ROOT dependency')
if 'ICIBINA_UIUX_PRO_MAX_ROOT' not in bridge or '.codex/plugins/cache' not in bridge or 'exact search.py, skill root, or plugin root' not in bridge: errors.append('UIUX bridge lacks V5.8 portable override/discovery contract')
visualqa=(DS/'VISUAL-QA.md').read_text(encoding='utf-8')
if 'forced-colors' not in visualqa or 'prefers-contrast' not in visualqa: errors.append('Visual QA missing high-contrast/forced-colors coverage')
if 'shadcn' not in (DS/'21ST-WORKFLOW.md').read_text(encoding='utf-8').lower(): errors.append('21st workflow missing shadcn bootstrap gate')
if errors:
 [print('ERROR:',e) for e in errors]; sys.exit(1)
print('experience-system-check: OK — 4 profiles, robust UIUX bridge, shadcn intake gate, high-contrast QA, Motion+ opt-in')

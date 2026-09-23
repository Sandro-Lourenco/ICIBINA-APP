#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SKILLS=ROOT/'.agents/skills'
p=argparse.ArgumentParser(); p.add_argument('--require-external',action='store_true'); a=p.parse_args()
errors=[]; warnings=[]; seen={}
required_local={
 'frontend-experience-orchestrator','backend-implementation-orchestrator','database-persistence-orchestrator',
 'qa-test-orchestrator','security-assurance-orchestrator','observability-performance-orchestrator',
 'course-platform-architect','asaas-payments','code-quality-orchestrator','platform-quality-gate','motion-experience-orchestrator'}
for path in SKILLS.glob('*/SKILL.md'):
 text=path.read_text(encoding='utf-8'); m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
 if not m: errors.append(f'invalid frontmatter: {path.relative_to(ROOT)}'); continue
 nm=re.search(r'^name:\s*(.+)$',m.group(1),re.M); dm=re.search(r'^description:\s*(.+)$',m.group(1),re.M)
 if not nm or not dm: errors.append(f'name/description missing: {path.relative_to(ROOT)}'); continue
 name=nm.group(1).strip().strip('"\''); desc=dm.group(1).strip().strip('"\'')
 if name in seen: errors.append('duplicate skill: '+name)
 seen[name]=path
 if len(desc)>260: warnings.append(f'description long ({len(desc)}): {name}')
for n in sorted(required_local-set(seen)): errors.append('missing local skill: '+n)
lock=json.loads((ROOT/'external-skills-lock.json').read_text(encoding='utf-8'))
missing=[]
for x in lock['sources']:
 if x['mode'] in ('manual','reference-only'): continue
 if x['target_name'] not in seen: missing.append(x['target_name'])
# External default skills are delivered by generated agent bundles; reference-only sources are intentionally not installed.
for x in errors: print('ERROR:',x)
for x in warnings: print('WARN:',x)
if missing:
 prefix='ERROR' if a.require_external else 'EXTERNAL-MISSING'
 for x in missing: print(f'{prefix}: {x}')
print(f'Validated {len(seen)} installed skills: {len(errors)} local errors, {len(warnings)} warnings, {len(missing)} pinned external gaps')
if errors or (a.require_external and missing): sys.exit(1)

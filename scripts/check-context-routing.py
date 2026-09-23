#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]
contracts=list((ROOT/'docs/contracts').glob('*.md'))
for p in contracts:
 n=len(p.read_text(encoding='utf-8'))
 if n>6500: errors.append(f'contract too large ({n} chars): {p.relative_to(ROOT)}')
for p in (ROOT/'.agents/skills').glob('*/SKILL.md'):
 text=p.read_text(encoding='utf-8'); n=len(text)
 if n>7500: warnings.append(f'local skill large ({n}): {p.relative_to(ROOT)}')
 if 'orchestrator' in p.parent.name and 'docs/contracts/' not in text:
  errors.append(f'orchestrator missing short contract: {p.relative_to(ROOT)}')
for p in [ROOT/'AGENTS.md',ROOT/'.agents/rules/project-core.md']:
 low=p.read_text(encoding='utf-8').lower()
 if 'não carregue' not in low: warnings.append(f'{p.relative_to(ROOT)} lacks explicit context guard')
for x in warnings: print('WARN:',x)
if errors:
 for x in errors: print('ERROR:',x)
 sys.exit(1)
print(f'context-routing-check: OK ({len(contracts)} contracts, {len(warnings)} warnings)')

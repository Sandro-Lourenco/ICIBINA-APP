#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
import re,sys
ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={'.git','.venv','node_modules','dist','build'}
mds=sorted(p for p in ROOT.rglob('*.md') if not any(part in EXCLUDE for part in p.parts))
repo_pat=re.compile(r'`((?:docs|design-system|database|scripts|\.agents|\.github|contracts)/[^`\n]+)`')
link_pat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
missing=[]
for md in mds:
    text=md.read_text(encoding='utf-8',errors='replace')
    for m in repo_pat.finditer(text):
        raw=m.group(1)
        if any(x in raw for x in ['*','{','}','<','>',' ']): continue
        cleaned=raw.rstrip('.,;:').split('#',1)[0]
        if '.' not in Path(cleaned).name: continue
        if not (ROOT/cleaned).exists(): missing.append((md.relative_to(ROOT),raw,'repo path'))
    for m in link_pat.finditer(text):
        raw=m.group(1).strip().strip('<>')
        if not raw or raw.startswith(('#','http://','https://','mailto:','data:')): continue
        raw=unquote(raw.split('#',1)[0])
        if any(x in raw for x in ['{','}','<','>','$']): continue
        candidate=(md.parent/raw).resolve()
        try: candidate.relative_to(ROOT.resolve())
        except ValueError: continue
        if not candidate.exists(): missing.append((md.relative_to(ROOT),raw,'markdown link'))
if missing:
    print('Broken repository-local documentation references:')
    for md,raw,kind in missing: print(f'{md}: {kind}: {raw}')
    sys.exit(1)
print(f'doc-links: OK ({len(mds)} markdown files scanned recursively)')

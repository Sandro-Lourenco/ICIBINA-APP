#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('--strict-runtime',action='store_true'); args=parser.parse_args()
manifest=ROOT/'.agents/cli-bundle-build.json'
if not manifest.exists():
    print('installed-skills-integrity: PENDING (bundles not built)')
    raise SystemExit(1 if args.strict_runtime else 0)
def tree_hash(root):
    h=hashlib.sha256()
    for f in sorted(x for x in root.rglob('*') if x.is_file()):
        rel=f.relative_to(root).as_posix().encode(); b=f.read_bytes(); h.update(len(rel).to_bytes(4,'big')); h.update(rel); h.update(len(b).to_bytes(8,'big')); h.update(b)
    return h.hexdigest()
data=json.loads(manifest.read_text()); lock=json.loads((ROOT/'external-skills-lock.json').read_text()); locked={x['target_name']:x for x in lock['sources']}; errors=[]
bases=[('codex-staging',ROOT/'plugins/codex/icibina-engineering/skills'),('antigravity-staging',ROOT/'plugins/antigravity/icibina-engineering/skills')]
workspace=ROOT/'.agents/plugins/icibina-engineering/skills'
if workspace.exists(): bases.append(('antigravity-active',workspace))
elif args.strict_runtime: errors.append('Antigravity active workspace plugin missing')
codex_cache=Path.home()/'.codex/plugins/cache/icibina-local/icibina-engineering/local/skills'
if codex_cache.exists(): bases.append(('codex-active-cache',codex_cache))
elif args.strict_runtime: errors.append(f'Codex active cache missing: {codex_cache}')
for rec in data.get('external_skills',[]):
    name=rec['target_name']; item=locked.get(name)
    if not item: errors.append(name+': not present in lock'); continue
    if rec.get('ref')!=item.get('ref'): errors.append(name+': built ref differs from lock')
    for label,base in bases:
        path=base/name
        if not path.exists(): errors.append(f'{name}: missing in {label}'); continue
        if tree_hash(path)!=rec.get('tree_sha256'): errors.append(f'{name}: content differs from reviewed tree in {label}')
if errors:
    for e in errors: print('ERROR:',e)
    raise SystemExit(1)
print('installed-skills-integrity: OK ('+', '.join(label for label,_ in bases)+')')

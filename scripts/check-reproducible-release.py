#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
errors=[]; pending=[]

# Frontend lock contract when the real app exists.
frontend=ROOT/'frontend'
real_pkg=frontend/'package.json'
if real_pkg.exists():
    lock=frontend/'package-lock.json'
    if not lock.exists(): errors.append('frontend/package-lock.json required for release')
    data=json.loads(real_pkg.read_text(encoding='utf-8'))
    for sec in ('dependencies','devDependencies'):
        for name,ver in data.get(sec,{}).items():
            if ver in ('latest','*','') or 'latest' in str(ver).lower():
                errors.append(f'forbidden mutable frontend version: {name}={ver}')
else:
    pending.append('real frontend/package.json absent; frontend lock gate deferred')

backend=ROOT/'backend'
if (backend/'pyproject.toml').exists():
    if not (backend/'uv.lock').exists(): errors.append('backend/uv.lock required for release')
    if not (ROOT/'.python-version').exists(): errors.append('.python-version required once backend is real')
else:
    pending.append('backend/pyproject.toml absent; Python lock gate deferred')

# Any production compose/k8s manifest must pin container images by digest.
prod_files=list(ROOT.glob('docker-compose.prod*.yml'))+list(ROOT.glob('docker-compose.prod*.yaml'))
prod_files+=list((ROOT/'deploy').rglob('*.yml')) if (ROOT/'deploy').exists() else []
image_re=re.compile(r'^\s*image:\s*([^#\s]+)',re.M)
for p in prod_files:
    txt=p.read_text(encoding='utf-8')
    for image in image_re.findall(txt):
        if '@sha256:' not in image:
            errors.append(f'production image must be digest pinned: {p.relative_to(ROOT)} -> {image}')
if not prod_files:
    pending.append('production container manifests absent; digest gate deferred')

if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
for p in pending: print('PENDING:',p)
print('reproducible-release-check: OK' if not pending else 'reproducible-release-check: BLUEPRINT OK / release locks pending')

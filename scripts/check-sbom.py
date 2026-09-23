#!/usr/bin/env python3
import json,sys
from pathlib import Path
if len(sys.argv)!=2: raise SystemExit('usage: check-sbom.py <cyclonedx-json>')
p=Path(sys.argv[1]);
if not p.exists() or p.stat().st_size<100: raise SystemExit('SBOM missing/empty: '+str(p))
d=json.loads(p.read_text(encoding='utf-8'))
if d.get('bomFormat')!='CycloneDX': raise SystemExit('SBOM is not CycloneDX')
if not isinstance(d.get('components',[]),list): raise SystemExit('SBOM components invalid')
print(f"sbom-check: OK ({len(d.get('components',[]))} components)")

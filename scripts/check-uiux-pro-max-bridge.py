#!/usr/bin/env python3
from pathlib import Path
import os, subprocess, sys, tempfile, json
ROOT=Path(__file__).resolve().parents[1]
BRIDGE=ROOT/'scripts/uiux-pro-max.py'
errors=[]

def make_search(path: Path):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text('import json,sys; print(json.dumps({"argv":sys.argv[1:]}))\n',encoding='utf-8')

def run(override: Path):
    env=os.environ.copy(); env['ICIBINA_UIUX_PRO_MAX_ROOT']=str(override)
    cp=subprocess.run([sys.executable,str(BRIDGE),'probe','--design-system','--motion','7'],cwd=ROOT,env=env,capture_output=True,text=True)
    if cp.returncode: raise RuntimeError(cp.stderr or cp.stdout)
    return json.loads(cp.stdout.strip())['argv']

with tempfile.TemporaryDirectory() as td:
    t=Path(td)
    # exact file
    exact=t/'exact-search.py'; make_search(exact)
    # skill root
    skill=t/'skill-root'; make_search(skill/'scripts/search.py')
    # plugin root
    plugin=t/'plugin-root'; make_search(plugin/'skills/ui-ux-pro-max/scripts/search.py')
    for label,override in [('exact',exact),('skill-root',skill),('plugin-root',plugin)]:
        try:
            argv=run(override)
            if argv!=['probe','--design-system','--motion','7']:
                errors.append(f'{label}: argument forwarding mismatch: {argv}')
        except Exception as e: errors.append(f'{label}: {e}')
    # Invalid explicit override must fail closed rather than silently falling back.
    env=os.environ.copy(); env['ICIBINA_UIUX_PRO_MAX_ROOT']=str(t/'missing')
    cp=subprocess.run([sys.executable,str(BRIDGE),'--print-path'],cwd=ROOT,env=env,capture_output=True,text=True)
    if cp.returncode==0: errors.append('invalid explicit override must fail closed')
if errors:
    [print('ERROR:',e) for e in errors]; raise SystemExit(1)
print('uiux-pro-max-bridge-check: OK — exact file, skill root, plugin root, fail-closed override')

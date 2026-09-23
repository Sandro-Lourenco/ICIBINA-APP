#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--strict-build', action='store_true', help='require generated plugin bundles to exist')
parser.add_argument('--runtime', action='store_true', help='also query local Codex/Antigravity CLI installations')
parser.add_argument('--agent', choices=['codex','antigravity','both'], default='both')
args=parser.parse_args()
errors=[]; pending=[]

required={
 'codex marketplace':ROOT/'.agents/plugins/marketplace.json',
 'codex config':ROOT/'.codex/config.toml',
 'codex installer ps1':ROOT/'scripts/install-skills-codex.ps1',
 'codex installer sh':ROOT/'scripts/install-skills-codex.sh',
 'antigravity installer ps1':ROOT/'scripts/install-skills-antigravity.ps1',
 'antigravity installer sh':ROOT/'scripts/install-skills-antigravity.sh',
 'bundle builder':ROOT/'scripts/build-agent-cli-bundles.py',
 'runtime smoke':ROOT/'scripts/smoke-agent-skills.py',
 'codex marketplace configurator':ROOT/'scripts/configure-codex-marketplace.py',
 'antigravity workspace installer':ROOT/'scripts/install-antigravity-workspace-plugin.py',
}
for label,p in required.items():
 if p.exists(): print('OK   ',label,p.relative_to(ROOT))
 else: errors.append(f'missing {label}: {p.relative_to(ROOT)}')

market=json.loads((ROOT/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
if market.get('name')!='icibina-local': errors.append('Codex marketplace name must be icibina-local')
entries={x.get('name'):x for x in market.get('plugins',[])}
entry=entries.get('icibina-engineering')
if not entry: errors.append('Codex marketplace missing icibina-engineering plugin')
elif entry.get('policy',{}).get('installation')!='INSTALLED_BY_DEFAULT': errors.append('Codex plugin must be INSTALLED_BY_DEFAULT')

codex_cfg=(ROOT/'.codex/config.toml').read_text(encoding='utf-8')
if '[plugins."icibina-engineering@icibina-local"]' not in codex_cfg or 'enabled = true' not in codex_cfg:
 errors.append('Codex project config must enable icibina-engineering@icibina-local')

lock=json.loads((ROOT/'external-skills-lock.json').read_text(encoding='utf-8'))
required_skill_names={x['target_name'] for x in lock['sources'] if x['mode']=='default'}
for n in ['ui-ux-pro-max','react','21st-ui-build','fastapi','test-master','security-reviewer','opentelemetry','k6']:
 if n not in required_skill_names: errors.append(f'lock missing required CLI-bundled skill: {n}')

targets=[]
if args.agent in ('codex','both'):
 targets.append(('Codex',ROOT/'plugins/codex/icibina-engineering'))
if args.agent in ('antigravity','both'):
 targets.append(('Antigravity',ROOT/'.agents/plugins/icibina-engineering'))
for agent,path in targets:
 if not path.exists() or not (path/'skills').exists():
  pending.append(f'{agent} plugin bundle not built/activated yet')
  continue
 names={p.parent.name for p in (path/'skills').glob('*/SKILL.md')}
 missing=sorted(required_skill_names-names)
 if missing: errors.append(f'{agent} plugin bundle missing skills: {missing}')
 else: print(f'OK    {agent} plugin bundle contains {len(names)} skills')
 if agent=='Codex':
  if not (path/'plugin.json').exists(): errors.append('Codex plugin missing plugin.json')
  mcp_file=path/'mcp.json'
 else:
  if not (path/'plugin.json').exists(): errors.append('Antigravity plugin missing plugin.json')
  mcp_file=path/'mcp_config.json'
 if not mcp_file.exists():
  errors.append(f'{agent} plugin missing Motion MCP config')
 else:
  mcp_data=json.loads(mcp_file.read_text(encoding='utf-8')).get('mcpServers',{})
  if 'motion' not in mcp_data: errors.append(f'{agent} plugin must include public Motion MCP')
  build_manifest=ROOT/'.agents/cli-bundle-build.json'
  if build_manifest.exists():
   plus_enabled=bool(json.loads(build_manifest.read_text(encoding='utf-8')).get('motion_plus_enabled'))
   if plus_enabled and 'motion-plus' not in mcp_data: errors.append(f'{agent} Motion+ opt-in recorded but MCP missing')
   if not plus_enabled and 'motion-plus' in mcp_data: errors.append(f'{agent} Motion+ present without explicit opt-in')

if args.runtime:
 runtime_targets=[]
 if args.agent in ('codex','both'): runtime_targets.append(('codex','Codex CLI',['codex','plugin','marketplace','list']))
 if args.agent in ('antigravity','both'): runtime_targets.append(('agy','Antigravity CLI',['agy','plugin','list']))
 for exe,label,cmd in runtime_targets:
  if not shutil.which(exe):
   errors.append(f'{label} not found in PATH')
   continue
  cp=subprocess.run(cmd,capture_output=True,text=True)
  if cp.returncode!=0: errors.append(f'{label} runtime check failed: {cp.stderr.strip()}')
  else:
   print(f'OK    {label} runtime command')
   if 'icibina' not in (cp.stdout+cp.stderr).lower(): pending.append(f'{label}: ICIBINA registration not visible in list output')

if errors:
 for e in errors: print('ERROR:',e)
 sys.exit(1)
if pending:
 for p in pending: print('PENDING:',p)
 if args.strict_build: sys.exit(2)
print('agent-cli-bundle-check: OK' if not pending else 'agent-cli-bundle-check: BLUEPRINT OK / runtime build pending')

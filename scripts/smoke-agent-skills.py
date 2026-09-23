#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,shutil,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MARKER_RE=re.compile(r"SMOKE_MARKER:\s*`([^`]+)`")
LOCAL_CASES=[(p.parent.name,p) for p in sorted((ROOT/'.agents/skills').glob('*/SKILL.md'))]
EXTERNAL_CASES=[
 ("ui-ux-pro-max", "Read the loaded skill. Return one JSON object only with integer keys total_styles and active_styles for its searchable UI style counts.", {"total_styles":79,"active_styles":50}),
 ("fastapi", "Read the loaded official FastAPI skill. Return one JSON object only with string keys dev and prod containing the recommended FastAPI CLI commands.", {"dev":"fastapi dev","prod":"fastapi run"}),
]
def marker(path):
 m=MARKER_RE.search(path.read_text(encoding='utf-8'))
 if not m: raise SystemExit(f'missing SMOKE_MARKER in {path}')
 return m.group(1)
def run(cmd,timeout=180): return subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=timeout)
def codex_prompt(skill,instruction): return f"Use the ${skill} skill from the active ICIBINA plugin. Do not edit files or run shell commands. {instruction}"
def agy_prompt(skill,instruction): return f"Use the {skill} skill from the active ICIBINA workspace plugin. Do not edit files or run commands. {instruction}"
def collect_strings(value):
 out=[]
 if isinstance(value,str): out.append(value)
 elif isinstance(value,dict):
  for v in value.values(): out.extend(collect_strings(v))
 elif isinstance(value,list):
  for v in value: out.extend(collect_strings(v))
 return out
def codex_text(stdout):
 parts=[]
 for line in stdout.splitlines():
  try: parts.extend(collect_strings(json.loads(line)))
  except Exception: parts.append(line)
 return '\n'.join(parts)
def first_json_object(text):
 decoder=json.JSONDecoder()
 for i,ch in enumerate(text):
  if ch!='{': continue
  try:
   obj,_=decoder.raw_decode(text[i:])
   if isinstance(obj,dict): return obj
  except Exception: pass
 raise ValueError('no JSON object found in agent response')
def execute(agent,skill,instruction,expected):
 if agent=='codex':
  cp=run(['codex','exec','--json',codex_prompt(skill,instruction)])
  if cp.returncode: raise RuntimeError(cp.stderr.strip() or 'codex exec failed')
  out=codex_text(cp.stdout)
 else:
  cp=run(['agy','-p',agy_prompt(skill,instruction),'--output-format','json','--print-timeout','3m'])
  if cp.returncode: raise RuntimeError(cp.stderr.strip() or 'agy failed')
  data=json.loads(cp.stdout)
  if data.get('status')!='SUCCESS': raise RuntimeError(data.get('error') or str(data.get('status')))
  out=data.get('response','')
 if isinstance(expected,dict):
  obj=first_json_object(out)
  for k,v in expected.items():
   actual=obj.get(k)
   if isinstance(v,str):
    if re.sub(r'\s+',' ',str(actual).strip()).lower()!=re.sub(r'\s+',' ',v.strip()).lower():
     raise RuntimeError(f'{k}: expected {v!r}, got {actual!r}')
   elif actual!=v: raise RuntimeError(f'{k}: expected {v!r}, got {actual!r}')
 elif expected not in out: raise RuntimeError(f'expected evidence {expected!r} not found')
 print(f'PASS  {agent}:{skill}')
parser=argparse.ArgumentParser(); parser.add_argument('--agent',choices=['codex','antigravity','both'],default='both'); parser.add_argument('--all',action='store_true'); parser.add_argument('--external',action='store_true')
a=parser.parse_args()
for agent,bin in [('codex','codex'),('antigravity','agy')]:
 if a.agent in (agent,'both') and not shutil.which(bin): raise SystemExit(f'{bin} CLI not found')
cases=[]
local=LOCAL_CASES if a.all else LOCAL_CASES[:1]
for s,p in local: cases.append((s,'Read the loaded skill and return only the value after SMOKE_MARKER.',marker(p)))
if a.external or a.all: cases += EXTERNAL_CASES
fail=[]
for s,inst,exp in cases:
 for agent in (['codex','antigravity'] if a.agent=='both' else [a.agent]):
  try: execute(agent,s,inst,exp)
  except Exception as e: fail.append(f'{agent}:{s}: {e}'); print('FAIL',fail[-1])
if fail: raise SystemExit(1)
print('agent-skill-smoke: OK')

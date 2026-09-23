#!/usr/bin/env python3
"""Architecture fitness functions for ICIBINA.

Blueprint mode: exits 0 when backend/src does not exist.
Implementation mode: checks import/layer rules and transaction ownership smells.
"""
from __future__ import annotations
import ast, sys
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'backend/src'
if not SRC.exists():
    print('architecture-check: backend/src absent; blueprint mode (skip code checks)')
    raise SystemExit(0)

viol=[]
module_edges=defaultdict(set)
DOMAIN_FORBIDDEN=('fastapi','sqlalchemy','redis','httpx','boto3','botocore','pydantic')
INTERFACE_FORBIDDEN=('sqlalchemy',)

def layer(path: Path) -> str|None:
    for name in ('domain','application','infrastructure','interface','interfaces'):
        if name in path.parts:
            return 'interface' if name=='interfaces' else name
    return None

def imports(tree):
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):
            for a in node.names: yield a.name
        elif isinstance(node,ast.ImportFrom) and node.module:
            yield node.module

def calls_commit(tree):
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr in {'commit','rollback'}:
            yield node.func.attr,node.lineno

for path in SRC.rglob('*.py'):
    try: tree=ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
    except Exception as e:
        viol.append((path,f'parse error: {e}')); continue
    ly=layer(path)
    for name in imports(tree):
        low=name.lower()
        # Module boundary: src.modules.<A> must not import another module's infrastructure/interface internals.
        parts=name.split('.')
        if 'modules' in path.parts and 'modules' in parts:
            try:
                src_mod=path.parts[path.parts.index('modules')+1]
                dst_mod=parts[parts.index('modules')+1]
                if src_mod != dst_mod:
                    module_edges[src_mod].add(dst_mod)
                    tail=parts[parts.index('modules')+2:]
                    if any(x in {'infrastructure','interface','interfaces','repositories'} for x in tail):
                        viol.append((path,f'cross-module internal import: {name}'))
            except (ValueError,IndexError):
                pass
        if ly=='domain' and low.startswith(DOMAIN_FORBIDDEN):
            viol.append((path,f'forbidden domain import: {name}'))
        if ly=='application' and ('.infrastructure' in low or low.endswith('infrastructure') or low.startswith('infrastructure')):
            viol.append((path,f'application depends on infrastructure: {name}'))
        if ly=='interface' and low.startswith(INTERFACE_FORBIDDEN):
            viol.append((path,f'interface/router imports SQLAlchemy directly: {name}'))
    # transaction boundary smell: repository adapters should not own commit/rollback
    if 'repositories' in path.parts or 'repository' in path.stem.lower():
        for method,line in calls_commit(tree):
            viol.append((path,f'repository calls {method}() at line {line}; Unit of Work should own transaction'))

# Coarse module dependency cycle detector. Cycles usually signal leaked bounded-context internals.
visiting=set(); visited=set()
def dfs(n,stack):
    if n in visiting:
        cycle=' -> '.join(stack+[n]); viol.append((SRC,f'module dependency cycle: {cycle}')); return
    if n in visited: return
    visiting.add(n)
    for m in module_edges.get(n,()): dfs(m,stack+[n])
    visiting.remove(n); visited.add(n)
for n in list(module_edges): dfs(n,[])

if viol:
    for p,msg in viol: print(f'{p.relative_to(ROOT)}: {msg}')
    raise SystemExit(1)
print('architecture-check: OK')

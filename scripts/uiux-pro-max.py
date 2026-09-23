#!/usr/bin/env python3
"""Portable launcher for the reviewed UI/UX Pro Max search tool.

Discovery is deterministic and host-agnostic. It accepts an explicit override as:
- exact search.py path;
- UI/UX Pro Max skill root containing scripts/search.py;
- plugin root containing skills/ui-ux-pro-max/scripts/search.py.

It does not depend on CLAUDE_PLUGIN_ROOT.
"""
from __future__ import annotations
import argparse, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = Path('skills/ui-ux-pro-max/scripts/search.py')
CANONICAL_CODEX_CACHE = Path.home()/'.codex/plugins/cache/icibina-local/icibina-engineering/local/skills/ui-ux-pro-max/scripts/search.py'


def _expand_override(raw: str) -> list[Path]:
    p = Path(raw).expanduser()
    if p.is_file() or p.name == 'search.py':
        return [p]
    return [
        p/'scripts/search.py',
        p/'ui-ux-pro-max/scripts/search.py',
        p/REL,
    ]


def candidates() -> list[Path]:
    override = os.environ.get('ICIBINA_UIUX_PRO_MAX_ROOT')
    if override:
        explicit = _expand_override(override)
        found = [p for p in explicit if p.is_file()]
        if not found:
            attempted='\n  - '.join(str(p) for p in explicit)
            raise SystemExit(
                'ICIBINA_UIUX_PRO_MAX_ROOT was set but no UI/UX Pro Max search.py was found. '
                'Accepted forms: exact search.py, skill root, or plugin root. Attempted:\n  - '+attempted
            )
        return found

    ordered = [
        # Active/project-scoped locations first.
        ROOT/'.agents/plugins/icibina-engineering'/REL,
        CANONICAL_CODEX_CACHE,
        # Generated staging bundles next.
        ROOT/'plugins/codex/icibina-engineering'/REL,
        ROOT/'plugins/antigravity/icibina-engineering'/REL,
        # Direct project skill location for diagnostics/development only.
        ROOT/'.agents/skills/ui-ux-pro-max/scripts/search.py',
    ]

    # Last-resort Codex cache discovery. Newest mtime wins so stale copies are
    # less likely to shadow an active installation; canonical cache above still wins.
    cache = Path.home()/'.codex/plugins/cache'
    if cache.exists():
        fallback=[]
        for p in cache.glob('**/skills/ui-ux-pro-max/scripts/search.py'):
            if p == CANONICAL_CODEX_CACHE:
                continue
            try: m=p.stat().st_mtime
            except OSError: m=0
            fallback.append((m,p))
        ordered.extend(p for _,p in sorted(fallback,key=lambda x:x[0],reverse=True))
    return ordered


def resolve() -> Path:
    seen=set()
    for p in candidates():
        try: rp=p.resolve()
        except Exception: rp=p
        key=str(rp)
        if key in seen: continue
        seen.add(key)
        if rp.is_file(): return rp
    raise SystemExit(
        'UI/UX Pro Max search.py not found. Install/build ICIBINA agent skills first '
        '(scripts/install-agent-skills.*) or set ICIBINA_UIUX_PRO_MAX_ROOT to an exact search.py, skill root, or plugin root.'
    )

parser=argparse.ArgumentParser(add_help=False)
parser.add_argument('--print-path',action='store_true')
known,rest=parser.parse_known_args()
path=resolve()
if known.print_path:
    print(path)
    raise SystemExit(0)
cp=subprocess.run([sys.executable,str(path),*rest],cwd=ROOT)
raise SystemExit(cp.returncode)

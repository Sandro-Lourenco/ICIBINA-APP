#!/usr/bin/env python3
"""Run the pinned Microsoft postgres-mcp with an ICIBINA-isolated profile store.

The wrapper redirects HOME/USERPROFILE for postgres-mcp configuration only, so the
agent cannot enumerate unrelated ~/.postgres-mcp profiles from other projects.
Passwords remain handled by the OS keyring when connection set-password is used.
"""
from __future__ import annotations
import os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / '.icibina' / 'mcp-home'
HOME.mkdir(parents=True, exist_ok=True)

env = os.environ.copy()
env['HOME'] = str(HOME)
env['USERPROFILE'] = str(HOME)
env.setdefault('POSTGRES_MCP_DISABLE_CWD_ACCESS', '1')
env.setdefault('POSTGRES_MCP_LOG', 'warn')

npx = shutil.which('npx')
if not npx:
    raise SystemExit('npx not found; Node.js is required for postgres-mcp')
args = [npx, '-y', '@microsoft/postgres-mcp@0.1.0-rc.10', *sys.argv[1:]]
cp = subprocess.run(args, cwd=ROOT, env=env)
raise SystemExit(cp.returncode)

#!/usr/bin/env python3
from __future__ import annotations
import shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "icibina-local"

def run(*args: str) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    if cp.returncode != 0:
        sys.stderr.write(cp.stdout)
        sys.stderr.write(cp.stderr)
        raise SystemExit(f"command failed ({cp.returncode}): {' '.join(args)}")
    return cp

if not shutil.which("codex"):
    raise SystemExit("Codex CLI not found in PATH")

before = run("codex", "plugin", "marketplace", "list")
combined = (before.stdout + before.stderr).lower()
if NAME in combined:
    print(f"marketplace {NAME} exists; upgrading")
    run("codex", "plugin", "marketplace", "upgrade", NAME)
else:
    print(f"marketplace {NAME} not found; adding repo-local marketplace")
    run("codex", "plugin", "marketplace", "add", ".")

after = run("codex", "plugin", "marketplace", "list")
if NAME not in (after.stdout + after.stderr).lower():
    raise SystemExit(f"{NAME} is not visible after configuration")
print("codex-marketplace: OK")

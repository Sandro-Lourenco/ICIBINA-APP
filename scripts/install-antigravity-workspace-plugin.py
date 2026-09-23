#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / "plugins" / "antigravity" / "icibina-engineering"
WORKSPACE = ROOT / ".agents" / "plugins" / "icibina-engineering"
VALIDATION_NAME = "icibina-engineering-cli-validation"

def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    if check and cp.returncode != 0:
        sys.stderr.write(cp.stdout)
        sys.stderr.write(cp.stderr)
        raise SystemExit(f"command failed ({cp.returncode}): {' '.join(args)}")
    return cp

if not shutil.which("agy"):
    raise SystemExit("Antigravity CLI (agy) not found in PATH")
if not STAGING.exists():
    raise SystemExit("Antigravity staging plugin is missing; run build-agent-cli-bundles.py first")

# Validate package through the native CLI without leaving ICIBINA rules installed globally.
with tempfile.TemporaryDirectory(prefix="icibina-agy-plugin-") as td:
    temp = Path(td) / VALIDATION_NAME
    shutil.copytree(STAGING, temp)
    manifest = json.loads((temp / "plugin.json").read_text(encoding="utf-8"))
    manifest["name"] = VALIDATION_NAME
    (temp / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Clear a stale validation-only plugin if a previous interrupted run left it behind.
    listing = run("agy", "plugin", "list")
    if VALIDATION_NAME in (listing.stdout + listing.stderr):
        run("agy", "plugin", "uninstall", VALIDATION_NAME)

    run("agy", "plugin", "install", str(temp))
    try:
        listing = run("agy", "plugin", "list")
        if VALIDATION_NAME not in (listing.stdout + listing.stderr):
            raise SystemExit("Antigravity CLI validation plugin not visible after install")
    finally:
        # Always remove the global validation package. ICIBINA must be workspace-scoped.
        run("agy", "plugin", "uninstall", VALIDATION_NAME, check=False)

# Final activation is workspace-only per Antigravity plugin scoping rules.
if WORKSPACE.exists():
    shutil.rmtree(WORKSPACE)
WORKSPACE.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(STAGING, WORKSPACE)

listing = run("agy", "plugin", "list")
if "icibina-engineering" not in (listing.stdout + listing.stderr).lower():
    raise SystemExit("Antigravity did not report the workspace-scoped ICIBINA plugin after activation")
print(f"antigravity-workspace-plugin: OK -> {WORKSPACE.relative_to(ROOT)}")

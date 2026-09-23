#!/usr/bin/env bash
set -euo pipefail

echo "=== ICIBINA — Antigravity 2.0 CLI project-scoped skills install ==="
command -v agy >/dev/null || { echo "Antigravity CLI (agy) not found in PATH" >&2; exit 1; }
command -v python >/dev/null || { echo "Python not found in PATH" >&2; exit 1; }
if [[ "${ICIBINA_MOTION_PLUS:-0}" == "1" ]]; then
  python scripts/build-agent-cli-bundles.py --include-motion-plus
else
  python scripts/build-agent-cli-bundles.py
fi
python scripts/install-antigravity-workspace-plugin.py
python scripts/check-agent-cli-bundles.py --strict-build --agent antigravity

echo
echo "ICIBINA is active only in this workspace under .agents/plugins/icibina-engineering."
echo "Run /skills and /mcp inside this project to inspect discovery."

#!/usr/bin/env bash
set -euo pipefail

echo "=== ICIBINA — Codex CLI native skills install ==="
command -v codex >/dev/null || { echo "Codex CLI not found in PATH" >&2; exit 1; }
command -v python >/dev/null || { echo "Python not found in PATH" >&2; exit 1; }

if [[ "${ICIBINA_MOTION_PLUS:-0}" == "1" ]]; then
  python scripts/build-agent-cli-bundles.py --include-motion-plus
else
  python scripts/build-agent-cli-bundles.py
fi
python scripts/configure-codex-marketplace.py
python scripts/check-agent-cli-bundles.py --strict-build --agent codex

echo
echo "Codex project config enables: icibina-engineering@icibina-local"
echo "Open this repository as a trusted Codex project so .codex/config.toml is applied."

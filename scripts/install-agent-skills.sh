#!/usr/bin/env bash
set -euo pipefail

echo "=== ICIBINA — CLI-native agent setup ==="
if ! command -v 21st >/dev/null; then
  npm install -g @21st-dev/cli@1.17.1
fi

if [[ "${ICIBINA_MOTION_PLUS:-0}" == "1" ]]; then
  ICIBINA_MOTION_PLUS=1 "$(dirname "$0")/install-skills-codex.sh"
  ICIBINA_MOTION_PLUS=1 "$(dirname "$0")/install-skills-antigravity.sh"
else
  "$(dirname "$0")/install-skills-codex.sh"
  "$(dirname "$0")/install-skills-antigravity.sh"
fi

echo
echo "=== Project validation ==="
python scripts/validate-agent-config.py
python scripts/check-external-skills-lock.py
python scripts/check-context-routing.py
python scripts/check-mcp-config.py
python scripts/check-21st-design-context.py
python scripts/check-uiux-pro-max-bridge.py
python scripts/check-shadcn-bootstrap-contract.py
python scripts/check-agent-cli-bundles.py

echo
echo "Skills are installed through Codex CLI and Antigravity 2.0 CLI plugin mechanisms."

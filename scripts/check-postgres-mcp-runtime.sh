#!/usr/bin/env bash
set -euo pipefail
out="$(python scripts/postgres-mcp-wrapper.py connection list 2>&1)"
printf '%s\n' "$out"
grep -q 'icibina-readonly' <<<"$out" || { echo 'MISSING profile icibina-readonly in isolated project store' >&2; exit 2; }
python scripts/check-postgres-mcp-profile-isolation.py --runtime

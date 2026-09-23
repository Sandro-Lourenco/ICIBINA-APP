#!/usr/bin/env bash
set -euo pipefail
HOST_NAME="${ICIBINA_DB_HOST:-localhost}"
PORT="${ICIBINA_DB_PORT:-5432}"
PROFILE="icibina-readonly"
echo "Using project-isolated postgres-mcp profile store: .icibina/mcp-home"
python scripts/postgres-mcp-wrapper.py connection remove "$PROFILE" -f >/dev/null 2>&1 || true
python scripts/postgres-mcp-wrapper.py connection add "$PROFILE" "host=$HOST_NAME port=$PORT user=icibina_mcp_reader dbname=ICIBINA sslmode=prefer" --access-mode ro
python scripts/postgres-mcp-wrapper.py connection set-password "$PROFILE"
python scripts/postgres-mcp-wrapper.py connection list
python scripts/check-postgres-mcp-profile-isolation.py --runtime

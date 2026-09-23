$ErrorActionPreference = "Stop"
$HostName = if ($env:ICIBINA_DB_HOST) { $env:ICIBINA_DB_HOST } else { "localhost" }
$Port = if ($env:ICIBINA_DB_PORT) { $env:ICIBINA_DB_PORT } else { "5432" }
$Profile = "icibina-readonly"
Write-Host "Using project-isolated postgres-mcp profile store: .icibina/mcp-home" -ForegroundColor Cyan
Write-Host "Prerequisite: role icibina_mcp_reader exists in ICIBINA." -ForegroundColor Yellow
python scripts/postgres-mcp-wrapper.py connection remove $Profile -f 2>$null | Out-Null
python scripts/postgres-mcp-wrapper.py connection add $Profile "host=$HostName port=$Port user=icibina_mcp_reader dbname=ICIBINA sslmode=prefer" --access-mode ro
python scripts/postgres-mcp-wrapper.py connection set-password $Profile
python scripts/postgres-mcp-wrapper.py connection list
python scripts/check-postgres-mcp-profile-isolation.py --runtime

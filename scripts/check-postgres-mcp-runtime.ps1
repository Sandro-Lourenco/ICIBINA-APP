$ErrorActionPreference = "Stop"
$out = python scripts/postgres-mcp-wrapper.py connection list 2>&1 | Out-String
Write-Host $out
if ($out -notmatch "icibina-readonly") { throw "MISSING profile icibina-readonly in isolated project store" }
python scripts/check-postgres-mcp-profile-isolation.py --runtime

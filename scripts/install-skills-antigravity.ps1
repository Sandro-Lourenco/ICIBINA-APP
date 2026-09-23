param([switch]$MotionPlus)
$ErrorActionPreference = "Stop"
Write-Host "=== ICIBINA — Antigravity 2.0 CLI project-scoped skills install ===" -ForegroundColor Cyan
if (-not (Get-Command agy -ErrorAction SilentlyContinue)) { throw "Antigravity CLI (agy) não encontrado no PATH." }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python não encontrado no PATH." }
if ($MotionPlus) { python scripts/build-agent-cli-bundles.py --include-motion-plus } else { python scripts/build-agent-cli-bundles.py }
python scripts/install-antigravity-workspace-plugin.py
python scripts/check-agent-cli-bundles.py --strict-build --agent antigravity
Write-Host "ICIBINA ativa apenas neste workspace em .agents/plugins/icibina-engineering." -ForegroundColor Green
Write-Host "Dentro deste projeto use /skills e /mcp para conferir a descoberta." -ForegroundColor Yellow

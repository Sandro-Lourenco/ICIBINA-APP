param([switch]$MotionPlus)
$ErrorActionPreference = "Stop"
Write-Host "=== ICIBINA — Codex CLI native skills install ===" -ForegroundColor Cyan
if (-not (Get-Command codex -ErrorAction SilentlyContinue)) { throw "Codex CLI não encontrado no PATH." }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python não encontrado no PATH." }
if ($MotionPlus) { python scripts/build-agent-cli-bundles.py --include-motion-plus } else { python scripts/build-agent-cli-bundles.py }
python scripts/configure-codex-marketplace.py
python scripts/check-agent-cli-bundles.py --strict-build --agent codex
Write-Host "Codex project config enables icibina-engineering@icibina-local." -ForegroundColor Green
Write-Host "Abra este repositório como trusted project no Codex para aplicar .codex/config.toml." -ForegroundColor Yellow

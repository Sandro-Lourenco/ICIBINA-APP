param([switch]$MotionPlus)
$ErrorActionPreference = "Stop"
Write-Host "=== ICIBINA — CLI-native agent setup ===" -ForegroundColor Cyan

# Runtime used by the reviewed 21st skills. This is NOT how the skills themselves are installed.
if (-not (Get-Command 21st -ErrorAction SilentlyContinue)) {
  npm install -g @21st-dev/cli@1.17.1
}

if ($MotionPlus) {
  & "$PSScriptRoot/install-skills-codex.ps1" -MotionPlus
  & "$PSScriptRoot/install-skills-antigravity.ps1" -MotionPlus
} else {
  & "$PSScriptRoot/install-skills-codex.ps1"
  & "$PSScriptRoot/install-skills-antigravity.ps1"
}

Write-Host "`n=== Project validation ===" -ForegroundColor Cyan
python scripts/validate-agent-config.py
python scripts/check-external-skills-lock.py
python scripts/check-context-routing.py
python scripts/check-mcp-config.py
python scripts/check-21st-design-context.py
python scripts/check-agent-cli-bundles.py

Write-Host "`nSkills are installed through Codex CLI and Antigravity 2.0 CLI plugin mechanisms." -ForegroundColor Green

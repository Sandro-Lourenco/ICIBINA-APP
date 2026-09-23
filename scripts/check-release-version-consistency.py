#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXPECTED_VERSION="5.8.0"
EXPECTED_HUMAN="V5.8"
EXPECTED_MARKER_SUFFIX="_V5_8"
errors=[]

# Canonical blueprint version.
inv=json.loads((ROOT/'architecture-invariants.json').read_text(encoding='utf-8'))
if inv.get('blueprint_version') != EXPECTED_VERSION:
    errors.append(f"architecture-invariants.json blueprint_version must be {EXPECTED_VERSION}")

# Bundle/plugin builder must emit exactly the release version.
builder=(ROOT/'scripts/build-agent-cli-bundles.py').read_text(encoding='utf-8')
for key in ('"version": "5.8.0"','"bundle_version": "5.8.0"'):
    if key not in builder:
        errors.append(f"build-agent-cli-bundles.py missing {key}")
for stale in ('"version": "5.7.0"','"bundle_version": "5.7.0"','"version": "5.6.0"'):
    if stale in builder:
        errors.append(f"build-agent-cli-bundles.py contains stale release value {stale}")

# Every local skill must expose one unique marker for the current release.
marker_re=re.compile(r"SMOKE_MARKER:\s*`([^`]+)`")
markers={}
skill_files=sorted((ROOT/'.agents/skills').glob('*/SKILL.md'))
if not skill_files:
    errors.append('no local skills found')
for skill in skill_files:
    text=skill.read_text(encoding='utf-8')
    found=marker_re.findall(text)
    name=skill.parent.name
    if len(found) != 1:
        errors.append(f"{name}: expected exactly one SMOKE_MARKER, found {len(found)}")
        continue
    marker=found[0]
    if not marker.endswith(EXPECTED_MARKER_SUFFIX):
        errors.append(f"{name}: stale marker {marker}; expected suffix {EXPECTED_MARKER_SUFFIX}")
    if marker in markers:
        errors.append(f"duplicate SMOKE_MARKER {marker}: {markers[marker]} and {name}")
    markers[marker]=name

# Smoke harness must discover all local skills dynamically.
smoke=(ROOT/'scripts/smoke-agent-skills.py').read_text(encoding='utf-8')
if "glob('*/SKILL.md')" not in smoke:
    errors.append('smoke-agent-skills.py must discover all local SKILL.md files dynamically')

# Current release entrypoints and report naming.
for rel in ('README.md','AGENTS.md','MASTER_PROMPT_ANTIGRAVITY.md'):
    text=(ROOT/rel).read_text(encoding='utf-8')
    if EXPECTED_HUMAN not in text:
        errors.append(f"{rel} does not identify current release {EXPECTED_HUMAN}")
for rel in ('CHANGELOG-V5.8.md','VALIDATION_REPORT_V5_8.md'):
    if not (ROOT/rel).exists():
        errors.append(f"missing current release file: {rel}")

# Stale Motion redistribution claims fixed in V5.8.
for rel in ('docs/12-SKILLS-E-AGENTES.md','docs/14-INTEGRACAO-BACKEND-FRONTEND.md'):
    text=(ROOT/rel).read_text(encoding='utf-8')
    forbidden=(
        'UI/UX Pro Max e Motion também seguem esse fluxo',
        'UI/UX Pro Max e `/motion` entram nos plugins pelo commit auditado',
    )
    for phrase in forbidden:
        if phrase in text:
            errors.append(f"{rel} contains stale Motion redistribution claim: {phrase}")
    for required in ('motiondivision/ai-kit','não'):
        if required not in text:
            errors.append(f"{rel} does not document current Motion redistribution policy")

# Deprecated frontend target may only point to real canonical policy files.
legacy=json.loads((ROOT/'frontend/package-target.legacy.json').read_text(encoding='utf-8'))
note=legacy.get('_deprecated','')
if 'dependency-policy.json' in note:
    errors.append('frontend/package-target.legacy.json references nonexistent dependency-policy.json')
for rel in ('toolchain-lock.json','supply-chain-policy.json','docs/40-SUPPLY-CHAIN-AND-LOCKFILES.md'):
    if rel not in note:
        errors.append(f"legacy frontend target must reference {rel}")
    if not (ROOT/rel).exists():
        errors.append(f"legacy frontend target points to missing file {rel}")

if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print(f'release-version-consistency: OK ({len(skill_files)} local skills, {EXPECTED_HUMAN})')

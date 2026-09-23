#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys,tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
inv=json.loads((ROOT/'architecture-invariants.json').read_text(encoding='utf-8'))
errors=[]

roadmap=(ROOT/'docs/11-ROADMAP-DE-IMPLEMENTACAO.md').read_text(encoding='utf-8')
if roadmap.count('Fase 0.5 — Baselines antes da UI massiva') != 1: errors.append('roadmap must contain Fase 0.5 exactly once')
builder=(ROOT/'scripts/build-agent-cli-bundles.py').read_text(encoding='utf-8')
if '5.8.0' not in builder or any(v in builder for v in ['5.7.0','5.5.0','5.4.0','5.2.0']): errors.append('agent bundle builder must emit V5.8.0 only')
prod_role=(ROOT/'database/003_mcp_readonly_role.sql').read_text(encoding='utf-8')
if 'CREATE SCHEMA IF NOT EXISTS agent_inspection AUTHORIZATION icibina_migrator' not in prod_role: errors.append('production MCP schema must be owned by icibina_migrator')
if not (ROOT/inv['release_images_lock']).exists(): errors.append('release image lock missing')
if not (ROOT/inv['capacity_baseline']).exists(): errors.append('capacity baseline missing')
env=(ROOT/'config/.env.example').read_text(encoding='utf-8')
compose=(ROOT/'docker-compose.target.yml').read_text(encoding='utf-8')
roles=(ROOT/'docs/38-DATABASE-ROLES-AND-PRIVILEGES.md').read_text(encoding='utf-8')
asaas=(ROOT/'docs/03-ASAAS-PAGAMENTOS.md').read_text(encoding='utf-8')
for role in inv['roles'].values():
    if role not in roles: errors.append('roles doc missing '+role)
if 'POSTGRES_USER: icibina_owner' not in compose: errors.append('compose bootstrap user must be icibina_owner')
if './database/bootstrap/00_roles.sh:/docker-entrypoint-initdb.d/00_roles.sh:ro' not in compose: errors.append('compose missing role bootstrap mount')
if not re.search(r'^DATABASE_URL=postgresql\+asyncpg://icibina_app:',env,re.M): errors.append('DATABASE_URL must use icibina_app')
if not re.search(r'^DATABASE_MIGRATION_URL=postgresql\+asyncpg://icibina_migrator:',env,re.M): errors.append('DATABASE_MIGRATION_URL must use icibina_migrator')
if 'event id UNIQUE + atualiza pagamento' in asaas: errors.append('legacy synchronous Asaas webhook diagram remains')
for required in ['inbox idempotente','outbox/job','HTTP 2xx','Worker']:
    if required.lower() not in asaas.lower(): errors.append('Asaas canonical flow missing '+required)
for p in [ROOT/'.agents/mcp_config.json', ROOT/'.codex/config.toml']:
    if inv['mcp']['wrapper'] not in p.read_text(encoding='utf-8'): errors.append(f'{p.relative_to(ROOT)} must use isolated MCP wrapper')
if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print('canonical-invariants-check: OK')

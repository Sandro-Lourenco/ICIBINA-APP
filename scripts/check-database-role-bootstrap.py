#!/usr/bin/env python3
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
compose=(ROOT/'docker-compose.target.yml').read_text(); env=(ROOT/'config/.env.example').read_text(); boot=(ROOT/'database/bootstrap/00_roles.sh').read_text(); release=(ROOT/'.github/workflows/release-gates.yml').read_text()
errors=[]
for role in ['icibina_owner','icibina_migrator','icibina_app','icibina_mcp_reader']:
 if role not in compose+env+boot: errors.append('bootstrap contract missing '+role)
if 'database/bootstrap/00_roles.sh:/docker-entrypoint-initdb.d/00_roles.sh:ro' not in compose: errors.append('compose does not mount role bootstrap')
if not re.search(r'DATABASE_URL=postgresql\+asyncpg://icibina_app:',env): errors.append('runtime DB URL role mismatch')
if not re.search(r'DATABASE_MIGRATION_URL=postgresql\+asyncpg://icibina_migrator:',env): errors.append('migration DB URL role mismatch')
for token in ['services:','postgres:','ICIBINA_release','DATABASE_MIGRATION_URL: postgresql+asyncpg://icibina_migrator:','Prove runtime role cannot perform DDL','Prove MCP least-data boundary at runtime']:
 if token not in release: errors.append('release DB isolation missing token: '+token)
if errors:
 for e in errors: print('ERROR:',e)
 raise SystemExit(1)
print('database-role-bootstrap-check: OK')

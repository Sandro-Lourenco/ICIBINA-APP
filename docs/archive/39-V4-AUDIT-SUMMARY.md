# 39 — V4 Audit Summary

## Fechado nesta versão

- progressive disclosure com 4 contratos curtos;
- 7 skills locais/orquestradores com gatilhos estreitos;
- Clean Code/Software Architect externos fora do auto-flow;
- FastAPI expert limitado a framework mechanics;
- PostgreSQL/SQL experts somente para tuning/complexidade;
- React skill subordinada a docs oficiais React 19.3 em detalhes version-sensitive;
- banco `ICIBINA` e `ICIBINA_test`;
- SQLAlchemy 2 async + asyncpg + Alembic como workflow ORM/schema;
- PostgreSQL MCP configurado em Codex + Antigravity;
- role/profile MCP read-only documentados;
- `.21st` derivado do Master com drift check;
- Motion skill/MCP tratados como runtime externo após installer;
- routing eval fixtures;
- architecture check ampliado;
- CI com blueprint, migration smoke, coverage target, dependency audits e frontend gates condicionais.

## Estado esperado antes da instalação externa

`validate-agent-config.py` reporta `EXTERNAL-MISSING` para skills de terceiros. Isso é correto: o ZIP não redistribui essas skills. Após rodar `scripts/install-agent-skills.*`, o strict readiness deve passar.

## Estado esperado antes do backend real

`check_architecture.py` reporta blueprint-mode/skip porque `backend/src` ainda não existe. Quando o backend real for colado/criado, o mesmo script passa a falhar em violações de camadas/commit em repository.

## MCP runtime

A configuração do servidor está versionada, mas credenciais não. O profile `icibina-readonly` deve ser criado localmente e senha armazenada no keyring. Use `scripts/check-postgres-mcp-runtime.*` para comprovar o profile.

## ORM runtime

A decisão ORM está pronta; models e revisions reais ainda serão implementados. SQL de `database/001`/`002` continua blueprint, não migration de produção.

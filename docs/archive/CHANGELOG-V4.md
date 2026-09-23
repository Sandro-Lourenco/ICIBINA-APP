# V4 — Context, MCP, ORM & Orchestration hardening

- banco renomeado para `ICIBINA` / `ICIBINA_test`;
- MCP PostgreSQL Microsoft configurado para Codex + Antigravity, com política read-only;
- role blueprint `icibina_mcp_reader`;
- SQLAlchemy 2 async + asyncpg + Alembic formalizados como único workflow de schema;
- novos `backend-implementation-orchestrator`, `database-persistence-orchestrator`, `code-quality-orchestrator`;
- frontend orchestrator reduzido para progressive disclosure;
- contratos curtos frontend/backend/database/quality;
- `.21st/DESIGN.md` e `.21st/design.json` derivados do Master;
- Clean Code e Software Architect externos removidos do auto-flow e classificados como manual/review-only;
- guards contra conflito do FastAPI generic CRUD com Clean Architecture ICIBINA;
- validators expandidos para context, MCP, DB naming, 21st projection e architecture rules;
- CI atualizado para ICIBINA_test e gates adicionais quando o código existir.

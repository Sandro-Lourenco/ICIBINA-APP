# 33 — PostgreSQL MCP da ICIBINA

## Objetivo

Dar a Codex e Antigravity capacidade de **inspecionar** PostgreSQL sem transformar MCP em canal paralelo de escrita/schema.

Servidor selecionado: `@microsoft/postgres-mcp@0.1.0-rc.10` (versão revisada no toolchain lock).

## Configuração do projeto

- Antigravity: `.agents/mcp_config.json`
- Codex: `.codex/config.toml`

Os arquivos iniciam o servidor MCP, mas **não versionam credenciais**.

## Perfil recomendado

Crie perfil local com senha no keyring do sistema:

```bash
npx -y @microsoft/postgres-mcp@0.1.0-rc.10 connection add icibina-readonly \
  "host=localhost port=5432 user=icibina_mcp_reader dbname=ICIBINA sslmode=prefer" \
  --access-mode ro

npx -y @microsoft/postgres-mcp@0.1.0-rc.10 connection set-password icibina-readonly
npx -y @microsoft/postgres-mcp@0.1.0-rc.10 connection list
```

Para host remoto, use TLS apropriado (`verify-full` quando disponível) e nunca copie senha para o repositório.

## Defense in depth

1. profile `--access-mode ro`;
2. role PostgreSQL `icibina_mcp_reader` com SELECT/CONNECT/USAGE apenas;
3. `default_transaction_read_only=on`;
4. statement timeout e connection limit;
5. `POSTGRES_MCP_DISABLE_CWD_ACCESS=1`;
6. agente não recebe superuser/table-owner;
7. preferir dev/staging/anonymized data.

Bootstrap do role: `database/003_mcp_readonly_role.sql`.

## O que o MCP pode fazer

- listar contexto/schema;
- consultas read-only;
- diagnosticar índices/estatísticas/performance;
- comparar estado real com models/migrations.

## O que o MCP não pode fazer no fluxo ICIBINA

- CREATE/ALTER/DROP;
- INSERT/UPDATE/DELETE;
- aplicar migration;
- corrigir dados produtivos;
- substituir SQLAlchemy/Alembic.

## Schema workflow

```text
Python SQLAlchemy model
 -> Alembic revision
 -> review
 -> test upgrade/downgrade/expand-contract
 -> alembic upgrade
 -> MCP read-only pode verificar o resultado
```

Referência oficial do servidor: https://github.com/microsoft/postgres-mcp


## V5 least-data
O role MCP não recebe SELECT em `public`. Exponha somente views aprovadas em `agent_inspection`; detalhes em `docs/46-MCP-DATA-GOVERNANCE.md`. O pacote MCP é pinado em `0.1.0-rc.10`.


## V5.3 — profile-store isolation

O MCP deve ser iniciado apenas por `scripts/postgres-mcp-wrapper.py`. O wrapper redireciona o store de profiles para `.icibina/mcp-home`; não use `npx ... postgres-mcp run` diretamente nos configs dos agentes. Isso impede enumeração acidental de profiles PostgreSQL de outros projetos.

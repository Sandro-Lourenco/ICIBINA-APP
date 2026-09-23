# MCP PostgreSQL — governança de dados

Read-only não basta: um agente read-only ainda pode exfiltrar dados que consegue ler. O princípio é **least privilege + least data**.

## Superfície permitida

`icibina_mcp_reader` recebe `USAGE` somente em `agent_inspection` e `SELECT` apenas em views aprovadas. Por padrão ele não recebe `SELECT` em `public` ou schemas internos.

Views de inspeção devem:
- excluir password hashes, refresh/session tokens, secrets, documentos e payloads sensíveis;
- mascarar email/telefone quando identidade completa não for necessária;
- evitar payment raw payloads;
- limitar campos de audit logs;
- expor métricas agregadas para diagnóstico sempre que possível.

## Profile MCP

- `access_mode=ro`;
- database role read-only;
- CWD/file access desabilitado;
- statement/idle timeout;
- connection limit;
- segredo no OS keyring.

## Produção

Conexão MCP direta em produção é opt-in, temporária e auditável. Preferir replica/ambiente diagnóstico sanitizado quando possível.

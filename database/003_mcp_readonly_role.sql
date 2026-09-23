-- Operational bootstrap. Execute as DB owner/admin, not via application MCP.
-- Password is configured out-of-band / keyring.

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'icibina_mcp_reader') THEN
    CREATE ROLE icibina_mcp_reader LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
  END IF;
END
$$;

ALTER ROLE icibina_mcp_reader SET default_transaction_read_only = on;
ALTER ROLE icibina_mcp_reader SET statement_timeout = '15s';
ALTER ROLE icibina_mcp_reader SET idle_in_transaction_session_timeout = '15s';
ALTER ROLE icibina_mcp_reader CONNECTION LIMIT 3;

CREATE SCHEMA IF NOT EXISTS agent_inspection AUTHORIZATION icibina_migrator;
ALTER SCHEMA agent_inspection OWNER TO icibina_migrator;
REVOKE ALL ON SCHEMA public FROM icibina_mcp_reader;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM icibina_mcp_reader;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM icibina_mcp_reader;

GRANT CONNECT ON DATABASE "ICIBINA" TO icibina_mcp_reader;
GRANT USAGE ON SCHEMA agent_inspection TO icibina_mcp_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA agent_inspection TO icibina_mcp_reader;
REVOKE CREATE ON SCHEMA agent_inspection FROM icibina_mcp_reader;

-- Future views in agent_inspection must be granted by the actual owner/migrator.
-- Do NOT grant SELECT on application schemas merely for agent convenience.

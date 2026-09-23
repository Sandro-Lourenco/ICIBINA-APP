#!/bin/sh
set -eu

: "${POSTGRES_DB:=ICIBINA}"
: "${POSTGRES_USER:=icibina_owner}"
: "${ICIBINA_APP_PASSWORD:?ICIBINA_APP_PASSWORD is required}"
: "${ICIBINA_MIGRATOR_PASSWORD:?ICIBINA_MIGRATOR_PASSWORD is required}"
: "${ICIBINA_MCP_READER_PASSWORD:?ICIBINA_MCP_READER_PASSWORD is required}"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  -v app_password="$ICIBINA_APP_PASSWORD" \
  -v migrator_password="$ICIBINA_MIGRATOR_PASSWORD" \
  -v reader_password="$ICIBINA_MCP_READER_PASSWORD" <<'EOSQL'
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='icibina_migrator') THEN
    CREATE ROLE icibina_migrator LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='icibina_app') THEN
    CREATE ROLE icibina_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='icibina_mcp_reader') THEN
    CREATE ROLE icibina_mcp_reader LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
  END IF;
END $$;

SELECT format('ALTER ROLE icibina_migrator PASSWORD %L', :'migrator_password') \gexec
SELECT format('ALTER ROLE icibina_app PASSWORD %L', :'app_password') \gexec
SELECT format('ALTER ROLE icibina_mcp_reader PASSWORD %L', :'reader_password') \gexec

REVOKE CREATE ON SCHEMA public FROM PUBLIC;
GRANT USAGE, CREATE ON SCHEMA public TO icibina_migrator;
GRANT USAGE ON SCHEMA public TO icibina_app;
REVOKE CREATE ON SCHEMA public FROM icibina_app;

ALTER DEFAULT PRIVILEGES FOR ROLE icibina_migrator IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO icibina_app;
ALTER DEFAULT PRIVILEGES FOR ROLE icibina_migrator IN SCHEMA public
  GRANT USAGE, SELECT ON SEQUENCES TO icibina_app;

CREATE SCHEMA IF NOT EXISTS agent_inspection AUTHORIZATION icibina_migrator;
REVOKE ALL ON SCHEMA agent_inspection FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM icibina_mcp_reader;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM icibina_mcp_reader;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM icibina_mcp_reader;
GRANT CONNECT ON DATABASE "ICIBINA" TO icibina_mcp_reader;
GRANT USAGE ON SCHEMA agent_inspection TO icibina_mcp_reader;
REVOKE CREATE ON SCHEMA agent_inspection FROM icibina_mcp_reader;

ALTER ROLE icibina_mcp_reader SET default_transaction_read_only = on;
ALTER ROLE icibina_mcp_reader SET statement_timeout = '15s';
ALTER ROLE icibina_mcp_reader SET idle_in_transaction_session_timeout = '15s';
ALTER ROLE icibina_mcp_reader CONNECTION LIMIT 3;
EOSQL

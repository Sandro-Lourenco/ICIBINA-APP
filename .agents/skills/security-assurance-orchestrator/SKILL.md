---
name: security-assurance-orchestrator
description: Orquestra segurança ICIBINA em mudanças sensíveis ou auditorias. Use para auth/authz, admin, pagamentos, uploads, secrets, MCP, release security review e incident hardening.
---
# Security Assurance Orchestrator

Leia `docs/contracts/SECURITY-CONTRACT.md`; para detalhes use docs/20, 41 ou 46 somente quando necessário.

- implementação: requisitos locais prevalecem; não importe exemplo genérico que quebre arquitetura.
- auditoria/release: use `security-reviewer` e registre findings/evidência.
- payments: combine com `$asaas-payments`, sem duplicar ownership.
- database/MCP: combine com `$database-persistence-orchestrator` somente se schema/role/query mudar.

Nunca trate ausência de scanner como PASS. Nunca execute teste destrutivo/ativo fora de escopo autorizado.

SMOKE_MARKER: `ICIBINA_SMOKE_SECURITY_ORCHESTRATOR_V5_8`

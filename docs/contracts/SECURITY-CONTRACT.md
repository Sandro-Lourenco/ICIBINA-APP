# SECURITY CONTRACT

Alvo: OWASP ASVS 5.0 Level 2 + threat model ICIBINA.

- AuthN/AuthZ, pagamentos, upload, secrets, admin e MCP são superfícies críticas.
- Role nunca substitui ownership/ABAC.
- Admin/super_admin: MFA obrigatório.
- Refresh token rotacionado, hash no DB, reuse detection e revogação de família.
- Sem secrets/PII em logs; least privilege e least data.
- PostgreSQL MCP não lê tabelas internas por padrão; somente `agent_inspection`.
- Security Reviewer é auditoria/milestone; implementação segue contratos locais primeiro.
- SAST/SCA/secret scan/container scan precisam de evidência no release gate.
- Nenhum teste ativo em produção sem autorização explícita.

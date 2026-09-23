# ADR-003 — Autenticação própria com sessões revogáveis

**Status:** Accepted

## Decision
Argon2id, access JWT curto e refresh token randômico com hash, rotation e family/replay detection. MFA obrigatório para admin/super_admin.

## Consequences
Maior controle e responsabilidade de segurança. Security baseline/ASVS e testes de sessão são obrigatórios.

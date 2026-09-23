# ADR-005 — Object Storage privado para mídia

**Status:** Accepted

## Decision
S3-compatible storage; MinIO local. Conteúdo pago privado, acesso por URL assinada curta; vídeo pesado evolui para HLS/CDN.

## Consequences
A API não deve ser proxy de grandes streams.

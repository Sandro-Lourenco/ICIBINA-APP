# ADR-004 — Asaas como gateway e webhook como fonte financeira

**Status:** Accepted

## Decision
Checkout/API Asaas via adapter. Browser não confirma pagamento. Webhook autenticado é persistido em inbox idempotente e aplicado por worker/state machine.

## Consequences
Eventual consistency explícita; exige reconciliação, retry e observabilidade.

---
name: asaas-payments
description: Regras obrigatórias para implementar ou revisar pagamentos Asaas, checkout, webhook, pedido, matrícula, refund e reconciliação nesta plataforma.
---

# Asaas Payments

## Non-negotiable

- API key somente no backend.
- Usar sandbox durante desenvolvimento/teste.
- Backend consulta preço no PostgreSQL.
- Pedido é criado antes do checkout e guarda snapshot.
- `order.id` deve ser usado como referência externa quando o endpoint permitir.
- Callback do browser nunca marca pedido pago.
- Webhook valida `asaas-access-token` com token próprio, não API key.
- `event.id` possui UNIQUE e handler é idempotente.
- Responder webhook 2xx rapidamente; trabalho pesado vai para job/outbox.
- Duplicata retorna sucesso sem duplicar side effects.
- Refund/chargeback atualizam acesso conforme política e geram audit/outbox.
- Reprocessamento admin usa evento persistido e exige permissão forte.
- Não logar payload sensível completo nem tokens.

## Checklist por PR

- evento duplicado testado;
- timeout Asaas testado;
- status fora de ordem considerado;
- matrícula duplicada impedida por constraint;
- checkout success page apenas consulta pedido;
- sandbox fixtures atualizadas;
- nenhum `VITE_ASAAS_*` secreto.

SMOKE_MARKER: `ICIBINA_SMOKE_ASAAS_PAYMENTS_V5_8`

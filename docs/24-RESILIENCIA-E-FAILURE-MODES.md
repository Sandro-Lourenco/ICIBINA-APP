# 24 — Resiliência e Failure Modes

## Princípio

Sistemas maduros são definidos pelo comportamento sob falha. Toda integração tem timeout, retry policy consciente, idempotência e observabilidade.

## Matriz principal

| Falha | Comportamento esperado | Retry | Estado/UX | Alerta |
|---|---|---|---|---|
| Asaas timeout ao criar checkout | não criar pedido duplicado; idempotency key | exponencial limitado | “não foi possível iniciar pagamento” | taxa alta |
| Webhook duplicado | `UNIQUE(provider,event_id)` | n/a | nenhum efeito duplicado | não |
| Webhook fora de ordem | state machine não rebaixa estado | reconciliação | estado consistente | divergência |
| Worker parado | inbox/outbox acumula | worker retoma | processamento pendente | queue age |
| Redis indisponível | degradar cache/rate limit conforme política; verdade no DB | reconectar | core continua quando seguro | sim |
| PostgreSQL indisponível | readiness falha; evitar writes parciais | pool/backoff | erro controlado | crítico |
| Storage indisponível | não perder metadado/job | retry | upload/processamento pendente | sim |
| Vídeo falha | job `failed` com retry budget | limitado | professor vê motivo/retry | após limite |
| Email fora | evento fica reprocessável | limitado/DLQ | ação principal não reverte | sim |
| Deploy incompatível | expand/contract evita quebra | rollback/roll-forward | canary interrompido | sim |

## Retry policy

Retry somente para falhas potencialmente transitórias:

```text
timeout
connection reset
429
5xx selecionados
```

Não retry automático para erro de validação/autorização/4xx permanente.

Use jitter e limite. Todo retry de write externo precisa de idempotency key/semântica segura.

## Circuit breaker

Não é obrigatório no MVP. Adotar apenas quando métricas mostrarem efeito cascata de provider externo. Timeout correto e bulkheads vêm primeiro.

## DLQ / Failed jobs

Job que excede tentativas:

- fica consultável no admin;
- preserva payload mínimo necessário e causa;
- tem ação segura de retry;
- gera audit event quando reprocessado manualmente;
- nunca oferece “executar SQL/shell” como correção.

## Disaster recovery

Definir por ambiente/provedor:

```text
RPO alvo
RTO alvo
backup frequency
retention
encryption
restore procedure
```

Backup só é considerado válido após restore drill periódico em ambiente isolado.

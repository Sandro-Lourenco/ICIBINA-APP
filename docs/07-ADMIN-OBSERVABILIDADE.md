# 07 — Admin, logs, manutenção e performance

## Separar dois tipos de log

### Audit log — PostgreSQL

Baixo/médio volume, retenção de negócio/segurança.

Exemplos:

- admin bloqueou usuário;
- professor publicou curso;
- role foi alterada;
- webhook foi reprocessado;
- manutenção foi ativada;
- refund administrativo foi solicitado.

### Application log — Loki/observability backend

Alto volume, estruturado em JSON:

```json
{
  "timestamp": "...",
  "level": "INFO",
  "service": "api",
  "request_id": "...",
  "route": "/api/v1/courses",
  "method": "GET",
  "status": 200,
  "duration_ms": 31
}
```

Não grave access token, refresh token, senha, Asaas API key, webhook token nem PII desnecessária.

## Correlation/request ID

Toda request recebe `X-Request-ID` gerado/validado pelo servidor.

Propagar para:

```text
log
trace
outbox/job
audit log
resposta HTTP
```

## Métricas

### API

- request count;
- p50/p95/p99;
- 4xx/5xx;
- requests in-flight;
- event loop lag quando aplicável.

### Banco

- pool in use/wait;
- active/idle connections;
- query latency;
- slow queries;
- lock waits;
- deadlocks;
- cache hit;
- autovacuum/bloat.

### Pagamentos

- checkouts criados;
- conversão por método;
- pedidos pending além do SLA;
- webhooks recebidos/processados/falhos/duplicados;
- refund/chargeback;
- reconciliações divergentes.

### Jobs

- queued;
- running;
- failed;
- retry count;
- oldest queued age;
- processing duration.

## Tracing

OpenTelemetry spans:

```text
HTTP request
  -> use case
     -> SQL
     -> Redis
     -> Asaas request
```

Nunca colocar secrets em span attributes.

## Admin Ops

O painel não deve ser um “terminal web”. Ele deve expor ações previamente definidas e seguras.

### Health card

```text
API        healthy
PostgreSQL healthy / latency 8 ms
Redis      healthy / latency 2 ms
Storage    healthy
Asaas      degraded? (última verificação)
Worker     healthy / heartbeat
```

Não faça chamada real ao Asaas em toda renderização do admin; use health checks com cache/intervalo.

### Maintenance mode

Tabela/configuração:

```text
maintenance.enabled
maintenance.message
maintenance.starts_at
maintenance.ends_at
maintenance.allow_admins
```

Middleware pode retornar `503` para operações específicas enquanto admin continua acessível.

Toda alteração exige `super_admin`, confirmação, motivo e audit log.

### Job retry

`POST /admin/ops/jobs/{id}/retry`

Requisitos:

- job está em estado retriável;
- limite de retries;
- idempotência;
- motivo/actor auditado.

### Webhook reprocess

Reprocessar o payload **já persistido**, não inventar um novo evento. O handler de negócio deve ser idempotente.

## Alertas

Criar alertas externos para:

- 5xx acima do limite;
- p95 alto sustentado;
- DB pool saturado;
- disk/storage critical;
- worker sem heartbeat;
- fila crescendo;
- webhook failure spike;
- muitos pagamentos pending;
- migração falhou.

## Segurança do painel de operações

- `admin` para visualização de algumas telas;
- `super_admin` para ações destrutivas/operacionais;
- MFA obrigatório recomendado;
- reautenticação para ações financeiras/irreversíveis;
- rate limit;
- audit log imutável do ponto de vista da aplicação.

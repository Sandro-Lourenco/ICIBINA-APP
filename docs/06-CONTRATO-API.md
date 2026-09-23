# 06 — Contrato API v1

Prefixo:

```text
/api/v1
```

## Envelope de erro

```json
{
  "error": {
    "code": "COURSE_NOT_FOUND",
    "message": "Curso não encontrado.",
    "details": null,
    "request_id": "..."
  }
}
```

Codes são estáveis; mensagem pode mudar/traduzir.

## Auth

```text
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout
POST /auth/logout-all
GET  /auth/me
POST /auth/forgot-password
POST /auth/reset-password
POST /auth/verify-email
```

### Login

```json
{
  "email": "aluno@example.com",
  "password": "..."
}
```

Resposta não precisa expor refresh token se estiver em cookie HttpOnly.

## Público

```text
GET /courses
GET /courses/{slug}
GET /teachers/{slug}
GET /categories
GET /certificates/verify/{code}
```

## Aluno

```text
GET  /student/dashboard
GET  /student/courses
GET  /student/courses/{course_id}
GET  /student/courses/{course_id}/lessons/{lesson_id}
PUT  /student/lessons/{lesson_id}/progress
POST /student/assessments/{assessment_id}/attempts
POST /student/attempts/{attempt_id}/answers
POST /student/attempts/{attempt_id}/submit
GET  /student/certificates
GET  /student/orders
GET  /student/orders/{order_id}
```

## Professor

```text
GET    /teacher/dashboard
GET    /teacher/courses
POST   /teacher/courses
GET    /teacher/courses/{id}
PATCH  /teacher/courses/{id}
DELETE /teacher/courses/{id}
POST   /teacher/courses/{id}/publish
POST   /teacher/courses/{id}/archive
POST   /teacher/courses/{id}/modules
PATCH  /teacher/modules/{id}
POST   /teacher/modules/{id}/lessons
PATCH  /teacher/lessons/{id}
POST   /teacher/courses/{id}/reorder
POST   /teacher/media/upload-url
GET    /teacher/media/jobs/{id}
GET    /teacher/courses/{id}/students
GET    /teacher/courses/{id}/analytics
```

Todas as rotas que recebem IDs precisam revalidar ownership no backend.

## Pagamentos

```text
POST /payments/checkout
GET  /orders/{order_id}
POST /webhooks/asaas                 # público tecnicamente, autenticado por webhook token
```

### Criar checkout

```json
POST /payments/checkout
{
  "course_id": "uuid"
}
```

Resposta:

```json
{
  "order_id": "uuid",
  "status": "pending",
  "checkout_url": "https://asaas.com/checkoutSession/show?id=..."
}
```

## Admin — negócio

```text
GET   /admin/users
GET   /admin/users/{id}
PATCH /admin/users/{id}/status
PUT   /admin/users/{id}/roles
GET   /admin/teachers
GET   /admin/courses
POST  /admin/courses/{id}/moderation
GET   /admin/orders
GET   /admin/payments
GET   /admin/webhooks
POST  /admin/webhooks/{event_id}/reprocess
GET   /admin/audit-logs
```

## Admin — operações

```text
GET  /admin/ops/health
GET  /admin/ops/metrics/summary
GET  /admin/ops/database
GET  /admin/ops/jobs
POST /admin/ops/jobs/{id}/retry
GET  /admin/ops/releases
GET  /admin/ops/maintenance
POST /admin/ops/maintenance
```

Evite criar um endpoint admin que execute SQL arbitrário, shell ou comando livre.

## Health público/infra

```text
GET /health/live
GET /health/ready
```

`live` confirma que o processo responde. `ready` confirma que dependências essenciais permitem tráfego.

Não retornar credenciais, DSN ou stack traces.

## Paginação

Para listas simples administrativas, offset/limit pode ser suficiente inicialmente. Para eventos/logs de alto volume, prefira cursor:

```json
{
  "items": [],
  "next_cursor": "opaque-token",
  "has_more": true
}
```

## Concorrência

Rotas de edição podem usar:

```http
If-Match: "version-12"
```

ou `version` no body. Conflito retorna `409`.

## OpenAPI

OpenAPI gerado pelo FastAPI é parte do contrato. CI deve detectar breaking changes intencionais e regenerar client types quando necessário.


## Extensões de medicina integrativa

Credenciais verificadas, referências, disclosures, revisão científica/editorial e créditos educacionais seguem `docs/28-EXTENSOES-DOMINIO-MEDICINA-INTEGRATIVA.md`. O OpenAPI implementado permanece a fonte executável; quando estes endpoints forem entregues, atualizar contract tests e tipos gerados do frontend.


## OpenAPI compatibility gate

O backend real exporta `backend/openapi.json` por `backend/scripts/export_openapi.py`. Release compara o documento com `contracts/openapi/baseline.json` usando a imagem imutável de oasdiff registrada em `release-images-lock.json`; breaking changes exigem decisão explícita de versionamento/ADR antes de atualizar a baseline.


## Conteúdo com risco de identificação de paciente

Endpoints futuros de notas, casos e uploads devem aplicar `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md`. Em bloqueio, retornar `PATIENT_IDENTIFIABLE_DATA_PROHIBITED` sem repetir o conteúdo sensível no erro/log.

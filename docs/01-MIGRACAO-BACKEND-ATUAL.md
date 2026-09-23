# 01 — Migração do backend atual

## Objetivo

O backend existente tem uma boa separação `domain/application/infrastructure/interface` em vários módulos. Preserve isso. A mudança principal será **infraestrutura**.

## O que permanece

Preservar sempre que os testes confirmarem comportamento:

- entidades e regras de `domain`;
- casos de uso em `application`;
- schemas de resposta que façam sentido para o novo contrato;
- regras de ownership/BOLA;
- testes de segurança;
- completion/progresso;
- avaliações;
- certificados;
- worker de vídeo, substituindo integrações necessárias;
- abstrações de storage;
- estrutura de erros e error handlers;
- versionamento `/api/v1`.

## O que sai/substitui

| Atual | Destino |
|---|---|
| `src/infra/supabase/*` | SQLAlchemy repositories + PostgreSQL |
| Supabase Auth | Auth própria PostgreSQL/JWT/refresh sessions |
| Supabase Storage | S3 compatible adapter |
| Supabase RPCs | services/repositories + transações SQL explícitas |
| Stripe | Asaas gateway |
| chamadas sync em async | drivers/clientes async |
| rotas legacy/deprecated | somente `/api/v1` |
| branding Lawrence | configurações genéricas |

## Mapa por pasta atual

### `src/main.py`

Refatorar para app factory:

```python
def create_app() -> FastAPI:
    app = FastAPI(...)
    install_middlewares(app)
    install_exception_handlers(app)
    install_routes(app)
    return app
```

Remover routers legacy. Manter `/docs` desligável em produção se desejado. Readiness deve verificar PostgreSQL/Redis/serviços essenciais — não Supabase.

### `src/shared/config.py`

Manter a ideia de settings validados, mas substituir:

```text
SUPABASE_*
STRIPE_*
```

por:

```text
DATABASE_URL
REDIS_URL
ASAAS_BASE_URL
ASAAS_API_KEY
ASAAS_WEBHOOK_TOKEN
JWT_PRIVATE/SECRET
FRONTEND_URL
STORAGE_*
```

Preservar as validações rígidas de produção.

### `src/core/security/security.py`

A responsabilidade continua, porém sem `supabase.auth.get_user`.

Criar:

```text
core/security/passwords.py
core/security/tokens.py
core/security/session.py
modules/auth/infrastructure/sqlalchemy_auth_repository.py
```

### `src/core/concurrency/sync_io.py`

Após SQLAlchemy async + httpx async, essa camada deixa de ser necessária na maior parte do código. Mantenha somente para bibliotecas inevitavelmente síncronas, nunca como solução padrão.

### `src/infra/stripe/`

Remover depois que a implementação Asaas e testes substitutos estiverem verdes.

Nova estrutura:

```text
src/infra/asaas/
├─ client.py
├─ schemas.py
├─ webhook.py
└─ errors.py
```

ou, preferencialmente, dentro do bounded context:

```text
src/modules/payments/infrastructure/asaas/
```

## Migração repository-by-repository

Não faça Big Bang.

Para cada módulo:

1. identifique a interface/port do repository;
2. escreva testes contratuais para essa interface;
3. implemente repository SQLAlchemy;
4. execute testes unitários + integração;
5. altere DI para usar SQLAlchemy;
6. só então remova o adapter Supabase daquele módulo.

### Ordem recomendada

```text
identity/auth
profiles
courses
authoring/modules/lessons
enrollments/progress
assessments
payments
certificates
reviews
sync/lives/media
```

## RPCs Supabase

O backend antigo delega regras a funções SQL/RPC. Antes de remover Supabase, cada RPC deve ser classificada:

- regra de negócio -> application service/use case;
- garantia atômica -> transação PostgreSQL;
- lock/concorrência -> `SELECT ... FOR UPDATE`, optimistic locking ou constraint;
- processamento assíncrono -> job/outbox.

Exemplos encontrados anteriormente incluem publicação de curso, reordenação de blocos, progresso e claim de job. Não replique RPC por RPC cegamente; preserve a **invariante**, não a tecnologia.

## Optimistic locking

Para edição de conteúdo do professor, adicione `version INTEGER NOT NULL DEFAULT 1` em agregados sensíveis.

Atualização:

```sql
UPDATE courses
SET title = :title, version = version + 1
WHERE id = :id AND version = :expected_version;
```

Se `rowcount = 0`, retorne `409 Conflict`.

## Regras para o agente

- nenhuma deleção do código antigo sem teste substituto;
- não alterar contrato externo e persistence no mesmo commit se puder separar;
- commits pequenos por bounded context;
- não misturar SQLAlchemy models com entidades de domínio;
- toda migration Alembic deve ter downgrade viável ou justificativa explícita;
- nunca editar banco manualmente como solução permanente;
- remover `.venv`, caches, `lost_blobs`, temporários e artefatos do repositório.

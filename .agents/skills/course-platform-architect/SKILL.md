---
name: course-platform-architect
description: Revise ou implemente mudanças que alterem fronteiras de módulos, ports/adapters, transações, autenticação ou a migração do backend legado.
---

# Course Platform Architect

## Princípios obrigatórios

1. Preserve separação `domain -> application` e adapters em `infrastructure`.
2. PostgreSQL é a fonte transacional. Toda mudança de schema usa Alembic.
3. React nunca acessa banco, Asaas ou secret diretamente.
4. Preço e autorização são decididos pelo backend.
5. Pagamento só libera matrícula após estado financeiro confiável processado por webhook idempotente.
6. Callback/success URL do checkout não é prova de pagamento.
7. `student`, `teacher`, `admin`, `super_admin` usam RBAC; ownership é verificado separadamente.
8. Não executar I/O síncrono em `async def` sem isolamento explícito.
9. Dinheiro é inteiro em centavos.
10. Eventos externos e jobs precisam de idempotência, retry limitado e observabilidade.
11. Audit logs e app logs são sistemas diferentes.
12. Não criar terminal/SQL arbitrário no painel admin.

## Antes de editar

- ler `docs/00-ARQUITETURA.md`;
- localizar interface/port existente;
- identificar testes atuais;
- propor a menor mudança vertical possível.

## Ao migrar backend legado

Não remover adapter Supabase/Stripe antes do adapter PostgreSQL/Asaas equivalente passar testes. Preserve regra de negócio, não tecnologia legada.

SMOKE_MARKER: `ICIBINA_SMOKE_COURSE_PLATFORM_ARCHITECT_V5_8`

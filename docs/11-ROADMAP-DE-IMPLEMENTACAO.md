# 11 — Roadmap executável

## Fase 0 — Preservação

Critério de saída:

- backend antigo tagueado/backup;
- testes atuais registrados;
- `.venv`, caches e temporários fora do repositório;
- lista de endpoints e invariantes congelada.

## Fase 0.5 — Baselines antes da UI massiva

- adotar ADR-001..010;
- ativar CI `quality-gates.yml`;
- validar architecture check;
- persistir/aceitar design system `integrative-medicine`;
- fechar rendering público/SEO;
- definir threat model + ASVS L2 tracking;
- definir capacity worksheet inicial;
- registrar o gate de bootstrap frontend: Tailwind/aliases/shadcn `components.json`/tokens antes do primeiro intake 21st.

**Gate:** agentes não iniciam dezenas de telas antes destes contratos estarem aceitos.

## Fase 1 — Fundação PostgreSQL

Entregas:

- SQLAlchemy async;
- asyncpg;
- Alembic;
- PostgreSQL Docker;
- session/transaction dependency;
- health DB;
- primeiro repository contratual.

Gate: uma feature pequena usando PostgreSQL real passa integração.

## Fase 2 — Identidade

- users/profiles;
- Argon2id;
- JWT access;
- refresh rotation;
- roles/permissions;
- password reset;
- session revoke;
- testes BOLA/RBAC.

Gate: aluno/professor/admin autenticam sem Supabase.

## Fase 3 — Cursos e autoria

- migrar courses/modules/lessons;
- ownership;
- optimistic locking;
- publish state machine;
- media metadata.

Gate: professor cria, edita e publica; outro professor recebe 403/404 conforme policy.

## Fase 4 — Aprendizagem

- enrollment;
- lesson progress;
- assessments;
- completion;
- certificates.

Gate: fluxo aluno completo sem pagamento ainda.

## Fase 5 — Asaas

- customer mapping;
- orders/order_items snapshot;
- checkout;
- webhook token;
- idempotency;
- enrollment após pagamento;
- reverse events;
- reconciliação;
- admin financeiro.

Gate: sandbox cobre PIX/cartão escolhidos e evento duplicado não duplica matrícula.

## Fase 6 — Frontend público + auth

- criar frontend real com package.json + package-lock;
- executar bootstrap shadcn pinado e revisar `components.json`;
- conectar tokens ICIBINA à primitive layer antes do primeiro intake 21st;
- design system;
- layout;
- landing/catalog/course;
- login/cadastro;
- query client;
- error boundary;
- route guards UX.

## Fase 7 — Área do aluno

- dashboard;
- cursos;
- player;
- progresso;
- avaliações;
- certificados;
- compras.

## Fase 8 — Professor

- dashboard;
- builder;
- upload;
- reorder;
- publish;
- alunos;
- analytics.

## Fase 9 — Admin/observabilidade

- users/roles;
- courses/moderação;
- financeiro;
- webhook inbox;
- audit log;
- jobs;
- ops health;
- metrics;
- maintenance mode.

## Fase 10 — Hardening

- security tests;
- rate limit;
- CSP/CORS;
- secret scan;
- load tests;
- backup restore drill;
- observability alerts;
- E2E completo;
- forced-colors / Windows High Contrast smoke nas rotas críticas;
- prefers-contrast enhancement quando aplicável.

## Fase 11 — Corte final do legado

Somente após todos os módulos usarem PostgreSQL/Asaas:

- remover Supabase deps;
- remover Stripe deps;
- remover routers legacy;
- remover hardcodes de branding;
- remover `sync_io` não utilizado;
- atualizar README/OpenAPI;
- congelar template `platform-base-v1`.

## Regra para o agente

Nunca avançar uma fase com testes quebrados por regressão conhecida. Se um teste legado for inválido no novo produto, substituí-lo por teste equivalente documentando o motivo; não simplesmente deletar.

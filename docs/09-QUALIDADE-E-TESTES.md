# 09 — Qualidade, testes e Definition of Done

> Os thresholds normativos e gates executáveis ficam em `docs/21-QUALITY-GATES.md`. Este documento descreve a estratégia de testes.

## Backend gates

Toda alteração deve passar:

```bash
ruff check .
ruff format --check .
mypy src                 # ou checker adotado no projeto
pytest -q
```

Além de:

- migrations testadas em DB limpo;
- upgrade da versão anterior;
- testes de integração PostgreSQL real em CI (container), não SQLite substituto;
- OpenAPI válido.

## Frontend gates

```bash
npm run lint
npm run typecheck
npm run test
npm run build
npm run test:e2e
```

## Pirâmide

### Unitários

- regras de curso;
- cálculo/snapshot de pedido;
- state machines;
- permission policies;
- mappers.

### Integração

- repositories PostgreSQL;
- transações;
- auth sessions;
- webhook handler com eventos fixtures;
- storage adapter fake/local.

### Contrato Asaas

Não chamar produção em testes.

- fixtures para payloads;
- mock server para erro/timeout/429/5xx;
- smoke tests explícitos contra sandbox em pipeline separado/manual;
- teste de evento duplicado;
- evento fora de ordem;
- refund após enrollment;
- webhook inválido.

### E2E

Playwright:

```text
cadastro/login
catálogo -> checkout fake/sandbox
aluno abre curso
professor cria curso
professor não edita curso alheio
admin altera role
admin vê webhook falho
logout/revogação
```

## Security regressions

Preserve os testes BOLA existentes e amplie:

```text
student A vs student B
teacher A vs course teacher B
admin vs super_admin
expired/revoked session
price tampering
webhook spoof
webhook duplicate
path traversal/upload
open redirect
```

## Performance budgets

Defina objetivos de produto, por exemplo:

```text
API p95 reads simples < 300 ms em staging representativo
5xx < 0.5% em steady state
LCP público <= 2.5 s no p75
INP <= 200 ms no p75
CLS <= 0.1 no p75
```

Esses números são SLOs iniciais a validar, não garantias automáticas.

Use k6/Locust para cenários:

- catálogo;
- lesson progress burst;
- login;
- admin list;
- webhook burst.

Nunca load-test Asaas diretamente sem política/autorização; simule o provider no teste de carga da sua API.

## Code review

Rejeitar PR que:

- confia em preço do frontend;
- executa SQL em router;
- retorna ORM diretamente sem schema;
- faz request externo dentro de transação longa;
- captura `Exception` e ignora;
- loga secrets;
- adiciona dependência sem motivo;
- cria duplicação grande para “andar mais rápido”;
- remove teste por estar falhando sem explicar regressão.

## Definition of Done

Feature concluída somente quando possui:

```text
regra implementada
autorização testada
schema/migration quando necessário
logging/metric relevante
loading/error/empty frontend
a11y básica
testes adequados
documentação do contrato
sem secret hardcoded
quality gates verdes
```

## Reprodutibilidade e supply chain

- commit do lockfile é obrigatório (`package-lock.json`/equivalente e lock Python escolhido);
- CI usa instalação reproduzível (`npm ci` ou equivalente);
- versões `latest` não ficam como dependência resolvida do projeto;
- secret scan + dependency/SCA scan no CI;
- dependência nova exige origem/licença/motivo;
- auth, pagamento e migration destrutiva exigem revisão humana antes de produção.

## Gate de diff para agentes

Antes do handoff:

```text
git status
git diff --check
git diff --stat
revisão do diff por escopo
```

Rejeite alterações não relacionadas, arquivos gerados por engano, segredos, snapshots enormes e formatação massiva não solicitada.


## Architecture + visual/a11y gates

- `python scripts/check_architecture.py`;
- Playwright screenshot regression para rotas críticas;
- axe automation para WCAG 2.2 AA;
- contract tests de repositories/gateways;
- coverage baseline conforme `docs/21-QUALITY-GATES.md`.

# 22 — PostgreSQL Migration & Data Change Policy

## 1. Fonte de verdade

Alembic é a única fonte de DDL aplicada pela aplicação. `database/*.sql` neste blueprint é referência de projeto/bootstrapping, não um canal paralelo de produção.

## 2. Expand / migrate / contract

Mudança incompatível é dividida:

```text
EXPAND
  adicionar estrutura compatível
MIGRATE
  backfill/dual read-write quando necessário
CONTRACT
  remover legado somente após adoção completa
```

Nunca depender de deploy simultâneo perfeito entre frontend/backend/database.

## 3. Regras de lock

Evitar migration que mantenha lock longo em tabela de alto tráfego.

Antes de alteração relevante documentar:

```text
tabela
linhas estimadas
lock esperado
runtime estimado
rollback
janela/canary
```

Índices grandes em produção devem usar estratégia online/`CONCURRENTLY` quando tecnicamente compatível com a ferramenta/versão e com transações do Alembic.

## 4. NOT NULL e defaults

Para coluna nova em tabela grande:

1. adicionar nullable/sem operação pesada quando necessário;
2. deploy compatível;
3. backfill em lotes;
4. validar invariantes;
5. aplicar constraint;
6. remover compatibilidade temporária depois.

## 5. Backfill

Backfill grande:

- job explícito e reiniciável;
- lotes limitados;
- checkpoint;
- métricas;
- idempotência;
- capacidade de pausar;
- nunca segurar uma transação gigantesca.

## 6. Timeouts

Produção precisa de limites conscientes para:

```text
statement_timeout
lock_timeout
idle_in_transaction_session_timeout
```

Valores exatos dependem do provedor/workload e ficam em configuração operacional, não hardcoded na regra de domínio.

## 7. Testes obrigatórios

CI para schema alterado:

```text
DB vazio -> upgrade head -> integration smoke
versão anterior -> upgrade head -> integration smoke
```

Quando downgrade for seguro/suportado, testá-lo. Quando não for, documentar recuperação roll-forward.

## 8. Dados financeiros e auditoria

Backfill/migration que altera:

```text
orders
payments
enrollments
audit_logs
```

exige script de verificação antes/depois com contagens, totais e invariantes.

## 9. Destructive change

Drop/rename destrutivo exige:

- evidência de zero uso;
- release anterior compatível;
- backup/restore válido;
- aprovação humana;
- plano de rollback ou roll-forward.

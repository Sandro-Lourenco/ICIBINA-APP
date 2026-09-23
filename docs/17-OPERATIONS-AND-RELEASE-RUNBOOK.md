# 17 — Runbook de operação e release

## Objetivos operacionais

Antes de produção, definir metas verificáveis de disponibilidade, latência, recuperação e retenção. Valores abaixo são ponto de partida e precisam ser aprovados pelo negócio:

```text
API availability SLO: 99.9% mensal
API p95 leitura comum: < 300 ms em staging representativo
RPO banco: <= 15 min quando PITR estiver disponível
RTO inicial: <= 2 h
```

## Pre-release

- branch protegida e CI verde;
- lockfiles presentes;
- migration testada em DB vazio e upgrade de N-1;
- backup/PITR operacional;
- `alembic upgrade head` em job único;
- feature flags para mudança de alto risco;
- dashboard/alertas essenciais criados;
- smoke test documentado;
- rollback de código compatível com schema expandido.

## Security gates

- secret scan;
- dependency/SCA scan;
- SAST quando disponível;
- container/image scan;
- revisão humana obrigatória para auth, autorização, pagamentos e migrations destrutivas.

## Incident basics

Em incidente:

1. reduzir impacto (feature flag/maintenance mode/rollback seguro);
2. preservar evidência e request IDs;
3. não editar dados diretamente sem script/runbook revisado;
4. registrar timeline;
5. reconciliar pagamento/matrícula após restauração;
6. criar ação corretiva e teste regressivo.

## Restore drill

Backup só é considerado confiável após restauração em ambiente isolado e smoke test. Faça drills periódicos e registre duração/resultado.

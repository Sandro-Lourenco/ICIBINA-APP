# Capacity & load test plan

Nenhum número de capacidade é afirmado sem teste.

## Perfis

### Launch
Definir usuários concorrentes iniciais, RPS de catálogo/player, checkout/min, webhook burst e jobs/min com base no lançamento real.

### Growth
2–5x Launch com distribuição de tráfego realista e crescimento de dados.

### Stress
Aumentar carga até violar um SLO; objetivo é descobrir gargalo e comportamento de degradação, não “provar infinito”.

## Cenários k6

- catálogo/listagem;
- login/refresh (sem brute force);
- lesson metadata/progress;
- dashboard aluno/professor;
- checkout creation com gateway mock/sandbox controlado;
- webhook burst em harness seguro;
- admin observability endpoints.

Medir p50/p95/p99, error rate, throughput, DB pool wait, query p95, CPU/memory, queue age e saturation. Registrar dataset, ambiente e commit.

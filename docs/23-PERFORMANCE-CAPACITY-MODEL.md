# 23 — Performance e Capacity Model

## 1. Objetivo

A arquitetura é escalável, mas capacidade só é afirmada após medição. Este documento define o modelo e os budgets que devem ser preenchidos com dados reais.

## 2. Web Vitals

Para páginas públicas no percentil 75, segmentado por mobile/desktop:

```text
LCP <= 2.5 s
INP <= 200 ms
CLS <= 0.1
```

Medir laboratório + RUM. Lighthouse sozinho não comprova produção.

## 3. API SLO inicial

Metas de partida, a validar com workload real:

```text
simple cached reads p95 < 200 ms
simple DB reads p95 < 300 ms
writes comuns p95 < 500 ms
5xx < 0.5% steady state
availability alvo inicial >= 99.9% para API principal
```

Não transformar números de blueprint em promessa contratual sem dados.

## 4. Database budgets

Monitorar:

```text
query p50/p95/p99
pool wait p95
active/idle connections
lock wait/deadlock
cache hit
rows scanned/returned
temp files
replication lag se houver
```

Query crítica repetida com p95 > budget exige análise com `EXPLAIN (ANALYZE, BUFFERS)`.

## 5. Async/jobs

Monitorar:

```text
queue depth
oldest job age
job runtime p95
retry count
DLQ/failed jobs
webhook receive-to-apply latency
video processing throughput
```

## 6. Capacity baseline executável

A fonte de evidência é `capacity-baseline.json`. O blueprint começa com `status=unverified`; isso **não é uma promessa de escala**. Antes de produção, `python scripts/check-capacity-baseline.py --strict` precisa passar com medições reais para MAU, pico de sessões concorrentes, API/write RPS, webhook burst, jobs/min, ingestão de vídeo e tamanho de banco, mais artefatos de evidência.

Regras:

- `launch_expected` vem do plano de negócio/lançamento, não de palpite do agente;
- `tested_limit` vem de load test reproduzível no commit indicado;
- documentar ambiente/dataset;
- margem alvo é decidida por risco/SLO e registrada no relatório, não hardcoded como capacidade “garantida”.

Estado atual do blueprint: **UNVERIFIED / PENDING até medição**.

## 7. Cenários de load test

1. login e refresh;
2. catálogo + course detail;
3. abrir aula/progresso;
4. burst de progress events;
5. checkout criado contra provider mock;
6. webhook burst com duplicatas/out-of-order;
7. professor publica curso;
8. admin filtra pagamentos/auditoria;
9. jobs de vídeo em paralelo.

## 8. Frontend budgets

Alvos iniciais por rota pública:

```text
JS inicial comprimido: manter mínimo; budget concreto definido após primeiro build
hero image: responsiva, AVIF/WebP, dimensions reservadas
nenhum chart/editor pesado no bundle público
route-level code splitting obrigatório
```

O CI deve congelar um baseline de bundle após a primeira implementação e bloquear regressões percentuais relevantes.

## 9. Escala horizontal

API deve ser stateless entre requests. Sessões, cache compartilhado e coordenação ficam em PostgreSQL/Redis conforme ADR. Workers são escalados separadamente.

Vídeo em produção deve usar object storage + CDN/signed playback quando o tráfego justificar; a API não faz proxy de grandes streams.

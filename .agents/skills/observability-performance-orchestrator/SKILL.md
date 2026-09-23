---
name: observability-performance-orchestrator
description: Orquestra observabilidade, profiling, capacity e load testing ICIBINA. Use para OTel, Prometheus, Grafana, Loki, Tempo, k6, SLOs ou performance/capacity work.
---
# Observability & Performance Orchestrator

Leia `docs/contracts/OBSERVABILITY-CONTRACT.md` e apenas o fluxo medido.

- OTel/instrumentação: skill `opentelemetry` quando instalada.
- Prometheus/Loki/Tempo: skill oficial correspondente do Grafana.
- load tests: skill `k6` e cenários de docs/47.
- tuning SQL: encaminhe para database orchestrator + postgres/sql specialist.

Não otimize sem baseline. Não crie labels de alta cardinalidade. Relate ambiente, carga, p50/p95/p99, error rate e gargalo observado.

SMOKE_MARKER: `ICIBINA_SMOKE_OBSERVABILITY_ORCHESTRATOR_V5_8`

# OBSERVABILITY / PERFORMANCE CONTRACT

- Instrumentação padrão: OpenTelemetry; métricas Prometheus; dashboards Grafana; logs Loki; traces Tempo.
- Correlation/request ID obrigatório nos fluxos críticos.
- Nunca use PII/user_id como label de alta cardinalidade.
- Métricas devem ter owner, unidade, labels limitadas e propósito.
- Load tests usam k6 e cenários descritos em docs/47; sem números inventados.
- Performance claim exige baseline antes/depois e ambiente descrito.
- Use skills Grafana/OTel/k6 apenas nesta classe de tarefa.

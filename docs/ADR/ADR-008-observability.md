# ADR-008 — OpenTelemetry + métricas/logs centralizados

**Status:** Accepted

## Decision
Trace/metrics/log correlation com OpenTelemetry, Prometheus/Grafana e Loki; Sentry opcional. Audit log é separado de application log.

## Consequences
Requer IDs de correlação, redaction e budgets de retenção.

# ADR-007 — Renderização pública HTML-first, dashboards SPA

**Status:** Accepted (principle)

## Decision
Landing, catálogo, curso e professor devem entregar conteúdo essencial no HTML inicial por SSR/SSG/prerender React/Vite. Dashboards autenticados permanecem client-rendered e lazy-loaded.

## Consequences
Build/deploy público fica um pouco mais complexo, mas melhora crawling, compartilhamento e desempenho percebido. A biblioteca de rendering concreta deve obedecer este contrato.

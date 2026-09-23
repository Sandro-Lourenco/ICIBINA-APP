---
name: qa-test-orchestrator
description: Orquestra testes e QA da ICIBINA. Use para test strategy, cobertura, integration/E2E, visual regression, flaky tests ou regressões; não para cada edição trivial.
---
# QA Test Orchestrator

Leia `docs/contracts/QA-CONTRACT.md` e o código/testes afetados.

## Roteamento
- teste unit/integration comum: use padrões locais; especialista externo só se houver complexidade.
- estratégia ampla/coverage/test architecture/performance/security testing: `test-master`.
- Playwright/E2E/visual/flaky browser: `playwright-expert`.
- acessibilidade automatizada: frontend orchestrator + skill de web accessibility + axe/Playwright.

## Saída
Defina risco, camada de teste mínima suficiente, dados/fixtures, comando executado e evidência. Não aumente escopo para testar o mundo inteiro.

SMOKE_MARKER: `ICIBINA_SMOKE_QA_ORCHESTRATOR_V5_8`

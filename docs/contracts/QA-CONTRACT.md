# QA CONTRACT

Use para testes, cobertura, E2E, regressão, flaky tests e estratégia de qualidade.

- Teste comportamento observável, happy path + erros + boundaries.
- Unit não chama rede/DB real; integration usa PostgreSQL real/isolado quando necessário.
- E2E cobre jornadas críticas, não cada detalhe de UI.
- Não aceite retry como solução de flaky test sem causa raiz.
- Bugs graves recebem teste regressivo.
- Release exige os scripts obrigatórios; ausência de script é FAIL, não SKIP.
- Use `test-master` para estratégia ampla; `playwright-expert` para browser/E2E/visual.
- Handoff usa `$platform-quality-gate`; não recarregue todas as skills para revisar.

- Frontend crítico inclui smoke de `forced-colors`/Windows High Contrast e validação de `prefers-contrast` quando suportado.

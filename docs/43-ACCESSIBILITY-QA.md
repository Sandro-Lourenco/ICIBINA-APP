# Accessibility QA — WCAG 2.2 AA

## Baseline

- semantic HTML primeiro;
- teclado completo e foco visível;
- accessible name para controles;
- contraste: 4.5:1 texto normal e 3:1 UI/focus quando aplicável;
- cor nunca é único sinal;
- conteúdo dinâmico com live regions apropriadas;
- reduced motion;
- zoom/reflow e target size avaliados.

## Ferramentas

- skill `web-accessibility-web-accessibility` para contrato semântico/interativo;
- Testing Library por role/label;
- Playwright para jornadas de teclado/foco;
- `@axe-core/playwright` para automação;
- auditoria manual de teclado e, antes de release importante, smoke com leitor de tela em fluxos críticos.

Automação não substitui revisão manual. Ausência de violações do axe não equivale a WCAG completo.


## High Contrast / forced colors — V5.7

Além do axe/teclado/zoom/reduced-motion, rotas críticas devem ter smoke manual ou automatizado em `forced-colors: active` quando o ambiente de browser suportar emulação adequada, com validação real em Windows High Contrast antes de releases relevantes. Verificar especialmente foco, seleção, bordas, botões, inputs, status, progress, gráficos e texto sobre imagem.

`prefers-contrast: more` entra como enhancement: respeitar a preferência quando disponível, sem criar uma segunda identidade visual ou depender exclusivamente dela para acessibilidade.

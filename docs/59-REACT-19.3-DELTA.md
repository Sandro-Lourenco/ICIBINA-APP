# 59 — React 19.3 delta para a skill React externa

## Autoridade de versão

O projeto usa **React 19.3**. A skill React externa revisada ainda declara baseline 19.2; ela continua útil para composição, hooks, forms, estados e Tailwind, mas **não é autoridade para comportamento específico de versão**.

Fonte oficial prevalente: https://react.dev/blog/2026/09/09/react-19-3

## Diferenças relevantes

React 19.3 tornou estáveis, entre outras mudanças:

- `<ViewTransition>` para transições DOM de enter/exit/update/share;
- Fragment refs (`<Fragment ref={...}>`) para operar sobre grupos de nós sem wrapper artificial;
- `browser()` em `react-dom`, usado com `use(browser())` para componentes que precisam optar por não renderizar no servidor;
- suporte a Trusted Types no React DOM;
- renderização direta de `<Context>` em React Server Components conforme documentação oficial.

## ViewTransition × Motion

Use a menor ferramenta adequada:

- React `<ViewTransition>`: transições DOM/navegação/layout quando o comportamento nativo satisfaz a UX;
- CSS: hover, focus, opacity e transições simples;
- Motion: drag/reorder, gestures, springs, shared layout complexo, stagger e orquestração que React/CSS não resolvam bem.

Não duplique a mesma animação em `<ViewTransition>` e Motion. Sempre respeite `prefers-reduced-motion` e o design system.

## Regra para agentes

Quando a skill React disser algo que conflite com React 19.3, consulte primeiro a documentação oficial. Registre a divergência no handoff se ela alterar a implementação.

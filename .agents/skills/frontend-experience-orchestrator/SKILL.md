---
name: frontend-experience-orchestrator
description: Coordena UI React da ICIBINA e roteia progressivamente UI/UX Pro Max, 21st.dev, Motion e acessibilidade para produzir interfaces bonitas, consistentes, performáticas e contextualizadas sem inflar o contexto.
---

# Frontend Experience Orchestrator — V5.8

## Contexto inicial mínimo

1. Leia `docs/contracts/FRONTEND-CONTRACT.md`.
2. Leia `design-system/integrative-medicine/pages/<page>.md` se existir.
3. Inspecione rota, primitives e código afetados.
4. Carregue foundations/especialistas somente conforme os gatilhos abaixo.

## Primeiro: classifique a superfície

```text
Editorial Light
Student Immersive
Operational Light
Operational Neutral
```

Se não souber, consulte `SURFACES.md`; não invente um quarto sistema visual.

## Roteamento progressivo

### React
Escrever/alterar componentes, hooks, state/forms/performance -> skill `react`.

### UI/UX Pro Max
Obrigatório em **nova página, redesign, nova superfície ou mudança importante de hierarchy/interaction**. Use `python scripts/uiux-pro-max.py ...` e os dials do `UIUX-PRO-MAX-RECIPES.md`; nunca dependa de `CLAUDE_PLUGIN_ROOT`. Para bug visual simples, use apenas domínio targeted quando necessário.

### 21st.dev
- primitive local existe -> reutilize;
- padrão genérico inexistente -> `21st search` / `21st-ui-build`;
- direção aberta e usuário quer alternativas -> `21st-ui-explore`;
- página/fluxo substancial pronto -> `21st-ui-review`.

Não carregue Explore+Build+Review ao mesmo tempo por padrão; avance por etapa.

### Motion
- Tier 0 simples -> CSS;
- Tier 1 pode usar Motion se presence/state justificar;
- Tier 2/3 -> carregar `$motion-experience-orchestrator` e seguir `MOTION.md`;
- Tier 4 -> rejeitar/reformular.

Motion é obrigatório onde a continuidade/interação se beneficia, não em quantidade fixa.

### Accessibility
Forms, dialogs, keyboard/focus, ARIA, dynamic announcements ou audit -> accessibility specialist.

## Student Immersive

Para dashboard/player/biblioteca/trilhas, preserve o perfil premium imersivo: fotografia contextual, contraste escuro, serif editorial seletiva e motion de continuidade. Não transformar isso em neon, glassmorphism generalizado ou gamificação infantil.

## Handoff

Para nova UI/redesign informe:

```text
surface_profile
uiux_pro_max: query/mode/dials/adopted guidance
21st: searches/candidate/build/review
motion: tier/components/reduced-motion/performance
react: primitives/features touched
quality: responsive/a11y/visual/e2e
```

<!-- Runtime discovery diagnostic; not a product instruction. -->
SMOKE_MARKER: `ICIBINA_SMOKE_FRONTEND_ORCHESTRATOR_V5_8`

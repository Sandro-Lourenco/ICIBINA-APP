# 19 — Design System e Experience System — Medicina Integrativa

A fonte canônica visual é `design-system/integrative-medicine/MASTER.md`.

A V5.5 transforma o design system em um **Experience System**: foundations compartilhadas + perfis de superfície + motion grammar + workflow assistido por UI/UX Pro Max, 21st.dev e Motion.

## Fontes canônicas

```text
design-system/integrative-medicine/MASTER.md
SURFACES.md
MOTION.md
COMPONENTS.md
PATTERNS.md
ACCESSIBILITY.md
UIUX-PRO-MAX-RECIPES.md
21ST-WORKFLOW.md
VISUAL-QA.md
pages/<route>.md
```

## Direção

**Medical editorial + scientific calm + natural precision + quiet premium.**

Não significa minimalismo genérico. A experiência do aluno pode usar **Student Immersive** com dark premium, fotografia contextual, serif editorial seletiva e motion deliberado. Professor/admin/checkout permanecem mais claros e operacionais.

## Surface profiles

- `Editorial Light`: público, catálogo/course detail, checkout, auth.
- `Student Immersive`: aluno, player, biblioteca/trilhas.
- `Operational Light`: professor e builder; `Operational Neutral`: admin/operações.

Detalhes: `SURFACES.md`.

## Ferramentas

### UI/UX Pro Max

Usar para direção visual, UX, responsiveness, typography, color, accessibility e auditoria. Para nova página/redesign, usar dials definidos em `UIUX-PRO-MAX-RECIPES.md`. Resultado da skill não sobrescreve foundations automaticamente.

### 21st.dev

Usar como camada de exploração, sourcing, build e review:

```text
local primitive -> 21st search -> inspect/adapt -> build -> 21st review
```

`21st-ui-explore` somente se a direção estiver aberta. `21st-design-sync` nunca publica sem autorização.

### Motion

CSS cobre microfeedback simples. `motion/react` cobre presence/layout/continuity/reorder/drag e choreography controlada. Tier 2/3 deve carregar `$motion-experience-orchestrator`; reduced-motion e performance são obrigatórios. Veja `MOTION.md`.

## Quality bar

Nova página/redesign só fecha quando houver, conforme aplicável:

```text
UI/UX Pro Max consultation
21st search/build/review
Motion review
responsive desktop/tablet/mobile
loading/error/empty/success
keyboard/focus
a11y/axe
visual regression
reduced motion
performance sanity
```

“Bonito” sem consistência, acessibilidade ou performance não passa.

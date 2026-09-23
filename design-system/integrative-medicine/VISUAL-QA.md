# ICIBINA Visual QA

UI de produção precisa provar consistência visual, responsividade, acessibilidade e motion behavior — não apenas “parecer boa” em um screenshot.

## Critical viewports

Baseline sugerida para rotas críticas:

```text
mobile compact: 360x800
iPhone-class:   390x844
tablet:         768x1024
laptop:         1440x900
wide desktop:   1920x1080
```

A suite pode ajustar dispositivos reais, mas deve manter pelo menos mobile + desktop e adicionar tablet em layouts complexos.

## Required visual states

Para página com dados assíncronos:

```text
loading
success
empty
error
long-content / overflow
permission/locked when relevant
```

Dashboard/player também validam:

```text
reduced motion
keyboard focus path
slow image loading
missing image fallback
long course title
high zoom/text resize
forced-colors / Windows High Contrast
prefers-contrast: more (quando suportado)
```

## Screenshot regression

- baselines revisadas e versionadas;
- não atualizar snapshots automaticamente para “fazer CI ficar verde”;
- diferenças intencionais exigem revisão visual;
- screenshots devem cobrir surface profile correto, light/dark/immersive quando aplicável.

## 21st review

Para nova página/redesign, execute `21st review` antes do visual regression final. Findings subjetivos não viram fix automático sem decisão de design/produto.

## UI/UX Pro Max audit

Depois da implementação, use busca/auditoria dirigida nos pontos de maior risco: hierarchy, density, interaction, accessibility, responsive e typography. Não regenere o design system durante review.

## Motion QA

Tier 2/3 valida:

- reduced motion;
- no layout thrash perceptível;
- foco e navigation intactos;
- no delayed CTA;
- no infinite motion desnecessário;
- frame/performance sanity em hardware razoável;
- MotionScore quando Motion+ estiver disponível e a rota justificar.

## Manual review checklist

```text
[ ] foco principal claro em <5s
[ ] não parece template SaaS genérico
[ ] não há excesso de cards/containers
[ ] typography hierarchy consistente
[ ] fotografia/crop não compete com texto
[ ] overlays mantêm contraste
[ ] ações principais previsíveis
[ ] layout funciona sem hover
[ ] reduced motion continua compreensível
[ ] forced-colors mantém controles, foco, seleção e status legíveis
[ ] informação continua disponível sem gradients/shadows/background images
[ ] mobile é recomposição, não desktop esmagado
```

# 31 — Frontend Agent Workflow — ICIBINA V5.8

## 1. Contexto mínimo

```text
FRONTEND-CONTRACT
      ↓
page override
      ↓
source/components reais
```

Abrir `MASTER.md`, `SURFACES.md`, `MOTION.md` ou docs longos apenas quando a decisão exige.

## 2. Pipeline visual para nova página/redesign

```text
1. identificar surface profile
2. ler override da página
3. UI/UX Pro Max: pesquisa/dials apropriados
4. confirmar bootstrap shadcn/tokens/primitives no frontend real
5. inventariar primitives locais
6. 21st search/explore quando aplicável
7. 21st build ou implementação React local
8. Motion somente para interações que justificam
9. 21st review
10. UI/UX audit focal
11. Playwright + axe + visual + reduced motion + forced-colors
12. handoff/evidence
```

Isso não significa carregar todas as skills simultaneamente. O agente avança sequencialmente e libera contexto conforme a etapa.

## 3. Roteamento

- React code -> `react`.
- Nova página/redesign/visual hierarchy -> `ui-ux-pro-max`.
- Padrão genérico inexistente -> `21st-cli-use` / `21st-ui-build`.
- Direção realmente aberta -> `21st-ui-explore`.
- UI substancial pronta -> `21st-ui-review`.
- Motion Tier 2/3 -> `$motion-experience-orchestrator` + Motion MCP público quando útil.
- Forms/dialog/keyboard/focus/ARIA complexos -> accessibility specialist.

## 4. Surface profile

Antes de desenhar, escolha um perfil:

```text
Editorial Light
Student Immersive
Operational Light
Operational Neutral
```

Nunca transformar admin/checkout em experiência cinematográfica porque uma referência 21st parecia atraente.

## 5. UI/UX Pro Max

Para páginas novas, usar os dials de `design-system/integrative-medicine/UIUX-PRO-MAX-RECIPES.md`. Consultas devem ter um objetivo dominante. Persistência/`--force` do Master requer autorização explícita.

## 6. 21st.dev

`.21st/DESIGN.md` e `.21st/design.json` derivam do Master. Antes do primeiro intake em frontend real, cumpra `docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md`. Use search antes de hand-code de padrão genérico ausente; reuse local primeiro; review é obrigatório em mudanças substanciais.

## 7. Motion

Leia `design-system/integrative-medicine/MOTION.md`.

```text
Tier 0 CSS
Tier 1 state
Tier 2 layout continuity
Tier 3 immersive choreography
Tier 4 prohibited/high-risk
```

Motion não é requisito quantitativo. Uma tela sem motivo para Motion complexo não deve recebê-lo.

## 8. Evidence

Handoff de nova página/redesign informa:

```text
surface_profile
uiux_query/mode/dials
21st searches/candidate adopted
components reused/created
motion tier + reason
reduced motion behavior
viewports tested
axe/visual/e2e/forced-colors results
known limitations
```

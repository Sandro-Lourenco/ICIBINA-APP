# Frontend Contract — ICIBINA V5.8

Use este contrato como contexto inicial para tarefas frontend. Leia documentos maiores apenas sob gatilho.

## Invariantes

- React 19.3 + TypeScript; TanStack Query para server state.
- `MASTER.md` + page override são autoridade visual.
- Toda rota usa um surface profile: Editorial Light, Student Immersive, Operational Light ou Operational Neutral.
- Reutilize componente local antes de buscar externo.
- Antes do primeiro intake 21st em frontend real, finalize o bootstrap shadcn/Tailwind/aliases/tokens conforme `docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md`.
- Padrão genérico inexistente: pesquise 21st antes de hand-code quando 21st estiver disponível.
- UI/UX Pro Max é obrigatório em nova página/redesign e dirigido em auditoria; não redefine foundations sozinho.
- Motion: CSS para Tier 0; `$motion-experience-orchestrator` + Motion MCP público para Tier 2/3; nunca animar por quota.
- WCAG 2.2 AA; teclado, foco, nomes acessíveis, touch targets, reduced motion e forced-colors/high-contrast.
- Estados de dados: loading + error + empty + success.
- Browser não guarda segredo, não decide preço e não confirma pagamento.
- Não adicionar dependência visual se primitive local resolve.
- Não inserir patient-identifiable data em exemplos, mocks ou UI.

## Contexto sob demanda

```text
React architecture -> docs/04-FRONTEND-REACT.md
agent workflow      -> docs/31-FRONTEND-AGENT-WORKFLOW.md
foundations         -> design-system/.../MASTER.md
surface profile     -> design-system/.../SURFACES.md
motion              -> design-system/.../MOTION.md
UIUX recipes        -> design-system/.../UIUX-PRO-MAX-RECIPES.md
21st workflow       -> design-system/.../21ST-WORKFLOW.md
shadcn bootstrap    -> docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md
page                -> design-system/.../pages/<page>.md
accessibility       -> design-system/.../ACCESSIBILITY.md
quality             -> docs/contracts/QUALITY-CONTRACT.md
React 19.3 delta    -> docs/59-REACT-19.3-DELTA.md
```

## Nova página / redesign

Fluxo mínimo:

```text
surface -> UI/UX Pro Max -> local primitives -> 21st search/build -> Motion if justified -> 21st review -> QA
```

## Handoff mínimo

Registrar surface, Master/override consultados, skills realmente usadas, UIUX query/dials quando aplicável, 21st candidate, motion tier, reduced-motion, checks/viewports e pendências.

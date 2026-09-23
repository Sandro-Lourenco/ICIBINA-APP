---
name: motion-experience-orchestrator
description: Coordena animações Motion da ICIBINA com motion/react, reduced motion, Motion MCP público e Motion+ opt-in, sem depender da redistribuição local do Motion AI Kit.
---

# Motion Experience Orchestrator — V5.8

Use para animação Tier 1–3 quando `MOTION.md` justificar Motion em vez de CSS puro. Contexto curto inicial: `docs/contracts/FRONTEND-CONTRACT.md`; depois carregue `MOTION.md` somente para a decisão de animação.

## Fonte de verdade

1. `design-system/integrative-medicine/MOTION.md`.
2. versão real do pacote `motion` no `frontend/package.json` quando existir.
3. Motion MCP público (`https://mcp.motion.dev`) para docs/exemplos disponibilizados pelo servidor.
4. Motion+ MCP somente quando explicitamente habilitado e autenticado.
5. documentação oficial Motion quando um detalhe for version-sensitive.

## Regras

- import atual: `motion/react`; não instalar `framer-motion` junto;
- Tier 0 continua CSS;
- Tier 2/3 exige comportamento de `prefers-reduced-motion`;
- não animar a mesma transição com React ViewTransition e Motion simultaneamente;
- evitar layout thrash; priorizar transform/opacity em animações frequentes;
- checkout, auth, alertas críticos e conteúdo clínico usam motion mínimo;
- Motion+ é melhoria opcional, nunca requisito de funcionamento.

## Supply-chain

O repositório `motiondivision/ai-kit` permanece referenciado no lock para rastreabilidade, mas a V5.8 **não redistribui sua skill** enquanto a licença do repositório no commit pinado estiver sem declaração verificável. Isso não altera a licença MIT da biblioteca runtime `motion` nem impede o uso do Motion MCP público.

## Handoff

Registre: tier, objetivo da animação, APIs usadas, reduced-motion, impacto de performance e ferramentas MCP realmente usadas.

SMOKE_MARKER: `ICIBINA_SMOKE_MOTION_ORCHESTRATOR_V5_8`

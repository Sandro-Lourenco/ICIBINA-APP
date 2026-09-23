# Frontend Skills Integration — V3

Esta revisão fecha a integração operacional entre Codex/Antigravity e as ferramentas visuais do projeto.

## Adicionado

- `.agents/skills/frontend-experience-orchestrator/SKILL.md`;
- `docs/31-FRONTEND-AGENT-WORKFLOW.md`;
- `scripts/check-frontend-agent-stack.py`;
- `external-skills/README.md`;
- readiness estrito para UI/UX Pro Max, React, 21st core skills e Motion AI Kit;
- traceability/gates específicos para uso real das skills.

## Corrigido

- `AGENTS.md` torna o pipeline de frontend explícito;
- Antigravity workspace rule aplica o mesmo comportamento;
- `docs/14` agora mira Codex **e** Antigravity, não apenas Antigravity;
- 21st.dev passou de referência genérica para `21st-cli-use`, `21st-ui-explore`, `21st-ui-build` e `21st-ui-review`;
- Motion/antigo Framer Motion diferencia CSS simples de animação não trivial;
- `validate-agent-config.py` não retorna falsa sensação de readiness quando as skills externas estão ausentes.

## Regra de supply-chain

As skills externas permanecem instaláveis pelas fontes oficiais em vez de serem copiadas silenciosamente para este ZIP. O pacote contém origem, comando, verificação e comportamento esperado.

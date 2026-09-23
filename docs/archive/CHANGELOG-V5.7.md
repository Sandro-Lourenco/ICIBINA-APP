# CHANGELOG — V5.7

## Frontend runtime & accessibility hardening

- UI/UX Pro Max bridge agora aceita `search.py` direto, skill root ou plugin root; override inválido falha fechado; fallback de cache é determinístico e prioriza cache canônico.
- Novo `check-uiux-pro-max-bridge.py` testa os três formatos e argument forwarding.
- `motiondivision/ai-kit` passa a `NOASSERTION`, `reference-only` e `redistribution=blocked` até licença upstream verificável.
- A capacidade Motion permanece via `motion/react`, novo `motion-experience-orchestrator` local e Motion MCP público; Motion+ segue opt-in.
- shadcn CLI fixado em `4.21.0`; novo gate formal exige `components.json`, aliases, Tailwind/tokens e primitive layer antes do primeiro intake 21st.
- Novo `check-shadcn-bootstrap-contract.py` fiscaliza o contrato em blueprint e, quando frontend real existir, exige `frontend/components.json` válido.
- Accessibility/Visual QA agora cobre `forced-colors`, Windows High Contrast e `prefers-contrast`.
- Validators, contracts, routing fixtures, toolchain lock e canonical sources atualizados para V5.7.

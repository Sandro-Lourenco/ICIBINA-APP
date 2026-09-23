# CHANGELOG — ICIBINA V5.8

## Documentation Consistency Hardening

V5.8 é um release de consistência. Não altera a arquitetura, stack, Experience System ou políticas funcionais da V5.7.

### Corrigido

1. `docs/12-SKILLS-E-AGENTES.md` e `docs/14-INTEGRACAO-BACKEND-FRONTEND.md` não afirmam mais que `motiondivision/ai-kit` é empacotado. O upstream permanece `reference-only`, `NOASSERTION` e `redistribution=blocked`; runtime continua `motion/react` + orquestrador local + Motion MCP público, com Motion+ opt-in.
2. Todos os 11 skills locais agora têm um único `SMOKE_MARKER` terminando em `V5_8`; `smoke-agent-skills.py --all` descobre todos automaticamente.
3. `frontend/package-target.legacy.json` deixou de referenciar o inexistente `dependency-policy.json` e aponta para `toolchain-lock.json`, `supply-chain-policy.json` e `docs/40-SUPPLY-CHAIN-AND-LOCKFILES.md`.
4. README, AGENTS, bootstrap, invariants, bundle builder e fontes visuais correntes identificam V5.8.

### Novo gate

`scripts/check-release-version-consistency.py` valida:

- `blueprint_version`;
- versões geradas pelo bundle builder;
- marker único e atual em todo skill local;
- descoberta dinâmica das skills no smoke test;
- ausência dos claims antigos de redistribuição Motion;
- referências reais do arquivo frontend legacy;
- presença de changelog/validation report da release corrente.

O gate roda em PR/main e também no contrato de release.

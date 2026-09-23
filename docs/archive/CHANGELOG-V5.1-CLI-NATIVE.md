# V5.1 — CLI-native skills

- Skills externas e locais passam a ser distribuídas por plugins nativos de Codex e Antigravity 2.0.
- Codex: repo marketplace + portable Agent Plugin + `.codex/config.toml` enablement.
- Antigravity: `agy plugin install` com skills, rules e Motion MCP.
- UI/UX Pro Max agora é pinada pelo commit auditado e instalada dentro dos plugins, não via `uipro init`.
- Motion `/motion` agora é pinada pelo repositório open-source e instalada dentro dos plugins; Motion/Motion+ MCP usam configuração nativa do host.
- `npx skills` deixa de ser mecanismo final de instalação da ICIBINA.
- `21st` permanece runtime dependency, não package manager de skills.
- Novo `build-agent-cli-bundles.py` e `check-agent-cli-bundles.py`.

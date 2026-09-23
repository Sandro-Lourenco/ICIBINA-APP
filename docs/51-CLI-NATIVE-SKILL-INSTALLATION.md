# 51 — Instalação nativa de skills: Codex CLI + Antigravity 2.0 CLI

## Regra canônica

As skills da ICIBINA **não são instaladas pelo `npx skills` como mecanismo final de distribuição**.

O fluxo oficial é:

```text
external-skills-lock.json
        ↓
commit exato auditado
        ↓
build-agent-cli-bundles.py
        ↓
┌───────────────────────────────┬──────────────────────────────────────┐
│ Codex CLI                     │ Antigravity 2.0 / Antigravity CLI   │
│ portable Agent Plugin         │ Antigravity native plugin            │
│ + repo marketplace            │ + rules + MCP config                 │
└───────────────────────────────┴──────────────────────────────────────┘
        ↓                                      ↓
codex plugin marketplace ...             agy plugin install ...
```

Isso preserva progressive disclosure e faz cada host descobrir as skills pelo mecanismo nativo.

## Codex CLI

Pré-requisito: `codex` instalado/autenticado e o repositório marcado como confiável.

```powershell
.\scripts\install-skills-codex.ps1
```

ou:

```bash
./scripts/install-skills-codex.sh
```

O script:

1. baixa somente as skills pinadas em `external-skills-lock.json`;
2. inclui os orquestradores locais ICIBINA;
3. gera `plugins/codex/icibina-engineering/` com `plugin.json`, `skills/` e `mcp.json`;
4. registra o marketplace local com `codex plugin marketplace add .`;
5. atualiza o marketplace com `codex plugin marketplace upgrade icibina-local` quando suportado;
6. usa `.codex/config.toml` para habilitar `icibina-engineering@icibina-local` no projeto.

Por padrão, o plugin Codex registra somente o Motion MCP público:

- `https://mcp.motion.dev`

Motion+ é opt-in. No PowerShell use `-MotionPlus`; no shell use `ICIBINA_MOTION_PLUS=1`.

O PostgreSQL MCP continua project-scoped em `.codex/config.toml` porque tem política e autenticação próprias.

## Antigravity 2.0 / CLI

Pré-requisito: `agy` instalado/autenticado.

```powershell
.\scripts\install-skills-antigravity.ps1
```

ou:

```bash
./scripts/install-skills-antigravity.sh
```

O script gera `plugins/antigravity/icibina-engineering/` e executa:

```bash
agy plugin install <temporary-validation-plugin>  # valida o pacote; depois é removido
agy plugin list
```

O plugin contém:

- `skills/` — orquestradores locais + especialistas externos pinados;
- `rules/` — regras persistentes do projeto;
- `mcp_config.json` — Motion usando `serverUrl`; Motion+ somente quando habilitado explicitamente;
- `plugin.json` — manifesto do plugin.

Depois de iniciar `agy`, valide interativamente:

```text
/skills
/mcp
```

## UI/UX Pro Max

A skill UI/UX Pro Max é obtida do commit auditado do repositório oficial e empacotada nos dois plugins. O CLI `ui-ux-pro-max-cli` deixa de ser o mecanismo de instalação da ICIBINA; a skill continua completa, incluindo scripts/data/references da pasta revisada.

## Motion

A V5.8 não redistribui a skill upstream `motiondivision/ai-kit`: o commit continua pinado para rastreabilidade, porém o repositório não expõe licença verificável nesse commit. O projeto usa `$motion-experience-orchestrator` (local) + Motion MCP público. Motion+ é opt-in e nunca requisito da aplicação.

Não use `npx motion-ai` como mecanismo de instalação do projeto enquanto o status de licença upstream estiver `NOASSERTION`. Se a licença for publicada/verificada futuramente, qualquer reintrodução exige atualização do lock, revisão de diff e changelog.

## 21st.dev

As skills 21st são empacotadas no plugin. O binário `21st` continua sendo uma **dependência de runtime**, não o mecanismo de instalação das skills:

```bash
npm install -g @21st-dev/cli@1.17.1
```

## Verificação

Blueprint/plugin bundle:

```bash
python scripts/check-agent-cli-bundles.py
python scripts/check-frontend-agent-stack.py
```

Depois da instalação local:

```bash
python scripts/check-agent-cli-bundles.py --runtime
python scripts/check-frontend-agent-stack.py --strict
```

No Antigravity CLI use também `/skills` e `/mcp`.

## Proibição

Não mantenha duas cópias divergentes da mesma skill como autoridades independentes. `.agents/skills/` contém apenas as skills locais ICIBINA source-controlled; especialistas externos são obtidos do lock e empacotados para cada CLI.


## V5.2 — Antigravity project scope

O plugin ICIBINA final fica em `.agents/plugins/icibina-engineering`. `agy plugin install` é usado somente como validação nativa de empacotamento, pois o comando instala globalmente. Veja `docs/52-ANTIGRAVITY-PROJECT-SCOPED-PLUGIN.md`.

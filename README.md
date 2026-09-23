# ICIBINA — Plataforma de Educação em Medicina Integrativa — Engineering Blueprint V5.8 — Documentation Consistency Hardening

Blueprint sênior para desenvolvimento com **Codex + Antigravity**, React, FastAPI, PostgreSQL 18, SQLAlchemy 2/Alembic, Asaas, design system médico, observabilidade e gates de qualidade/segurança.

## Evolução acumulada até a V5.8

A V5.8 preserva toda a arquitetura e o Experience System da V5.7 e fecha os drifts documentais/versionamento identificados na auditoria final:

- **contexto mínimo por tarefa**: contrato curto → código afetado → orquestrador → especialista sob demanda;
- **skills externas versionadas por commit revisado** quando instaladas a partir do GitHub;
- **UI/UX Pro Max, Motion e 21st.dev** continuam especializados e sob demanda, sem dominar o contexto;
- novas skills especializadas para **QA/E2E, segurança, acessibilidade e observabilidade**;
- PostgreSQL MCP permanece **read-only**, mas agora a política é **least-data**: acesso somente ao schema `agent_inspection`, nunca às tabelas internas por padrão;
- PostgreSQL MCP fixado em versão revisada, não `latest`;
- **SQLAlchemy typed ORM + Alembic** continuam sendo a única autoridade para evolução do schema;
- quality/release gates deixam de aceitar `--if-present` para capacidades obrigatórias;
- GitHub Actions do blueprint usam **commit SHA**, não tags flutuantes;
- CI inclui blueprint para SAST, secret scan e filesystem/dependency scan;
- documentação possui **fontes canônicas explícitas** para reduzir drift;
- evidence contract registra skills realmente carregadas e comandos realmente executados;
- changelogs antigos saem da raiz e ficam em `docs/archive/`.

Relatório atual: `VALIDATION_REPORT_V5_8.md`.

Changelog atual: `CHANGELOG-V5.8.md`.

## Leia primeiro

1. `AGENTS.md`
2. `docs/CANONICAL-SOURCES.md`
3. `docs/30-IMPLEMENTATION-READINESS.md`
4. contrato curto correspondente em `docs/contracts/`
5. orquestrador local correspondente em `.agents/skills/`

Não leia `docs/` inteiro antes de cada tarefa.

## Comandos de validação do blueprint

```bash
python scripts/validate-blueprint.py
python scripts/validate-agent-config.py
python scripts/check-context-routing.py
python scripts/check-skill-policy.py
python scripts/check-external-skills-lock.py
python scripts/check-installed-skills-integrity.py
python scripts/check-database-identity.py
python scripts/check-mcp-config.py
python scripts/check-mcp-data-boundary.py
python scripts/check-21st-design-context.py
python scripts/check-design-tokens.py
python scripts/check-experience-system.py
python scripts/check-uiux-pro-max-bridge.py
python scripts/check-shadcn-bootstrap-contract.py
python scripts/check-github-actions-pins.py
python scripts/check-toolchain-pins.py
python scripts/check-reproducible-release.py
python scripts/check-agent-cli-bundles.py
python scripts/check-release-contracts.py
python scripts/validate-skill-evals.py
python scripts/validate-doc-links.py
```

## Skills externas — instalação nativa dos agentes

A ICIBINA instala skills pelo mecanismo nativo de **cada agente**. `external-skills-lock.json` fixa os commits auditados; `scripts/build-agent-cli-bundles.py` monta os plugins sem transformar `.agents/skills/` em depósito de terceiros.

Codex CLI:

```powershell
.\scripts\install-skills-codex.ps1
```

Antigravity 2.0 / Antigravity CLI:

```powershell
.\scripts\install-skills-antigravity.ps1
```

Instalação dos dois, mais dependências de runtime como o binário `21st`:

```powershell
.\scripts\install-agent-skills.ps1
```

No Linux/macOS use os equivalentes `.sh`. Codex usa **plugin marketplace** da própria CLI; Antigravity usa **`agy plugin install` somente para validar o bundle**, e a ativação final fica project-scoped em `.agents/plugins/icibina-engineering`. UI/UX Pro Max é baixado do commit auditado e entra nos dois plugins. A skill upstream do Motion AI Kit permanece referência `NOASSERTION` e não é redistribuída; Motion usa orquestrador local + Motion MCP público. Leia `docs/51-CLI-NATIVE-SKILL-INSTALLATION.md`.

## PostgreSQL MCP

- banco: `ICIBINA`;
- profile: `icibina-readonly`;
- role: `icibina_mcp_reader`;
- servidor: `@microsoft/postgres-mcp@0.1.0-rc.10`;
- modo: read-only;
- superfície permitida: schema `agent_inspection` e views aprovadas;
- schema/data writes: **somente aplicação/migrations autorizadas**, nunca MCP.

Leia `docs/33-MCP-POSTGRESQL-ICIBINA.md` e `docs/46-MCP-DATA-GOVERNANCE.md`.

## Fonte de schema

Depois que a implementação começar:

```text
SQLAlchemy typed models
        ↓
Alembic revisions revisadas
        ↓
PostgreSQL ICIBINA
```

Os SQLs de modelagem deste blueprint são referências históricas e não competem com Alembic. Veja `docs/45-SCHEMA-SOURCE-OF-TRUTH.md`.

## Status

Este pacote é um **engineering blueprint**. Ele pode ser avaliado como documentação e governança, mas o produto só pode ser considerado pronto depois de implementação, migrations reais, testes, security evidence, load tests, restore drill, observabilidade e release gates aprovados.

## Hardening V5.3

- Antigravity ICIBINA fica **workspace-scoped** em `.agents/plugins/icibina-engineering`; o `agy plugin install` é usado só para validar o bundle e a validação global é removida.
- Instaladores são **fail-closed**; erro de marketplace/plugin não é ignorado.
- `scripts/smoke-agent-skills.py` executa smoke tests reais via `codex exec --json` e `agy -p --output-format json`.
- `scripts/check-reproducible-release.py` exige locks/digests quando backend, frontend e deploy reais existirem.
- `supply-chain-policy.json` formaliza requisitos imutáveis de release.


## V5.3 final semantic/runtime gates

```bash
python scripts/check-canonical-invariants.py
python scripts/check-release-version-consistency.py
python scripts/check-database-role-bootstrap.py
python scripts/check-postgres-mcp-profile-isolation.py
python scripts/check-design-tokens.py
python scripts/check-experience-system.py
python scripts/check-uiux-pro-max-bridge.py
python scripts/check-shadcn-bootstrap-contract.py
python scripts/check_frontend_architecture.py
```

After agent plugins are installed, prove an external plugin skill too:

```bash
python scripts/smoke-agent-skills.py --agent both --external
```


## V5.4 — closure hardening

A V5.4 fecha drift editorial/versionamento, imagens imutáveis de release, integridade do cache ativo do Codex, React 19.3 delta, link checking recursivo, capacity evidence, compliance brasileiro, proibição de dados identificáveis de pacientes e refresh policy de imagens de desenvolvimento. Histórico: `docs/archive/CHANGELOG-V5.4.md`.


## V5.5 — Experience System

A V5.5 oficializa uma experiência visual menos genérica e mais premium sem fragmentar a marca:

- `Editorial Light` para público/checkout/auth;
- `Student Immersive` para dashboard/player/biblioteca/trilhas;
- `Operational Light` para professor/builder e `Operational Neutral` para admin/operações;
- UI/UX Pro Max com recipes/dials por superfície;
- 21st.dev com search/build/review obrigatório em mudanças substanciais;
- Motion grammar por tiers, reduced-motion e performance;
- tokens Student Immersive validados por contraste;
- novos componentes `StudentHero`, `JourneyProgress`, `ImmersiveCourseCard` e `ProfessionalMilestone`.

Veja `design-system/integrative-medicine/MASTER.md`, `SURFACES.md`, `MOTION.md` e `docs/60-FRONTEND-DESIGN-EXCELLENCE-PIPELINE.md`.

## V5.6 — Experience System hardening

A V5.6 fecha os últimos drifts encontrados na auditoria visual:

- quatro perfis canônicos sem ambiguidade: `Editorial Light`, `Student Immersive`, `Operational Light` e `Operational Neutral`;
- `scripts/uiux-pro-max.py` torna o `search.py` do UI/UX Pro Max portátil entre workspace Antigravity, bundles e cache ativo do Codex;
- Motion MCP público continua default, enquanto Motion+ é opt-in explícito;
- `preview.html` demonstra os quatro perfis em um único preview interativo;
- `check-experience-system.py` valida headings, surface names, `.21st`, page overrides, preview, bridge e política Motion+.

Veja `docs/61-EXPERIENCE-SYSTEM-V5.6-HARDENING.md`.

## V5.7 — frontend runtime & accessibility hardening

- UI/UX Pro Max bridge aceita `search.py` direto, skill root ou plugin root e falha fechado em override inválido;
- Motion AI Kit upstream passa a `NOASSERTION`/`redistribution=blocked` até licença verificável, com orquestrador Motion local preservando o workflow;
- shadcn CLI `4.21.0` fica pinado e o bootstrap `components.json`/tokens/primitives antecede o primeiro intake 21st;
- QA cobre `forced-colors`, Windows High Contrast e `prefers-contrast`;
- novos validators impedem regressão desses contratos.

Veja `docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md` e `docs/63-EXTERNAL-SKILL-LICENSE-GOVERNANCE.md`.

## V5.8 — documentation consistency hardening

- corrige documentação antiga que tratava `motiondivision/ai-kit` como redistribuível;
- todos os 11 skills locais passam a ter `SMOKE_MARKER` da release V5.8;
- smoke `--all` descobre todos os skills locais automaticamente;
- `frontend/package-target.legacy.json` aponta apenas para políticas/arquivos realmente existentes;
- `scripts/check-release-version-consistency.py` impede regressão de versão, markers e claims legados;
- quality/release gates executam o novo consistency check.

# Fontes canônicas — ICIBINA V5.8

Objetivo: impedir que dois documentos deem ordens diferentes ao agente.

| Tema | Fonte canônica | Complementos |
|---|---|---|
| roteamento de agentes | `AGENTS.md` | `docs/32-CONTEXT-ENGINEERING-ROUTING.md` |
| arquitetura | `docs/00-ARQUITETURA.md` + ADRs | contratos não redefinem arquitetura |
| invariantes semânticos operacionais | `architecture-invariants.json` | `scripts/check-canonical-invariants.py` fiscaliza drift |
| frontend | `docs/contracts/FRONTEND-CONTRACT.md` + `design-system/integrative-medicine/MASTER.md` | page overrides, docs/04 e 31 |
| backend | `docs/contracts/BACKEND-CONTRACT.md` | docs/35 |
| banco/ORM | `docs/contracts/DATABASE-CONTRACT.md` + ADR-002 + docs/34 | docs/22/36 |
| pagamentos | `.agents/skills/asaas-payments/SKILL.md` + docs/03 | contrato API |
| segurança | `docs/contracts/SECURITY-CONTRACT.md` + docs/20 | docs/41/46 |
| QA | `docs/contracts/QA-CONTRACT.md` + docs/21 | docs/37/43/44 |
| observabilidade/performance | `docs/contracts/OBSERVABILITY-CONTRACT.md` + docs/07/23 | docs/47 |
| conteúdo médico | docs/27 | design content guide |
| schema real após implementação | SQLAlchemy models + Alembic history | live DB é evidência de execução, não fonte de mudança |
| skills externas/distribuição | `external-skills-lock.json` + `docs/51-CLI-NATIVE-SKILL-INSTALLATION.md` + `docs/63-EXTERNAL-SKILL-LICENSE-GOVERNANCE.md` | `skills-manifest.json` explica roteamento |
| MCP PostgreSQL | docs/33 + docs/46 | `scripts/postgres-mcp-wrapper.py` + configs `.agents`/`.codex` |
| capacidade medida | `capacity-baseline.json` | docs/23; `UNVERIFIED` bloqueia afirmações de escala comprovada |
| compliance médico Brasil | `docs/56-BRASIL-COMPLIANCE-MEDICAL-CONTENT.md` | docs/27/08 |
| dados identificáveis de pacientes | `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md` | UI/content/security |
| imagens de release | `release-images-lock.json` | `supply-chain-policy.json` |
| imagens de desenvolvimento | `development-images-lock.json` | docs/58 |
| delta React 19.3 | `docs/59-REACT-19.3-DELTA.md` | docs oficiais React prevalecem em fatos version-sensitive |

## Regra de conflito

Se documento secundário contradizer a fonte canônica, **não escolha silenciosamente**. Preserve a fonte canônica, registre o drift e corrija a documentação na mesma mudança quando isso fizer parte do escopo.

- Antigravity plugin scope -> `docs/52-ANTIGRAVITY-PROJECT-SCOPED-PLUGIN.md`
- Runtime skill discovery -> `docs/53-RUNTIME-SKILL-SMOKE-TESTS.md`
- Reproducible release -> `docs/54-REPRODUCIBLE-RELEASE-HARDENING.md` + `supply-chain-policy.json`


## UI / Experience System

```text
Foundations          -> design-system/integrative-medicine/MASTER.md
Surface profiles     -> design-system/integrative-medicine/SURFACES.md
Motion grammar       -> design-system/integrative-medicine/MOTION.md
Components           -> design-system/integrative-medicine/COMPONENTS.md
Patterns             -> design-system/integrative-medicine/PATTERNS.md
UIUX Pro Max recipes -> design-system/integrative-medicine/UIUX-PRO-MAX-RECIPES.md
21st workflow        -> design-system/integrative-medicine/21ST-WORKFLOW.md
shadcn bootstrap     -> docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md
Visual QA            -> design-system/integrative-medicine/VISUAL-QA.md
Page rules           -> design-system/integrative-medicine/pages/*.md
Agent pipeline       -> docs/31-FRONTEND-AGENT-WORKFLOW.md + docs/60-FRONTEND-DESIGN-EXCELLENCE-PIPELINE.md
```

- Experience System hardening: `docs/61-EXPERIENCE-SYSTEM-V5.6-HARDENING.md`

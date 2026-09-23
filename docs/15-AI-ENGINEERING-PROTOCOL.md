# 15 — Protocolo de engenharia com IA — ICIBINA V5

## Objetivo

Agentes trabalham com contexto mínimo suficiente, mudanças pequenas e evidência executável.

## Context loading

```text
1 AGENTS.md / project rule
2 contrato curto do domínio
3 código/testes afetados
4 orquestrador local
5 especialista externo apenas quando gatilho real ocorrer
6 documento longo apenas para decisão ainda não resolvida
7 quality gate no final
```

Não carregue todas as skills para “garantir qualidade”. Isso aumenta conflito e reduz espaço para o código real.

## Task classes

- local: arquivo + teste afetado;
- feature: contrato + orquestrador;
- cross-cutting: dois contratos/orquestradores quando necessário;
- high-risk: pagamento/auth/migration + regressões negativas/rollback;
- architecture: course-platform-architect + ADR;
- review/refactor: code-quality-orchestrator;
- release: platform-quality-gate + runbook.

## Multi-agent

- uma branch/worktree por tarefa;
- ownership de arquivos não sobreposto;
- leia `git status`/`git diff` antes de editar;
- não reverta trabalho desconhecido;
- integração por commits/PRs pequenos.

## External skills

Skills externas são especialistas consultivos. Projeto e docs oficiais da versão têm precedência. Registre no handoff somente as skills realmente usadas.

## Database/MCP

MCP `icibina-postgres` é ferramenta read-only de inspeção. DDL/DML segue código/migration; não use MCP como atalho para “consertar o banco”.

## Handoff

```text
Goal completed
Files changed
Contracts/skills used
Commands actually executed + result
Risk/rollback
Pending validation
```

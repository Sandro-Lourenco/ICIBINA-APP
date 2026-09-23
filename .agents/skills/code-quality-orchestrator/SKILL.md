---
name: code-quality-orchestrator
description: Use para revisão de código, refactor, redução de duplicação, smells, SOLID ou cleanup estruturado; não ativar automaticamente para edição trivial ou feature comum.
---

# Code Quality Orchestrator

## Objetivo

Melhorar qualidade sem ampliar o escopo nem carregar uma skill genérica enorme em toda tarefa.

## Fluxo

1. Leia `docs/contracts/QUALITY-CONTRACT.md`.
2. Inspecione o diff e o contexto local.
3. Identifique problemas comprováveis: responsabilidade misturada, dependência invertida, duplicação estável, naming, erro, testabilidade, ciclo/import indevido.
4. Faça refactor cirúrgico separado de mudança funcional quando possível.
5. Rode testes afetados + architecture check.

## SOLID local

- SRP por use case/componente, não por número arbitrário de linhas.
- abstração só quando existe contrato estável/segundo consumidor real;
- application depende de ports;
- adapters são substituíveis via contract tests;
- `shared/` só recebe conceitos realmente compartilhados.

## External clean-code

A skill externa `clean-code` é **manual/review-only**, não dependência do fluxo padrão. Use apenas em auditoria ampla quando o custo de contexto for justificado.

SMOKE_MARKER: `ICIBINA_SMOKE_CODE_QUALITY_ORCHESTRATOR_V5_8`

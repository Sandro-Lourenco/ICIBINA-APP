# 61 — Experience System V5.6 Hardening

## Objetivo
Fechar os drifts encontrados na auditoria V5.5 sem aumentar o contexto dos agentes.

## UI/UX Pro Max
A invocação canônica é `python scripts/uiux-pro-max.py ...`. O bridge resolve o `search.py` da skill pinada no workspace Antigravity, bundles de build ou cache ativo Codex. Não dependa de `CLAUDE_PLUGIN_ROOT`.

## Surface profiles
Os únicos nomes válidos são `Editorial Light`, `Student Immersive`, `Operational Light` e `Operational Neutral`. Todo page override deve declarar exatamente um.

## Motion
Motion MCP público pode ser default. Motion+ é opt-in via `--include-motion-plus`, `-MotionPlus` no PowerShell ou `ICIBINA_MOTION_PLUS=1` no shell. Nenhuma funcionalidade essencial depende de Motion+.

## Preview e QA
`design-system/integrative-medicine/preview.html` demonstra os quatro perfis. `check-experience-system.py` falha em caso de surface drift, heading duplicado, `.21st` inconsistente, preview incompleto, bridge ausente ou Motion+ não condicional.

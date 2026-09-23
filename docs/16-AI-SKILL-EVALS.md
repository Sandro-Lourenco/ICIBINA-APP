# 16 — Evals de roteamento de skills

A configuração é boa somente se ativa o especialista certo **sem carregar especialistas desnecessários**.

## Frontend

Prompt: `Crie a página de detalhes do curso seguindo a identidade ICIBINA.`

Esperado: `frontend-experience-orchestrator`, React, UI/UX Pro Max; 21st somente se faltar padrão genérico; Motion somente se animação não trivial.

Não esperado: database orchestrator, postgres-pro, software-architect.

Prompt: `Corrija 8px de padding no badge existente.`

Esperado: frontend orchestrator leve + componente local. Não precisa UIUX/21st/Motion por padrão.

## Backend

Prompt: `Adicione GET /api/v1/courses/{id}.`

Esperado: backend orchestrator + FastAPI quando útil. Database orchestrator só se persistence mudar.

Não esperado: course-platform-architect se a fronteira não mudou.

## Database

Prompt: `Adicione índice para busca de cursos publicados e prove com EXPLAIN.`

Esperado: database orchestrator + postgres-pro/sql-pro, migration Alembic, teste/EXPLAIN. MCP read-only pode verificar.

Prompt: `Adicione coluna slug.`

Esperado: database orchestrator; postgres-pro não é obrigatório para alteração simples.

## Architecture

Prompt: `Devemos extrair payments para microserviço?`

Esperado: course-platform-architect; software-architect externo é opcional/manual quando análise profunda justificar.

## Quality

Prompt: `Faça auditoria SOLID do módulo courses.`

Esperado: code-quality-orchestrator. Clean-code externo somente se explicitamente escolhido para auditoria ampla.

Prompt: `Prepare o milestone para handoff.`

Esperado: platform-quality-gate.

## Payment

Prompt: `Implemente PAYMENT_RECEIVED e reprocessamento idempotente.`

Esperado: asaas-payments + backend/database orchestrators conforme arquivos tocados.

## Regressão

Falha de roteamento é: skill crítica ausente **ou** ativação de 3+ especialistas sem gatilho concreto. Registre casos reais e transforme-os em fixtures/evals automatizados quando o harness do agente estiver disponível.

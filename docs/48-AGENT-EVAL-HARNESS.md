# Agent skill routing eval harness

`evals/skill-routing.jsonl` define casos esperados/proibidos, mas validação de JSON não prova comportamento do agente.

## Contrato de execução

Para uma campanha de eval:
1. executar prompt em sessão limpa;
2. capturar skills efetivamente carregadas/tool calls;
3. normalizar para nomes de skill;
4. comparar `required`, `optional`, `forbidden`;
5. registrar score e regressões por modelo/agente/versão.

## Métricas

- required recall;
- forbidden activation rate;
- unnecessary specialist count;
- context bytes/tokens aproximados carregados;
- task success após roteamento.

A V5 adiciona evidence files para tarefas reais; isso não substitui harness automatizado, mas torna auditoria possível.

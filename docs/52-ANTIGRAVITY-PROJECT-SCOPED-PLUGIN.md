# Antigravity — plugin ICIBINA com escopo de projeto

## Decisão

O plugin `icibina-engineering` contém regras, orquestradores e integrações específicas da ICIBINA. Portanto **não deve permanecer instalado globalmente** no perfil do Antigravity.

A documentação atual do Antigravity distingue:

- `.agents/plugins/<plugin>/` no workspace: ativo somente naquele projeto;
- `agy plugin install <path>`: staging no diretório global do CLI.

## Fluxo adotado

1. `build-agent-cli-bundles.py` constrói o pacote revisado em `plugins/antigravity/icibina-engineering`;
2. `install-antigravity-workspace-plugin.py` cria uma cópia temporária com nome de validação;
3. essa cópia passa por `agy plugin install` + `agy plugin list`, provando que o CLI aceita o pacote;
4. a cópia global de validação é removida;
5. o plugin final é materializado em `.agents/plugins/icibina-engineering`;
6. `/skills` e `/mcp` devem ser conferidos dentro do repositório ICIBINA.

Assim usamos o CLI nativo para validação do pacote sem deixar regras ICIBINA vazarem para outros workspaces.

## Gate

`python scripts/check-agent-cli-bundles.py --strict-build`

Após autenticar os CLIs, execute também:

```bash
python scripts/smoke-agent-skills.py --agent antigravity
```

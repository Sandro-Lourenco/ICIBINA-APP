# Supply chain, versões e lockfiles — V5

## Objetivo

A versão revisada de uma skill/dependência deve ser a versão instalada. `reviewed_ref` sem enforcement não é controle.

## Skills externas

`external-skills-lock.json` registra `repo`, `ref`, `source_path` e `target_name`. `scripts/build-agent-cli-bundles.py` baixa o **commit exato**, extrai somente a pasta revisada e monta dois pacotes:

- `plugins/codex/icibina-engineering` — portable Agent Plugin;
- `plugins/antigravity/icibina-engineering` — plugin nativo Antigravity 2.0/CLI.

A instalação é validada pelos CLIs nativos. Codex usa `codex plugin marketplace ...`; Antigravity valida o pacote com `agy plugin install` e ativa a cópia final somente no workspace em `.agents/plugins/icibina-engineering`. Não use `npx skills` como mecanismo final. Upgrades exigem:

1. atualizar `ref`;
2. revisar diff do upstream;
3. regenerar bundles;
4. rodar skill routing/context checks;
5. atualizar changelog.

## Dependências de runtime

- 21st CLI: versão explícita; necessário pelas skills 21st, mas não instala as skills.
- Microsoft PostgreSQL MCP: versão explícita em configs/scripts.
- Motion MCP: endpoints hospedados oficiais declarados dentro dos plugins dos agentes.
- UI/UX Pro Max: pinada por commit Git e empacotada nos plugins nativos.
- Motion runtime/MCP: biblioteca/runtime segue sua licença própria; `motiondivision/ai-kit` permanece referência pinada, mas sua skill não é redistribuída enquanto o commit auditado não declarar licença verificável. `NOASSERTION` + `redistribution=blocked` é fiscalizado pelo lock checker.

## Aplicação real

Backend deve ter um lockfile suportado (`uv.lock`, `poetry.lock` ou equivalente aprovado). Frontend deve ter `package-lock.json` e CI usa `npm ci`. `package.json` real não pode usar `latest`, `*` ou ranges vazios.

## GitHub Actions

Actions externas devem usar commit SHA de 40 caracteres. Comentário pode indicar a tag humana auditada.

## Containers

`latest` pode existir apenas em template local explicitamente marcado. Imagens de staging/produção devem usar versão imutável/digest.

## Imagens de release e desenvolvimento — V5.4

- `release-images-lock.json` é a única fonte aceita para imagens usadas nos gates de release; referências devem ser `@sha256`.
- `development-images-lock.json` governa somente Docker local e exige revisão a cada 90 dias.
- a imagem MinIO local não é evidência de produção; o upstream arquivado exige reavaliação antes de dependência operacional.
- `python scripts/check-release-image-lock.py` e `python scripts/check-development-image-review.py --strict` fiscalizam drift.

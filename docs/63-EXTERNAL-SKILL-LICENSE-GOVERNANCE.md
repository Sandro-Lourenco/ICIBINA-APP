# 63 — Governança de licença de skills externas — V5.8

## Regra

Pin de commit prova **versão**, não prova **direito de redistribuição**. Antes de copiar uma skill externa para os plugins ICIBINA, o lock precisa registrar licença verificável no source auditado.

Estados aceitos:

```text
license conhecida + redistribuição permitida -> pode bundlar
NOASSERTION + redistribution=blocked         -> referência somente
manual                                        -> não entra no bundle default
```

`scripts/check-external-skills-lock.py` falha se `NOASSERTION` não estiver acompanhado de bloqueio de redistribuição.

## Motion AI Kit

No commit `1140efe9ad5e03c689ea6bb19d9d3850a4dae5f7` do repositório `motiondivision/ai-kit`, a auditoria V5.7 não encontrou arquivo de licença no tree e a metadata do repositório não declara licença. Portanto:

```text
license: NOASSERTION
mode: reference-only
redistribution: blocked
```

Isso **não** redefine a licença da biblioteca runtime `motion`, que é um projeto separado. A ICIBINA mantém as capacidades de animação por `motion/react`, pelo orquestrador local `motion-experience-orchestrator` e pelo Motion MCP público; Motion+ continua opt-in.

## Reintrodução futura da skill upstream

Somente após:

1. licença upstream verificável no commit escolhido;
2. compatibilidade do uso/redistribuição confirmada;
3. atualização de `external-skills-lock.json`;
4. revisão do diff;
5. build dos bundles;
6. integrity + smoke tests;
7. changelog.

Não inferir licença de um repositório a partir da licença de outro projeto da mesma organização.

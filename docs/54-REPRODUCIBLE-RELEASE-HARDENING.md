# Release reproducível — hardening final

## Regra

Blueprint pode usar templates de desenvolvimento. Release real não pode depender de versões mutáveis.

Quando o código real existir, o release exige:

- Python exato em `.python-version` e `backend/uv.lock`;
- `frontend/package.json` acompanhado de `package-lock.json`, sem `latest`, `*` ou versão vazia;
- GitHub Actions por SHA imutável;
- skills por commit auditado + hash da árvore instalada;
- MCP packages por versão explícita;
- imagens de produção por `@sha256:<digest>`.

`docker-compose.target.yml` é somente template local e não constitui evidência de release.

## Gate

```bash
python scripts/check-reproducible-release.py
```

Enquanto backend/frontend/deploy reais não existirem, o gate deve informar `PENDING`, jamais `PASS` de produção.

## Reviewed runtime baseline (2026-09-23)

- Node.js `24.21.0` LTS
- Python `3.13.15`
- uv `0.12.17`

Esses números são baseline revisado, não licença para upgrade automático. Mudança exige atualização de `toolchain-lock.json`, CI e revisão de compatibilidade.

# Development image refresh policy — ICIBINA V5.4

## Objetivo

Imagens usadas somente no ambiente local são conveniências de desenvolvimento, não evidência de release. Elas precisam de revisão periódica para evitar que o ambiente local fique anos preso a imagens antigas ou descontinuadas.

A fonte executável desta política é `development-images-lock.json`.

## Cadência

- revisão mínima: a cada **90 dias**;
- qualquer CVE crítica relevante, depreciação ou arquivamento upstream antecipa a revisão;
- a revisão registra data, referência usada, status upstream e decisão;
- tags mutáveis de desenvolvimento **nunca** satisfazem o gate de produção/release.

## MinIO

A baseline local permanece `minio/minio:RELEASE.2025-10-15T17-29-55Z` apenas para desenvolvimento S3-compatible. O repositório upstream foi arquivado em 25/04/2026; portanto, a ICIBINA deve reavaliar uma alternativa mantida antes de qualquer dependência operacional/produção. Não promover esta imagem a produção apenas porque funciona localmente.

## Produção

Produção e release obedecem `release-images-lock.json` e `supply-chain-policy.json`: referência imutável por digest `@sha256:...`.

## Gate

```bash
python scripts/check-development-image-review.py
python scripts/check-development-image-review.py --strict
```

O modo `--strict` falha quando uma revisão venceu ou quando a referência local documentada diverge do lock.

# OpenAPI compatibility baseline

When `backend/` becomes real, CI exports the current specification to `backend/openapi.json` and compares it with `contracts/openapi/baseline.json` using **a imagem imutável de oasdiff registrada em `release-images-lock.json`**.

Policy:
- breaking changes fail release unless an explicit versioning/ADR decision approves them;
- after an intentional compatible release, update the baseline in the same reviewed PR;
- never hand-edit the generated current spec.

# Release gates

## Regra

No release, capacidade obrigatória ausente é `FAIL`, não `SKIP`.

### Backend implementado
- lockfile presente;
- Ruff/format/typecheck;
- Alembic `upgrade head` em DB limpo;
- pytest + coverage baseline;
- architecture fitness functions;
- dependency/security scan;
- authz/payment regressions quando aplicáveis.

### Frontend implementado
- package-lock + `npm ci`;
- lint/typecheck/unit/build;
- scripts obrigatórios: `test:e2e`, `test:a11y`, `test:visual`, `check:bundle`;
- Core Web Vitals/performance evidence para páginas públicas críticas.

### Operação
- migration/rollback plan;
- observability/alerts;
- backup/restore drill conforme milestone;
- security gate;
- changelog e ADR quando decisão estrutural.


## V5.3 hard gates
- backend: PostgreSQL release isolado com roles `owner/migrator/app/mcp_reader`;
- migrations rodam apenas com `icibina_migrator`;
- `icibina_app` prova DDL negado;
- `icibina_mcp_reader` prova leitura permitida apenas em `agent_inspection` e DDL negado;
- suites `authz` e `payments_security` são obrigatórias;
- OpenAPI é exportado e comparado com baseline via a imagem imutável de oasdiff registrada em `release-images-lock.json`;
- SBOM CycloneDX é gerado e validado;
- frontend/backend architecture fitness functions são release gates.

## Gates V5.4 adicionais

Antes de release:

```bash
python scripts/check-release-image-lock.py
python scripts/check-development-image-review.py --strict
python scripts/check-capacity-baseline.py --strict
```

`capacity-baseline.json` só passa em modo estrito depois de medições reproduzíveis; não há números default inventados.

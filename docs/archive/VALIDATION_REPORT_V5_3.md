# ICIBINA V5.3 — Validation Report

Data da validação: 2026-09-23.

## Resultado

A V5.3 passou em todos os gates estáticos executáveis do blueprint neste ambiente. Estados dependentes de runtime/código real continuam **PENDING**, nunca são promovidos a PASS sem evidência.

## PASS

- 10 skills locais: 0 erros / 0 warnings;
- 19 skills externas: lock/policy válidos, runtime ainda não instalado;
- blueprint critical files: 69 presentes;
- links internos: 103 Markdown verificados;
- canonical semantic invariants;
- PostgreSQL role bootstrap contract;
- ICIBINA / ICIBINA_test identity;
- PostgreSQL MCP pinned + project-isolated profile store;
- MCP least-data (`agent_inspection` only);
- 21st design context;
- 7 context contracts, 0 warnings;
- 16 skill-routing eval fixtures;
- skill policy;
- external skills lock;
- GitHub Actions SHA pins;
- exact toolchain pins;
- release contract static gate;
- JSON/YAML parse;
- Python compile;
- shell syntax;
- light and dark design-token contrast.

### Contrast evidence

Light theme critical text/status pairs remain >= 4.5:1.
Dark theme:
- foreground/background: 17.25:1;
- muted/surface: 8.98:1;
- primary/surface: 8.48:1;
- danger/surface: 7.25:1;
- warning/surface: 9.14:1;
- info/focus on surface: 6.27:1;
- success/surface: 8.45:1;
- border/surface: 3.36:1.

## V5.3 hardening added

1. Fresh local PostgreSQL initializes `icibina_owner`, `icibina_migrator`, `icibina_app`, `icibina_mcp_reader` coherently.
2. Runtime uses `icibina_app`; Alembic uses `icibina_migrator`.
3. Release gets a clean PostgreSQL service and proves `icibina_app` cannot DDL.
4. Release creates canaries proving `icibina_mcp_reader` can read approved `agent_inspection` data but cannot read application schema or DDL.
5. postgres-mcp profile files are isolated under `.icibina/mcp-home`; unrelated user profiles are not in the server profile store.
6. `architecture-invariants.json` + checker detect semantic drift across env/compose/docs/payment/MCP.
7. Asaas sequence now uses inbox/outbox -> commit -> 2xx -> worker effects.
8. Plugin smoke tests can probe plugin-only `ui-ux-pro-max` and official `fastapi`, not only local orchestrators.
9. Active Antigravity workspace plugin participates in external-skill integrity verification.
10. OpenAPI release contract uses oasdiff v1.32.1 against a reviewed baseline once backend is real.
11. Security/release workflows generate and validate CycloneDX SBOM.
12. Backend release requires explicit `authz` and `payments_security` pytest markers.
13. Backend architecture checker adds cross-module internal-import and coarse cycle checks.
14. Frontend architecture checker blocks raw `fetch()` outside transport and cross-feature internal imports under the defined policy.
15. MinIO local quick-start has an explicit pinned release tag; production still requires image digest.

## PENDING by design

- external skill runtime installation through Codex / Antigravity;
- agent runtime smoke tests (`--external`) until CLIs are installed/authenticated;
- `backend/src` architecture checks until backend implementation exists;
- `frontend/src` architecture checks until frontend implementation exists;
- `backend/uv.lock`, `.python-version`, real OpenAPI baseline/export and pytest security markers until backend exists;
- `frontend/package.json` + `package-lock.json` and release scripts until frontend exists;
- production container digest pins until production manifests exist;
- runtime PostgreSQL/MCP profile proof until local DB + profile are configured.

## Runtime commands after extraction

```powershell
.\scripts\install-agent-skills.ps1
.\scripts\setup-postgres-mcp.ps1
python scripts\check-postgres-mcp-profile-isolation.py --runtime
python scripts\check-agent-cli-bundles.py --runtime
python scripts\check-frontend-agent-stack.py --strict
python scripts\smoke-agent-skills.py --agent both --external
```

## Verdict

V5.3 is internally consistent as an engineering blueprint. Remaining PENDING items require the real application/runtime and are deliberately fail-closed at release time.

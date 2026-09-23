# V5.2 — final blueprint hardening

- Antigravity ICIBINA project-scoped; global CLI install only validates package and is removed.
- Codex marketplace setup fail-closed; no `|| true`/silent catch.
- Runtime skill discovery smoke tests for Codex and Antigravity headless modes.
- Reproducible release policy for Python/Node locks and container digests.
- New supply-chain policy file and release checker.
- Critical orchestrators carry runtime-only smoke markers.

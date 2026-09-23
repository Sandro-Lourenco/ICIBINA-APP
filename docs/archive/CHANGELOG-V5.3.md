# ICIBINA V5.3

- Executable local PostgreSQL role bootstrap (`owner`, `migrator`, `app`, `mcp_reader`).
- Runtime and migration DSNs now use distinct roles.
- Release/quality backend jobs use isolated PostgreSQL and prove app DDL denial.
- postgres-mcp profile files isolated under `.icibina/mcp-home` through a wrapper.
- Canonical semantic invariant file + checker added.
- Asaas webhook diagram aligned with inbox/outbox/worker rule.
- Dark mode semantic tokens and contrast checks added.
- Plugin smoke tests now include plugin-only UI/UX Pro Max and official FastAPI skills.
- Active Antigravity workspace plugin included in integrity verification.
- OpenAPI breaking-change release gate (oasdiff 1.32.1) specified.
- CycloneDX SBOM generation/validation added to security and release CI.
- Explicit `authz` and `payments_security` pytest suites required for backend release.
- Backend module-boundary/cycle checks and frontend architecture checks expanded.
- MinIO quick-start now has an explicit pinned local default instead of a missing mandatory env var.

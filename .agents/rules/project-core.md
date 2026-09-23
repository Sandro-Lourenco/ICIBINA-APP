# ICIBINA — workspace rule V5

Configurar esta rule como **Always On** no workspace Antigravity.

- Leia `AGENTS.md` e o contrato curto; não carregue docs/skills em massa.
- Banco: `ICIBINA`; CI: `ICIBINA_test`.
- Preserve `interface -> application -> domain`; infrastructure implementa ports.
- SQLAlchemy só em infrastructure; Unit of Work controla transação; schema só Alembic.
- PostgreSQL MCP é read-only e só deve enxergar `agent_inspection`/views aprovadas.
- Skills externas são especialistas sob demanda; projeto local prevalece sobre exemplos genéricos.
- Frontend segue design system ICIBINA; a11y WCAG 2.2 AA é requisito, não polimento.
- Browser nunca decide preço ou confirma pagamento.
- Role + ownership; jobs/webhooks idempotentes.
- Sem produção irreversível sem aprovação humana explícita.
- No handoff, reporte evidência real e skills efetivamente usadas.


## UI Experience
Frontend segue o Experience System ICIBINA: `Editorial Light`, `Student Immersive`, `Operational Light` e `Operational Neutral`. Nova página/redesign passa pelo frontend orchestrator; UI/UX Pro Max/21st/Motion não podem criar uma identidade paralela ao Master.

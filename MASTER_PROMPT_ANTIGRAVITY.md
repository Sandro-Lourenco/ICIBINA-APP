# Bootstrap — Antigravity — ICIBINA V5.8

1. Configure `.agents/rules/project-core.md` como **Always On**.
2. Leia `AGENTS.md`; não leia toda a documentação.
3. Classifique a tarefa e leia somente o contrato curto correspondente em `docs/contracts/`.
4. Inspecione código/testes afetados.
5. Ative o orquestrador local indicado em `AGENTS.md`.
6. Carregue especialista externo somente quando o gatilho específico ocorrer.
7. Banco `ICIBINA`: SQLAlchemy/Alembic é a autoridade; MCP `icibina-postgres` é read-only e limitado a `agent_inspection`.
8. Para tarefa substancial, registre evidence no formato `docs/tasks/TASK_EVIDENCE_TEMPLATE.json`.
9. Use `$platform-quality-gate` no handoff; `SKIPPED/PENDING != PASS`.
10. Nunca alegue skill, MCP, teste, build, migration, benchmark ou review que não foi realmente executado.


## Experience System V5.8

Em frontend visual, siga `FRONTEND-CONTRACT` e o `frontend-experience-orchestrator`. Nova página/redesign deve classificar a surface e usar progressivamente UI/UX Pro Max, 21st.dev e Motion. Para área do aluno/player, use `Student Immersive` quando o override indicar; admin/checkout não herdam essa estética.

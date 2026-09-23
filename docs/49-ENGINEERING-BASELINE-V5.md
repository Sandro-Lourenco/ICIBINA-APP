# Engineering baseline V5

Este documento define o que significa “V5 documentalmente pronta”.

- fontes canônicas identificadas;
- contratos curtos e orquestradores com gatilhos estreitos;
- skills GitHub revisadas instaláveis por commit exato;
- MCP PostgreSQL versionado, read-only e least-data;
- ORM/Alembic como schema authority;
- release gates sem falso verde por script ausente;
- security CI planejado/executável quando código existe;
- a11y WCAG 2.2 AA;
- load/capacity sem promessas não medidas;
- evidence contract para skills/gates usados;
- docs antigas arquivadas, não concorrendo com a versão atual.

Isso avalia a governança e a documentação. Produto 10/10 exige evidência real após implementação.


## V5.3 semantic/runtime proof layer
A baseline documental só é considerada íntegra quando `architecture-invariants.json` e os validators V5.3 confirmam roles, MCP isolation, Asaas ordering, light/dark contrast and release evidence.

## V5.4 closure

A V5.4 fecha os drifts remanescentes da auditoria: roadmap sem duplicação, versão única 5.4.0 nos bundles, imagens de release por digest, owner canônico de `agent_inspection`, cache ativo Codex incluído no integrity check, React 19.3 delta, smoke externo semântico, link checker recursivo, capacity baseline executável, compliance Brasil, política de dados de pacientes e refresh de imagens de desenvolvimento.

Capacidade permanece intencionalmente `UNVERIFIED` até existir teste real; runtime de agentes permanece `PENDING` até instalação/autenticação local.


## V5.5 experience-system baseline

A V5.5 acrescenta uma baseline visual executável:

- `Editorial Light`, `Student Immersive`, `Operational Light` e `Operational Neutral` como perfis canônicos de superfície;
- UI/UX Pro Max com recipes e dials por superfície;
- 21st search/build/review com design context derivado do Master;
- Motion tiers 0–4, reduced-motion e performance rules;
- token set Student Immersive validado por contraste;
- `check-experience-system.py` e novos skill-routing evals;
- visual QA e evidence contract ampliados.

A baseline melhora qualidade e consistência, mas não obriga animação ou componente externo quando isso não ajuda o usuário.

# Changelog V5.4 — 2026-09-23

V5.4 fecha os 12 pontos restantes da auditoria V5.3.

- remove duplicação de Fase 0.5 do roadmap;
- atualiza plugin/bundle/smoke markers para V5.4;
- release containers passam a usar referências imutáveis de `release-images-lock.json`;
- alinha `003_mcp_readonly_role.sql` ao owner `icibina_migrator`;
- integrity checker passa a verificar o cache ativo do Codex e plugin ativo do Antigravity;
- adiciona delta oficial React 19.3;
- smoke tests externos passam a usar JSON semântico tolerante;
- link validator passa a cobrir todo Markdown do repositório;
- Capacity Model recebe baseline executável `UNVERIFIED` sem números inventados;
- adiciona compliance Brasil (LGPD/ANPD/CFM);
- proíbe dados identificáveis de pacientes em notas/uploads/conteúdo, com UX e controles técnicos;
- cria política de refresh periódico de imagens de desenvolvimento e registra o status do MinIO.

A V5.4 mantém `PENDING != PASS`: capacidade, runtime dos agentes, lockfiles reais e manifests de produção permanecem pendentes até existirem evidências reais.

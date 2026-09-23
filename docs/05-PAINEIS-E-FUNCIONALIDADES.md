# 05 — Painéis e funcionalidades

## Área pública

### Landing

- proposta de valor;
- cursos em destaque;
- professores;
- prova social;
- FAQ;
- CTA para catálogo.

### Catálogo

- busca;
- categoria;
- nível;
- professor;
- preço;
- paginação/cursor;
- ordenação controlada pelo backend.

### Página do curso

- capa;
- título/subtítulo;
- professor;
- descrição;
- objetivos;
- conteúdo curricular;
- duração;
- requisitos;
- avaliações;
- preço;
- CTA de compra ou “continuar curso”.

## Painel do aluno

### Dashboard

Cards úteis, não decorativos:

- continuar estudando;
- progresso dos cursos;
- próximas atividades/lives;
- certificado recente;
- avisos.

### Meus cursos

Status:

```text
em andamento
concluído
acesso suspenso
```

### Player de aula

```text
sidebar curricular
video/player
título e descrição
recursos/downloads
concluir aula
próxima aula
notas pessoais opcional
```

Atualização de progresso deve ser idempotente.

### Avaliações

- tentativas;
- tempo/limite se configurado;
- score;
- feedback;
- revisão conforme política do professor.

### Certificados

- lista;
- validação pública por código/QR;
- download PDF;
- data e curso.

### Compras

- pedido;
- data;
- status;
- valor;
- método quando disponível;
- link de cobrança/segunda via quando aplicável;
- nota/recibo apenas se existir integração correspondente.

## Painel do professor

### Dashboard

- cursos ativos/rascunho;
- alunos ativos;
- conclusão média;
- últimas matrículas;
- avaliações recentes;
- jobs de vídeo com falha.

Métricas financeiras do professor só aparecem se o modelo comercial realmente exigir repasse/marketplace; não inventar essa regra.

### Builder de curso

```text
Informações
Currículo
Módulos
Aulas
Mídia/recursos
Avaliações
Configurações
Pré-visualização
Publicação
```

Suportar drag/reorder com operação atômica no backend.

### Publicação

Fluxo sugerido:

```text
draft -> review_pending -> published -> archived
```

Se não houver moderação administrativa, `review_pending` pode ser removido.

### Alunos

Professor enxerga somente alunos matriculados nos próprios cursos e somente os dados necessários para ensino.

### Analytics do curso

- matrículas no período;
- alunos ativos;
- progresso médio;
- aulas com maior abandono;
- conclusão;
- notas agregadas;
- reviews.

## Painel administrativo

### Visão geral

- usuários ativos;
- novos cadastros;
- matrículas;
- pagamentos por estado;
- receita reconhecida conforme regra financeira;
- webhooks falhos;
- jobs falhos;
- API p50/p95/p99;
- error rate;
- DB pool/conexões;
- queue depth.

### Usuários

- busca;
- status;
- roles;
- sessões;
- bloqueio/desbloqueio com motivo;
- reset/revogação de sessão;
- audit trail.

### Professores

- perfil;
- status de aprovação caso exista processo;
- cursos;
- ocorrências/moderação.

### Cursos

- listar;
- filtrar por status;
- revisar publicação;
- arquivar/despublicar com motivo e auditoria.

### Financeiro

- pedidos;
- pagamentos;
- Asaas IDs;
- webhooks;
- divergências;
- reprocessamento controlado;
- refund somente se um fluxo administrativo seguro for implementado.

### Operações

- health de API/DB/Redis/storage/Asaas;
- latência;
- taxa de erro;
- jobs;
- dead letter/retries;
- webhooks com falha;
- migrations aplicadas;
- versão do build/commit;
- feature flags;
- maintenance mode.

### Auditoria

Exibir:

```text
quem
quando
ação
recurso
resultado
IP anonimizado/adequado à política
request/correlation id
antes/depois apenas para campos permitidos
```

Nunca mostrar senha, token, API key ou payload financeiro bruto sensível.


## Medicina integrativa — requisitos de domínio

### Curso/professor

Além do conteúdo comum, permitir registrar e apresentar quando aplicável:

- credenciais profissionais do docente;
- objetivos de aprendizagem;
- público profissional/pré-requisitos;
- referências;
- data e responsável por revisão;
- disclosure/conflito de interesse;
- créditos/acreditação somente quando validados;
- status de revisão editorial/científica.

### Aluno

Na experiência de aula, prever padrões `EvidenceNote`, `ClinicalPearl`, `ClinicalCaution`, `ReferenceList` e transcrição/legenda quando disponível.

### Admin acadêmico

Adicionar visão de:

- conteúdo aguardando revisão;
- revisão vencendo/vencida;
- professores/credenciais pendentes de validação;
- disclosures;
- referências incompletas quando a política exigir;
- acreditações/créditos ativos e respectivos documentos/validade.

Governança completa: `docs/27-GOVERNANCA-CONTEUDO-MEDICO.md`.


## Regra transversal para notas/casos/uploads

Qualquer nota pessoal, material ou upload em contexto clínico deve exibir o aviso de não inserir dados identificáveis de pacientes e obedecer `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md`.

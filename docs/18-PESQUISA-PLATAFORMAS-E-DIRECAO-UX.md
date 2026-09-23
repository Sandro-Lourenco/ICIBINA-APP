# 18 — Pesquisa de plataformas e direção de produto/UX

> Pesquisa de referência realizada em setembro de 2026. O objetivo é extrair padrões úteis, não copiar identidade visual, textos, componentes proprietários ou fluxos de terceiros.

## 1. Posicionamento do produto

A plataforma será um **ambiente premium de educação em medicina integrativa para profissionais e estudantes da saúde**, com três atributos que devem aparecer tanto na experiência quanto na comunicação:

1. **Credibilidade científica** — referências, revisão, credenciais do docente, data de revisão e transparência de conflitos de interesse.
2. **Clareza didática** — conteúdos complexos divididos em unidades curtas, recursos visuais, avaliações e continuidade de estudo.
3. **Cuidado humano sem estética “mística”** — linguagem acolhedora e elementos naturais discretos, mas com rigor de produto médico/acadêmico.

A interface não deve parecer nem um prontuário hospitalar frio nem um site de spa/wellness. A direção é **academic healthcare + calm premium + evidence-first**.

## 2. Referências pesquisadas

### Coursera

Padrões úteis:

- descoberta forte por busca, categoria e trilhas;
- course cards comparáveis e previsíveis;
- páginas de curso com módulos, docente, resultados de aprendizagem, duração e certificado;
- progresso e certificado como elementos centrais da jornada.

Aplicar:

- catálogo com filtros claros;
- card de curso informativo sem excesso de texto;
- página pública de curso com “o que você aprenderá”, programa, professor, carga horária e requisitos.

Não copiar:

- identidade azul, hierarquia visual ou composição específica.

### MasterClass

Padrões úteis:

- forte percepção premium;
- fotografia de alta qualidade e narrativa editorial;
- hierarquia simples, grandes títulos e foco no docente.

Aplicar com moderação:

- hero editorial nas páginas públicas;
- retrato do professor com credenciais;
- espaço em branco e composição sofisticada.

Não aplicar:

- dark/cinematic como linguagem dominante do produto médico;
- imagens excessivamente dramáticas que prejudiquem legibilidade ou credibilidade acadêmica.

### Osmosis

É a referência de produto mais próxima no eixo **educação em saúde**.

Padrões úteis observados:

- vídeos curtos e visuais;
- quizzes e flashcards;
- study schedule;
- active recall e spaced repetition;
- notas de alto rendimento;
- fluxogramas/decision trees;
- integração do assistente de IA dentro do contexto da aula;
- transcrição, velocidade de reprodução e continuidade entre recursos.

Aplicar:

- player com currículo lateral;
- resumo e referências da aula;
- avaliação logo após blocos importantes;
- “continuar estudando” e sequência recomendada;
- futura evolução para active recall/flashcards como módulo opcional.

### AMBOSS

Padrões úteis:

- conhecimento médico denso com excelente navegação;
- ligação entre conteúdo, perguntas e recursos visuais;
- ferramentas de professor e analytics;
- forte sinal de autoria/revisão por profissionais;
- organização para “learn / practice / teach”.

Aplicar:

- conteúdo educacional conectado a avaliações e referências;
- metadados científicos visíveis sem poluir a tela;
- analytics orientado a lacunas de aprendizagem;
- painel docente focado em ação, não apenas métricas decorativas.

### Lecturio

Padrões úteis:

- short-form video lessons;
- qbank;
- spaced repetition;
- learning paths;
- concept pages;
- associação clara entre vídeo, prática e revisão.

Aplicar:

- trilhas de aprendizagem;
- estimativa de carga e duração;
- sequência vídeo → leitura/resumo → prática → revisão.

### MedBridge

Padrões úteis:

- educação continuada para profissionais de saúde;
- forte uso de credenciais, acreditação e créditos;
- biblioteca por disciplina/especialidade;
- experiência voltada a profissionais em exercício.

Aplicar:

- suporte estrutural a CE/CME/horas educacionais quando juridicamente e academicamente aplicável;
- informações de acreditação somente quando comprovadas;
- certificados verificáveis e histórico de formação.

### Institute for Functional Medicine (IFM)

É a referência de domínio para **educação em medicina funcional/integrativa**.

Padrões úteis observados:

- currículo organizado em formação fundamental e módulos avançados;
- cursos on-demand e cohort-based;
- docentes apresentados como especialistas e clínicos;
- certificação e educação continuada tratadas como jornadas distintas;
- forte importância de competências, escopo profissional, independência educacional e transparência.

Aplicar:

- taxonomia por trilha e nível;
- distinção entre “curso”, “trilha”, “evento/coorte” e “certificação”;
- credenciais e escopo profissional do docente;
- revisão científica e disclosure de conflitos.

Não afirmar:

- que um curso é certificado/acreditado por qualquer instituição sem contrato e comprovação formal.

## 3. Padrões de produto adotados

### Jornada pública

```text
Descoberta
  → filtro por tema/nível/formato
  → página do curso
  → docente + evidência + programa
  → checkout
  → matrícula confirmada por webhook
```

### Jornada de aprendizagem

```text
Continuar estudando
  → aula curta/focada
  → resumo clínico/educacional
  → referências
  → questão/avaliação
  → progresso
  → próxima aula
```

### Jornada do professor

```text
Curso em rascunho
  → objetivos de aprendizagem
  → módulos/aulas
  → referências e disclosures
  → avaliações
  → revisão editorial/científica quando exigida
  → preview
  → publicação
```

### Jornada administrativa

```text
Negócio + acadêmico + operação
  → usuários/professores
  → cursos e revisão
  → pagamentos
  → auditoria
  → saúde/performance/jobs
```

## 4. O que será diferencial para medicina integrativa

- conteúdo com **data de revisão** e responsável pela revisão;
- referências bibliográficas por aula/curso;
- disclosure de conflito de interesse;
- tag de “conteúdo educacional — não substitui julgamento clínico” onde necessário;
- informações de nível, público profissional e pré-requisitos;
- componentes para `Evidence note`, `Clinical pearl`, `Caution`, `Practice reflection` e `Reference list`;
- linguagem visual que una ciência, natureza e cuidado sem prometer cura ou resultados clínicos;
- separação explícita entre **educação** e **orientação médica individual**.

## 5. Anti-patterns rejeitados

- estética de “detox”, cristais, folhas em toda a UI ou linguagem pseudocientífica;
- claims como “cura”, “reverte”, “garantido” sem base e revisão apropriadas;
- professor apresentado apenas por autoridade social sem credenciais verificáveis;
- cards com dezenas de badges;
- dashboard com números sem ação associada;
- dark mode como única identidade;
- verde pastel com contraste insuficiente;
- animações orgânicas excessivas em tarefas clínicas/acadêmicas;
- gamificação infantilizada para público profissional.

## 6. Fontes consultadas

- Coursera — https://www.coursera.org/
- MasterClass — https://www.masterclass.com/
- Osmosis — https://www.osmosis.org/ e https://www.osmosis.org/features
- AMBOSS — https://www.amboss.com/int e https://www.amboss.com/us/features
- Lecturio — https://www.lecturio.com/medical/
- MedBridge — https://www.medbridge.com/educate
- Institute for Functional Medicine — https://www.ifm.org/education e https://www.ifm.org/certification
- NHS Digital Service Manual — https://service-manual.nhs.uk/
- Google Search Central Course structured data — https://developers.google.com/search/docs/appearance/structured-data/course

# Page override — Dashboard aluno

**Surface:** `Student Immersive`  
**UI/UX Pro Max dials:** variance 7 / motion 7 / density 5  
**North Star:** o aluno deve sentir continuidade, progresso e pertencimento profissional em menos de cinco segundos.

## Layout desktop

```text
256px learning sidebar
        │
        ├─ top search + notifications + user
        │
        ├─ immersive editorial hero
        │    saudação + mensagem + contexto visual
        │
        ├─ Continue de onde parou
        │    curso atual + progresso + CTA
        │
        ├─ Meus cursos em andamento
        │
        └─ Recomendado para você

right rail 300–340px
        ├─ Minha jornada
        ├─ Próxima aula
        └─ Marcos profissionais / recursos
```

## Visual

- background verde-petróleo profundo; não preto puro;
- sidebar pode incorporar fotografia/botânico discreto em zona não operacional;
- hero usa fotografia humana/profissional/natureza contextual com overlay escuro estável;
- Source Serif 4 permitida em saudação/headline editorial; Inter em controles/dados;
- progress e próxima ação devem permanecer mais importantes que métricas secundárias;
- right rail usa poucas surfaces, não mosaico de cartões idênticos;
- cards de curso podem usar fotografia/ilustração real contextual;
- “conquistas” são **marcos profissionais**: conclusão, consistência, certificado, trilha — sem moedas, XP, ranking ou gamificação infantil.

## Componentes

```text
StudentShell
LearningSidebar
StudentHero
ContextualSearch
ContinueLearningCard
ImmersiveCourseCard
JourneyProgress
UpcomingLessonCard
ProfessionalMilestone
RecommendedLearningRail
```

## Motion

- hero content: opacity + y 8–14px, 280–380ms;
- sidebar active indicator: 160–220ms;
- continue card: reveal 220–300ms, sem atrasar CTA;
- course cards: hover translateY <=2px / image scale <=1.02;
- progress: interpolar somente quando houve mudança real;
- right rail: stagger opcional 40–60ms, máximo 3 blocos;
- dashboard → lesson pode usar shared continuity de thumbnail/título quando estável;
- reduced motion remove transforms/stagger e preserva conteúdo imediato.

## Mobile

- sidebar vira drawer/bottom navigation apropriada ao IA final;
- hero reduz altura; headline continua legível sem cobrir rosto/foco da imagem;
- right rail vira fluxo abaixo do conteúdo principal;
- próxima ação aparece antes de recomendações;
- evitar horizontal carousels como única forma de descobrir cursos.

## Não fazer

```text
6+ stat cards no topo
gráficos decorativos
neon/glow de IA
glassmorphism em todos os cards
background animado contínuo
parallax obrigatório
serif em inputs/labels/dados
badges de jogo/XP/ranking
```

# Integrative Medical Learning System — MASTER

**Status:** Source of Truth visual 1.2 — ICIBINA Experience System V5.8  
**Produto:** plataforma de cursos de medicina integrativa  
**Stack alvo:** React + Tailwind CSS v4 + shadcn/ui + 21st.dev + Motion

## 1. North Star

A experiência deve transmitir em menos de cinco segundos:

> **“Aqui eu estudo saúde com profundidade, clareza e credibilidade.”**

### Design principles

1. **Evidence before ornament** — informação e confiança vêm antes de efeitos.
2. **Calm, not sleepy** — visual sereno com contraste e hierarquia fortes.
3. **Human clinical** — profissionais e alunos reais; evitar banco de imagens artificialmente “zen”.
4. **Nature as accent** — botânico/terra como nuance, nunca como prova de eficácia.
5. **Progress is visible** — o aluno sempre sabe onde está e o próximo passo.
6. **Complexity on demand** — dashboards mostram resumo primeiro e detalhes por drill-down.
7. **Professional dignity** — sem gamificação infantilizada.

## 2. Visual language

### Keywords

```text
medical editorial
scientific calm
natural precision
modern academic
human warmth
quiet premium
```

### Avoid

```text
neon gradients
excessive glassmorphism
spa beige everywhere
leaf icons on every card
crystal/energy symbolism
dark cinematic styling used indiscriminately across operational surfaces
purple AI glow as default
floating blobs behind form fields
```

## 3. Color system

### Brand / light

| Token | Hex | Uso |
|---|---|---|
| `brand-950` | `#103B34` | texto/ênfase extrema |
| `brand-900` | `#165044` | primary hover/pressed |
| `brand-800` | `#1C6254` | **primary** |
| `brand-700` | `#2A7868` | links/secondary emphasis |
| `brand-500` | `#5AA08E` | gráficos/ornamento |
| `brand-200` | `#CDE2DA` | borders/selected subtle |
| `brand-100` | `#E7F1ED` | tint/background |
| `brand-50` | `#F3F8F6` | subtle section |

### Warm accent

| Token | Hex | Uso |
|---|---|---|
| `sand-700` | `#7A5A1E` | texto sobre fundo claro |
| `sand-500` | `#B78332` | detalhe/ícone |
| `sand-200` | `#E8D6B4` | highlight sutil |
| `sand-100` | `#F5ECDA` | fundos editoriais |

### Neutrals

| Token | Hex |
|---|---|
| `ink-950` | `#12211D` |
| `ink-800` | `#293A35` |
| `ink-600` | `#5D6B66` |
| `ink-400` | `#8C9994` |
| `ink-200` | `#D9E0DD` |
| `ink-100` | `#E9EEEC` |
| `canvas` | `#F8FAF7` |
| `surface` | `#FFFFFF` |

### Status

| Semântica | Hex principal | Fundo sugerido |
|---|---|---|
| Success | `#2E7D55` | `#EAF5EE` |
| Info | `#276A9A` | `#EAF3F9` |
| Warning | `#A15C00` | `#FFF3E0` |
| Danger | `#B42318` | `#FDECEA` |

`#1C6254` sobre branco possui contraste alto o suficiente para texto normal. Tokens devem ser revalidados automaticamente sempre que alterados.

### Dark mode

Dark mode é opcional para o lançamento, recomendado para player/estudo noturno se for implementado corretamente.

```text
background: #0F1715
surface:    #15211E
surface-2:  #1C2B27
foreground: #F5FAF7
muted:      #B4C2BD
primary:    #74C9B3
border:     #30433D
```

Nunca simplesmente inverter cores.

## 4. Typography

### Font families

- **UI / body:** `Inter`, fallback `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`.
- **Editorial accent (opcional em marketing/artigos):** `Source Serif 4`, fallback `Georgia, serif`.

Não usar serif em tabelas, forms, player controls ou dashboard operacional.

### Scale

```text
Display XL  56/64  700  public hero desktop
Display L   44/52  700
H1          36/44  700
H2          30/38  700
H3          24/32  650
H4          20/28  650
Body L      18/29  400
Body        16/25  400
Body S      14/21  400
Label       14/20  600
Meta        13/18  500
```

Mobile display reduz sem quebrar a hierarquia; body continua 16px.

## 5. Spacing

Base 4px, preferir múltiplos previsíveis:

```text
1=4  2=8  3=12  4=16  5=20  6=24
8=32 10=40 12=48 16=64 20=80 24=96
```

### Page rhythm

- público: section gap 64–96px desktop, 40–64px mobile;
- app: 24–40px entre grupos;
- card padding: 20–24px;
- compact admin rows: 12–16px vertical.

## 6. Radius and elevation

```text
radius-sm: 8px
radius-md: 12px
radius-lg: 16px
radius-xl: 24px
radius-full: 9999px
```

Não usar radius gigantesco em todos os containers.

Shadows:

```text
sm: 0 1px 2px rgba(18,33,29,.06)
md: 0 8px 24px rgba(18,33,29,.08)
lg: 0 16px 40px rgba(18,33,29,.10)
```

Preferir border + subtle shadow a cartões “flutuando” em excesso.

## 7. Grid

### Marketing

```text
max-width: 1200px
padding: 24px mobile / 32px tablet / 40px desktop
12-column desktop
```

### App

```text
sidebar: 256px expanded / responsive drawer mobile
content max-width: 1440px admin
content reading width: 760–880px lesson/article
```

O player pode ultrapassar reading width para mídia, mas transcrição/texto não.

## 8. Motion language

Motion deve parecer **calm precision**.

Durations:

```text
micro: 120–160ms
standard: 180–240ms
enter panel: 240–320ms
page choreography: <= 420ms
```

Easing:

```text
standard: cubic-bezier(.2,.8,.2,1)
exit: cubic-bezier(.4,0,1,1)
```

Use spring apenas em drag/reorder ou interações físicas claras. Nada de bounce em pagamento, segurança ou conteúdo clínico.

`prefers-reduced-motion: reduce` remove transform/scroll choreography e mantém apenas feedback essencial.

## 9. Iconography

Lucide como baseline.

- stroke 1.75–2;
- 16px meta, 20px controls, 24px navigation;
- icon-only button sempre tem accessible name;
- não usar emoji como ícone de interface.

Ilustrações médicas devem ter legenda/alt apropriado e origem/licença registrada.

## 10. Photography

### Preferir

- docentes reais em ambientes claros/profissionais;
- contexto de ensino e prática;
- diversidade real;
- luz natural controlada;
- anatomia/ciência apenas quando relevante.

### Evitar

- médico genérico com prancheta olhando câmera em todos os banners;
- “mãos segurando planta” como shorthand de medicina integrativa;
- imagens de suplementos como hero institucional;
- imagens que impliquem resultado clínico garantido.

## 11. Buttons

### Primary

- fundo `brand-800`, texto branco;
- hover `brand-900`;
- min-height 44px;
- radius 10–12px;
- sem gradiente.

### Secondary

- surface + border `brand-200`;
- texto `brand-900`.

### Destructive

- danger somente para ação destrutiva real;
- confirmação descreve objeto/efeito.

### Link button

Para ações terciárias; não substituir links navegacionais sem necessidade.

## 12. Forms

- label sempre visível;
- hint abaixo do label;
- erro abaixo do campo e associado por `aria-describedby`;
- estado focus usa ring com contraste forte;
- required não depende apenas de asterisco;
- não apagar valor após erro;
- máscaras não devem impedir paste/autofill.

## 13. Cards

### CourseCard

Hierarquia:

```text
thumbnail 16:9
category/level (máx 2 badges)
title (2–3 linhas)
instructor
duration / format
price/CTA quando público
progress quando aluno
```

Não misturar preço + progresso + status editorial no mesmo card; cada superfície possui variante própria.

### StatCard

Número + label + delta/context. Todo KPI deve responder “o que devo fazer com isso?”.

## 14. Medical educational patterns

### EvidenceNote

Fundo informativo suave, título “Evidência e contexto”, referências associadas e data de revisão quando pertinente.

### ClinicalPearl

Destaque discreto em brand/sand; nunca parecer guideline oficial se não for.

### ClinicalCaution

Warning/danger conforme severidade. Ícone + título + texto; nunca apenas amarelo/vermelho.

### ContentReviewStamp

```text
Revisado em 12 set 2026
Revisão científica: Nome, credencial
```

Evitar selo “aprovado cientificamente” genérico.

## 15. Charts

Admin/professor:

- line: evolução temporal;
- bar: comparação discreta;
- progress/funnel: conversão/conclusão;
- donut somente para 2–5 partes simples.

Regras:

- legenda textual;
- tooltip com valor;
- não depender só de cor;
- eixo/escala honestos;
- paleta status não usada como paleta categórica arbitrária.

## 16. Accessibility baseline

WCAG 2.2 AA.

- foco sempre visível;
- skip link;
- headings sem pular níveis arbitrariamente;
- target ~44px;
- zoom até 200% sem perda de função;
- keyboard completo;
- captions/transcript quando disponível;
- formulários com error summary em fluxos longos;
- nenhum accessibility overlay/widget como substituto de acessibilidade real.

## 17. Responsive strategy

Mobile-first.

### Public

- hero empilha texto/imagem;
- cards 1 coluna → 2 → 3/4;
- filtros viram sheet no mobile.

### Student

- bottom/compact nav apenas se arquitetura de informação justificar;
- currículo de aula vira drawer;
- player 16:9 responsivo.

### Teacher/Admin

- sidebar vira drawer;
- tabelas críticas usam responsive column priority ou scroll controlado;
- ações primárias permanecem acessíveis sem hover.

## 18. Component governance

Componentes entram em `shared/components/ui` apenas se forem verdadeiramente genéricos. Componente de domínio permanece na feature.

21st.dev:

1. search;
2. inspect code/deps/license;
3. adapt tokens;
4. remove efeitos supérfluos;
5. accessibility review;
6. tests;
7. commit local — o produto não depende do registry em runtime.

## 19. Visual QA

Antes de considerar uma tela pronta:

```text
320/375px mobile
768px tablet
1280px desktop
1440px large dashboard
keyboard
200% zoom
light mode
reduced motion
loading/error/empty/success
long text/PT-BR
```

## 20. Page overrides

Consulte `pages/*.md`. Override pode especializar layout/densidade, mas não redefinir tokens sem ADR/design approval.


## 21. Supporting specifications

- `COMPONENTS.md` — anatomia/estados de componentes;
- `PATTERNS.md` — jornadas e padrões de produto;
- `CONTENT-GUIDE.md` — voz/microcopy/conteúdo médico;
- `ACCESSIBILITY.md` — WCAG 2.2 AA e QA.


## 22. Surface profiles — ICIBINA Experience System

A ICIBINA usa **quatro perfis canônicos**, todos derivados das mesmas foundations. A consistência vem de tokens, tipografia, componentes, acessibilidade e motion grammar compartilhados; a composição muda conforme a tarefa. Os únicos nomes válidos são:

```text
Editorial Light
Student Immersive
Operational Light
Operational Neutral
```

### A. Editorial Light

Uso padrão em site público, catálogo, course detail, checkout, auth, conteúdo jurídico e suporte.

- canvas claro `#F8FAF7` e surfaces brancas;
- hierarquia editorial, confiança e fotografia clínica/humana;
- Source Serif 4 somente como acento editorial;
- motion baixo/médio e funcional;
- compra/formulários priorizam legibilidade, previsibilidade e confiança.

### B. Student Immersive

Uso em dashboard do aluno, lesson player, biblioteca, trilhas e sessões de estudo.

- base verde-petróleo profunda, nunca preto puro;
- fotografia contextual de alta qualidade quando agrega narrativa;
- Source Serif 4 permitida em headings editoriais e acolhimento;
- Inter obrigatório em navegação, controles, dados e conteúdo operacional;
- overlays/gradientes existem para legibilidade, não para ornamentação neon;
- motion Tier 2/3 pode reforçar continuidade da aprendizagem;
- não usar gamificação infantil, glassmorphism em massa ou parallax obrigatório.

### C. Operational Light

Uso em teacher dashboard e course builder/autoria.

- foundations claras da marca;
- densidade média/alta, foco em autoria, status editorial, forms e organização;
- sem hero cinematográfico;
- motion baixo/médio para disclosure, reorder, feedback e continuidade de edição;
- componentes podem ser ricos, mas informação e produtividade vencem atmosfera.

### D. Operational Neutral

Uso em admin, operações, auditoria, financeiro, jobs, manutenção e observabilidade.

- alta densidade e leitura explícita de estado;
- tabelas/data grids e drill-downs priorizam dados;
- motion mínimo;
- unknown/error nunca são visualmente suavizados;
- sem fotografia decorativa, hero imersivo ou stagger de dashboard.

### Regra de escolha

```text
Descoberta/compra/conteúdo público?     -> Editorial Light
Aprendizagem pessoal/continuidade?       -> Student Immersive
Autoria/trabalho do professor?           -> Operational Light
Admin/operação/manutenção/auditoria?     -> Operational Neutral
```

Nenhuma página pode inventar um quinto perfil sem uma decisão explícita de Design System e atualização dos validators.

## 23. Experience quality bar

Uma tela ICIBINA de produção não é considerada pronta apenas porque “funciona”. Para rotas visuais importantes ela precisa demonstrar:

1. **hierarquia deliberada** — existe um foco principal claro;
2. **composição não-genérica** — evitar coleção uniforme de cards sem narrativa;
3. **continuidade** — próxima ação e estado atual são óbvios;
4. **profundidade controlada** — imagem, tipografia, sobreposição e motion com propósito;
5. **consistência sistêmica** — tokens e primitives locais prevalecem;
6. **movimento funcional** — estado, entrada/saída, continuidade espacial ou feedback;
7. **acessibilidade** — tudo continua operável sem motion, mouse ou percepção de cor;
8. **performance** — animação não pode sacrificar INP/LCP ou criar layout thrash;
9. **credibilidade médica** — nenhum efeito visual reduz clareza de alerta/evidência/credencial;
10. **responsive real** — desktop, tablet e mobile são composições, não simples encolhimento.

## 24. Tool-assisted design workflow

UI/UX Pro Max, 21st.dev e Motion são **instrumentos de qualidade**, não autoridades paralelas ao Design System.

```text
MASTER + surface + page override
       ↓
UI/UX Pro Max bridge — pesquisa/critério/dials
       ↓
21st explore/search — referências e candidatos
       ↓
21st build — implementação orientada ao contexto
       ↓
Motion — movimento e continuidade onde agrega UX
       ↓
21st review + UI/UX audit
       ↓
Playwright + axe + visual + reduced motion
```

Regras:

- use `python scripts/uiux-pro-max.py ...`; não dependa de `CLAUDE_PLUGIN_ROOT`;
- `MASTER.md`, `SURFACES.md` e override da página vencem recomendação externa;
- não use componente externo sem adaptar tokens, semântica, dependências e a11y;
- não use motion para “mostrar que temos animação”;
- não persista resultado UI/UX Pro Max não verificado;
- não publique tema 21st sem autorização explícita;
- Motion MCP básico pode estar ativo por padrão; Motion+ é **opt-in** e nunca requisito de funcionalidade essencial.

## 25. Visual reference

A direção premium aprovada do dashboard do aluno está em `references/student-dashboard-premium-direction.png`. Ela calibra composição/atmosfera do `Student Immersive`, mas não substitui tokens, componentes, acessibilidade ou page override. A ordem de autoridade é: Master → surface/motion/components → page override → referência visual.

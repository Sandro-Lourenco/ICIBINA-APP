# Component specifications

Consulte `MASTER.md` para foundations. Este arquivo descreve anatomia, variantes e estados mínimos.

## 1. Global state matrix

Todo componente interativo precisa considerar, quando aplicável:

```text
default
hover (não exclusivo)
focus-visible
active/pressed
disabled
loading
error/invalid
selected/checked
read-only
```

Hover nunca contém a única informação necessária para operar.

## 2. Button

Sizes:

| Size | Height | Uso |
|---|---:|---|
| sm | 36px | tabelas/ações densas, quando target composto continua acessível |
| md | 44px | default |
| lg | 48px | CTA público |

Variants: `primary`, `secondary`, `outline`, `ghost`, `destructive`.

Regras:

- loading preserva largura e inclui texto acessível;
- icon-only >= 44×44 em touch e possui `aria-label`/accessible name;
- não usar destructive para “cancelar modal”.

## 3. Inputs

Anatomia:

```text
Label
Hint (opcional)
Control
Inline error / help
```

- altura default 44–48px;
- focus ring de 2px + offset, usando token de foco;
- `aria-invalid` e `aria-describedby` quando inválido;
- placeholder não é label.

## 4. Badge/Tag

Usos permitidos:

- status;
- categoria;
- nível;
- verificação.

Máximo recomendado de dois badges visíveis em `CourseCard`. Não usar badge como botão sem semântica interativa explícita.

## 5. Alert

Variants: info, success, warning, danger.

Anatomia:

```text
icon
heading curto
message
action opcional
```

`ClinicalCaution` usa a mesma fundação, mas semântica editorial específica.

## 6. Dialog / Sheet

- focus trap real;
- foco retorna ao trigger;
- ESC fecha quando seguro;
- destructive confirmation nomeia o objeto e impacto;
- mobile prefere sheet para filtros/navegação; diálogo para decisão curta.

## 7. Table / DataTable

Admin/professor:

- headers semânticos;
- sort com estado anunciado;
- filtros persistem em URL quando representam navegação/consulta;
- paginação server-side para grandes volumes;
- row action não depende de hover;
- coluna de status contém texto + ícone/cor.

## 8. CourseCard

### Public

```text
thumbnail
topic/level
title
instructor
duration/format
price/CTA context
```

### Student

```text
title
progress
last lesson/next lesson
continue CTA
```

### Teacher

```text
title
status editorial
last modified
students/summary optional
actions
```

Não reutilizar uma única variante com dezenas de boolean props; preferir composição/variants discriminadas.

## 9. VideoLessonShell

Desktop:

```text
player main
curriculum side panel
lesson metadata
content tabs below
```

Mobile: currículo em sheet/drawer.

Obrigatório:

- keyboard controls do player;
- legenda/transcrição quando disponibilizada;
- velocidade quando provider permitir;
- loading/error/retry;
- progresso não depende apenas de `ended` do vídeo se a regra de negócio for diferente.

## 10. EvidenceNote

Propósito: contextualizar evidência/referências.

Anatomia:

```text
label "Evidência e contexto"
summary
references link/list
review date optional
```

Não inferir “nível de evidência” automaticamente. Se houver classificação, ela precisa ser editorialmente definida e versionada.

## 11. ClinicalPearl

Destaque educacional curto. Máximo recomendado: 1–3 blocos por aula, salvo necessidade real. Não usar como CTA promocional.

## 12. ClinicalCaution

Para limitação, contraindicação, risco ou incerteza educacional relevante.

- warning/danger conforme política editorial;
- sempre texto explícito;
- não pode depender de tooltip.

## 13. ReferenceList

- citações numeradas/ordenadas;
- DOI/PMID/URL como link quando disponível;
- links externos indicados de forma acessível;
- não esconder todas as referências em modal se forem essenciais para a credibilidade da página.

## 14. ContentReviewStamp

Renderiza somente revisão válida.

```text
Revisado em DD MMM YYYY
Revisão: Nome, credencial verificada
```

Não usar selo genérico “cientificamente comprovado”.

## 15. CredentialBadge

Mostra credencial publicável/verificada, não texto livre. Tooltip pode explicar emissor/validade, mas informação essencial continua acessível sem hover.

## 16. ContinuingEducationBadge

Só existe para `course_education_credits.status=verified` e dentro da validade. Deve apresentar tipo, horas/créditos e entidade quando aplicável, sem sugerir reconhecimento além do documentado.

## 17. SystemHealthCard

Admin only.

```text
service name
status text
latency/freshness
last checked
link para detalhe
```

Nunca transformar “unknown” em verde. `unknown` é estado explícito.

## 18. PaymentStatus

Estados visuais mapeiam a state machine real. Não inventar status frontend. Exemplo:

```text
pending
paid
expired
refunded
chargeback
```

Mensagem de processamento explica eventual consistency sem afirmar pagamento antes do webhook.


## 19. PatientDataWarning

Componente obrigatório próximo de notas/casos/uploads clínicos.

```text
Ícone/label de privacidade
“Não inclua dados que identifiquem um paciente.”
Texto curto com exemplos (nome, documento, prontuário, imagem)
link opcional “Ver política de privacidade de casos”
```

Não pode depender apenas de cor; deve ser anunciado por screen reader. Backend continua responsável por policy/validação.


## 20. StudentShell

Container da experiência `Student Immersive`.

```text
LearningSidebar
TopContextBar
MainLearningContent
OptionalJourneyRail
```

- sidebar desktop 256px; mobile vira navegação adequada ao IA final;
- não aplica blur/translucência global;
- preserva skip link, landmarks e foco;
- surface profile é contexto visual, não autorização para mudar semântica dos primitives.

## 21. StudentHero

Hero editorial do aluno; não é banner promocional.

Anatomia:

```text
contextual greeting
editorial headline/message
optional supporting sentence
optional primary learning CTA
high-quality image with contrast overlay
```

Regras:

- não esconder informação essencial na imagem;
- rosto/focal point respeitado em crops responsivos;
- texto mantém contraste em todas as imagens aprovadas;
- máximo uma área hero forte por dashboard;
- Motion segue `MOTION.md`.

## 22. JourneyProgress

Resumo profissional da jornada, não gamificação.

```text
overall progress
courses in progress
lessons completed
study time (quando confiável)
certificates/milestones
```

- valores vêm do backend/analytics real;
- ring/chart sempre possui texto equivalente;
- animação não simula crescimento inexistente.

## 23. ImmersiveCourseCard

Variação Student de `CourseCard`.

- imagem contextual;
- category/track opcional;
- title + instructor;
- progress + current/next context;
- CTA principal previsível;
- no máximo 1–2 badges;
- hover não é requisito para descobrir ação.

## 24. ProfessionalMilestone

Representa progresso profissional/educacional sem XP/ranking.

Exemplos válidos:

```text
primeiro curso iniciado
trilha concluída
certificado emitido
consistência de estudo informativa
módulo clínico concluído
```

Evitar fire emoji, coins, levels, ranking competitivo ou manipulação de streak para retenção.

## 25. ContextualSearch

Search da área logada com escopo explícito (curso/aula/recurso). Pode abrir command palette no desktop quando justificável.

- shortcut exibido somente se funcional;
- resultados agrupados semanticamente;
- keyboard-first;
- empty/error/loading claros;
- mobile usa interação apropriada, não campo minúsculo persistente.

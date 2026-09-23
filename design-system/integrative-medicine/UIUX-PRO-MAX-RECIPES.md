# UI/UX Pro Max — ICIBINA Recipes

Estas recipes operacionalizam a skill sem permitir que ela substitua o Design System. Resultados são **pesquisa de design**; `MASTER.md` e o override da página continuam canônicos.

## Regras

- use `--design-system` somente para nova superfície, redesign substancial ou validação de direção;
- nunca use `--force` no Master sem decisão explícita de produto/design;
- use consulta estreita por `--domain` para problemas locais;
- registre a query e as recomendações efetivamente adotadas no handoff de UI relevante;
- descarte recomendações que conflitem com acessibilidade, credibilidade médica ou tokens ICIBINA.


## Invocação canônica portátil

Na ICIBINA **não use** `CLAUDE_PLUGIN_ROOT` diretamente. Codex e Antigravity instalam a skill em caminhos diferentes. Use sempre o bridge:

```bash
python scripts/uiux-pro-max.py "<query>" --design-system --variance 7 --motion 7 --density 5 -p "ICIBINA"
```

Diagnóstico:

```bash
python scripts/uiux-pro-max.py --print-path
```

O bridge localiza a skill revisada no workspace Antigravity, bundle Codex/Antigravity ou cache ativo do Codex e repassa todos os argumentos ao `search.py` original.

## Dials recomendados

| Superfície | Variance | Motion | Density |
|---|---:|---:|---:|
| Home pública | 6 | 5 | 3 |
| Course detail | 5 | 4 | 4 |
| Student dashboard | 7 | 7 | 5 |
| Lesson player | 4 | 5 | 5 |
| Biblioteca/trilhas | 6 | 6 | 5 |
| Teacher dashboard | 4 | 3 | 7 |
| Course builder | 3 | 4 | 8 |
| Admin | 2 | 2 | 8 |
| Checkout | 3 | 2 | 4 |
| Auth | 3 | 3 | 3 |

Esses valores definem **intensidade de exploração**, não quantidade obrigatória de animações.

## Student Dashboard

Consulta de direção:

```text
professional medical education student dashboard premium immersive dark editorial learning progress
```

Resultado desejado:

```text
medical editorial
scientific calm
premium immersive learning
human photography
progress hierarchy
non-gamified professional milestones
```

Pesquisas detalhadas úteis:

```text
"dark dashboard focus contrast" --domain ux
"learning dashboard hierarchy" --domain ux
"medical education premium" --domain style
"editorial academic serif sans" --domain typography
"progress dashboard accessible" --domain chart
```

## Lesson Player

```text
professional medical learning video player dark focused curriculum transcript references
```

Priorizar:

- player e conteúdo, não decoração;
- navegação de currículo previsível;
- transcrição/recursos/referências;
- controles acessíveis;
- baixa distração.

## Public / Course Detail

```text
medical education editorial premium evidence trust course detail professional
```

Priorizar credenciais, conteúdo, clareza de compra e prova editorial — não estética wellness.

## Admin / Teacher

Use consultas direcionadas a densidade, hierarchy, forms, tables, filters e responsive behavior. Não solicitar direção “cinematic” ou “immersive” para operações.

## Acessibilidade

Para problemas específicos, buscar o outcome semântico antes da stack, por exemplo:

```text
focus not obscured
error summary validation
icon button accessible label
live progress screen reader
reduced motion dashboard
```

## Handoff

Para nova página/redesign, registrar:

```text
uiux_query:
uiux_mode: design-system | domain | stack
uiux_dials: variance/motion/density
adopted_guidance:
rejected_guidance + reason:
```

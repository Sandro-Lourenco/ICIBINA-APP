# ICIBINA Surface Profiles — V5.8

Fonte complementar ao `MASTER.md`. Existem **quatro perfis canônicos**; page overrides devem usar exatamente um destes nomes.

## 1. Editorial Light

**Rotas:** público, catálogo, course detail, checkout, auth, jurídico e suporte.

```text
background     #F8FAF7
surface        #FFFFFF
primary        #1C6254
accent         #B78332
UI font        Inter
editorial font Source Serif 4 (uso seletivo)
```

Composição editorial clara, whitespace real, confiança, fotografia contextual e motion baixo/médio.

## 2. Student Immersive

**Rotas:** dashboard aluno, lesson player, biblioteca, trilhas, sessões de estudo.

```text
background        #071613
surface           #0D211D
surface-elevated  #14312B
foreground        #F5FAF7
muted             #B6C9C1
border            #55766C
primary           #8AD6C0
accent            #D9B66E
focus             #78BCE5
```

- sidebar fixa/drawer com navegação simples;
- hero fotográfico/editorial somente com valor narrativo;
- uma ação dominante no viewport inicial;
- right rail opcional para jornada/próxima aula/agenda;
- serif seletiva em headings; controles e dados continuam Inter;
- overlays estáveis atrás de texto sobre fotografia;
- motion médio/alto, deliberado, com reduced-motion equivalente.

## 3. Operational Light

**Rotas:** teacher dashboard, course builder e autoria.

- foundations claras da marca;
- densidade média/alta;
- forms, conteúdo, workflow editorial e reorder em primeiro plano;
- motion baixo/médio;
- sem hero cinematográfico, wallpaper decorativo ou glassmorphism generalizado.

## 4. Operational Neutral

**Rotas:** admin, operações, auditoria, financeiro, observabilidade e manutenção.

- densidade alta;
- dados e status explícitos;
- motion mínimo;
- sem hero, fotografia decorativa ou efeitos imersivos;
- unknown/error são estados explícitos.

## 5. Surface matrix

| Superfície | Perfil | Variance | Motion | Density | Serif | Imagem hero |
|---|---|---:|---:|---:|---|---|
| Home pública | Editorial Light | 6 | 5 | 3 | sim, seletiva | sim |
| Course detail | Editorial Light | 5 | 4 | 4 | sim, seletiva | opcional |
| Dashboard aluno | Student Immersive | 7 | 7 | 5 | sim, heading | sim |
| Lesson player | Student Immersive | 4 | 5 | 5 | mínimo | não dominante |
| Biblioteca/trilhas | Student Immersive | 6 | 6 | 5 | seletiva | opcional |
| Professor | Operational Light | 4 | 3 | 7 | não | não |
| Course builder | Operational Light | 3 | 4 | 8 | não | não |
| Admin | Operational Neutral | 2 | 2 | 8 | não | não |
| Checkout | Editorial Light | 3 | 2 | 4 | não | não |
| Auth | Editorial Light | 3 | 3 | 3 | mínimo | opcional |

Os valores são dials de pesquisa/decisão, não CSS numérico direto.

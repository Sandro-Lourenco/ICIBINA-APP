# 27 — Governança de conteúdo médico e educacional

## 1. Objetivo

Uma plataforma de medicina integrativa precisa diferenciar conteúdo educacional de aconselhamento clínico individual e tornar autoria, revisão, evidências e conflitos transparentes.

## 2. Metadados editoriais mínimos por curso

```text
learning objectives
target audience
prerequisites
education level
estimated duration
instructor(s)
instructor credentials
published_at
last_content_review_at
next_review_due_at (quando política exigir)
reviewed_by
conflict_of_interest/disclosure
references
credit/accreditation metadata somente quando validado
```

## 3. Metadados por aula quando aplicável

- referências bibliográficas;
- data de atualização;
- clinical reviewer;
- materiais anexos versionados;
- aviso educacional em tópicos sensíveis.

## 4. Workflow editorial

```text
draft
  → editorial review
  → scientific/clinical review quando requerido
  → changes requested
  → approved
  → published
  → scheduled review
  → archived/superseded
```

Professor não pode “autoaprovar” conteúdo que a política classifique como exigindo revisão independente.

## 5. Componentes de conteúdo

### Evidence Note

Resume o que uma referência realmente sustenta. Não deve gerar grau de evidência automaticamente por IA.

### Clinical Pearl

Dica educacional de aplicação/conexão conceitual. Não é prescrição individual.

### Caution

Risco, contraindicação, limitação ou incerteza que merece destaque.

### Reference List

Citações persistentes e exportáveis. Quando possível armazenar DOI/PMID/URL e data de acesso.

## 6. IA em conteúdo

IA pode auxiliar rascunho, resumo, questões e revisão editorial, mas:

- não publica claim médico automaticamente;
- não inventa referência;
- conteúdo gerado precisa rastrear revisão humana quando publicado como material oficial;
- prompts não incluem dados pessoais de pacientes;
- qualquer ferramenta de IA integrada deve ter política de dados e disclosure adequado.

## 7. Conflito de interesse

Docente/editor declara conflitos relevantes. Administração mantém histórico da declaração; UI apresenta disclosure de forma proporcional ao contexto.

## 8. Acreditação/CE/CME

Nunca mostrar selo, créditos ou linguagem de acreditação sem evidência contratual/documental correspondente.

Arquitetura deve permitir metadados, mas a ativação de cada acreditador é uma configuração de negócio/compliance.

## 9. Health literacy

Mesmo com público profissional:

- títulos objetivos;
- siglas expandidas na primeira ocorrência;
- tabelas/figuras com legenda;
- não esconder informação de risco atrás de hover;
- texto de marketing separado de conteúdo científico;
- claim forte deve ser sustentado e revisado.


## 10. Brasil / conteúdo público

Para comunicação e credenciais de médicos no Brasil, seguir `docs/56-BRASIL-COMPLIANCE-MEDICAL-CONTENT.md`. Casos, notas e uploads seguem `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md`.

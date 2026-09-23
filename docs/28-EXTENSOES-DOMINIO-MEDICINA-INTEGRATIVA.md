# 28 — Extensões de domínio para medicina integrativa

Este documento conecta governança médica, banco, API e UX para evitar que o design system descreva dados que o backend não consegue representar.

## 1. Novas capacidades de domínio

### Credenciais do professor

Entidade/aggregate support para:

```text
tipo/título da credencial
instituição emissora
jurisdição
identificador quando publicável
verificação
validade
visibilidade pública
```

Nunca assumir credencial a partir de texto livre no perfil.

### Referências

Curso e aula podem ter referências ordenadas com DOI/PMID/URL quando disponíveis. Citation text permanece obrigatório para não depender de provider externo em runtime.

### Disclosure

Cada docente associado a um curso pode ter declaração de conflito de interesse. Histórico relevante é auditável.

### Content Review

Tipos:

```text
editorial
scientific
clinical
compliance
```

Estados:

```text
pending
changes_requested
approved
rejected
superseded
```

### Education credits

Metadados de crédito/acreditação são opcionais e só aparecem publicamente com `status=verified` e validade aplicável.

## 2. Blueprint SQL

`database/002_medical_education_extensions.sql` descreve as tabelas de referência. Na implementação real converter para Alembic e revisar modelagem com o código existente.

## 3. API additions alvo

### Público

```text
GET /api/v1/courses/{slug}
  instructor_credentials[]
  last_content_review_at
  review_summary
  disclosures[]
  references_summary
  education_credits[] somente verified/válidos
```

### Professor/authoring

```text
PUT /api/v1/teacher/courses/{id}/references
PUT /api/v1/teacher/courses/{id}/disclosure
GET /api/v1/teacher/courses/{id}/review-status
POST /api/v1/teacher/courses/{id}/submit-review
```

### Admin/editorial

```text
GET  /api/v1/admin/content-reviews
POST /api/v1/admin/content-reviews/{id}/decision
GET  /api/v1/admin/instructor-credentials
POST /api/v1/admin/instructor-credentials/{id}/verify
GET  /api/v1/admin/education-credits
POST /api/v1/admin/education-credits/{id}/verify
```

Nomes finais devem ser refletidos pelo OpenAPI; esta lista é contrato-alvo, não desculpa para duplicar endpoints existentes.

## 4. Publicação

Policy engine de publicação pode exigir, por categoria de curso:

```text
learning objectives presentes
professor com credencial aplicável
references mínimas quando política exigir
disclosure preenchido
scientific/clinical review approved quando exigido
```

A regra deve ser configurável e auditável; não hardcode “todo curso exige exatamente N referências”.

## 5. UI mapping

- `CredentialBadge` lê apenas credenciais verificadas/publicáveis;
- `ContentReviewStamp` não aparece se não houver revisão válida;
- `ContinuingEducationBadge` só renderiza créditos verificados;
- `ReferenceList` não gera/infere referências via IA;
- `ClinicalCaution` é bloco de conteúdo editorial, não diagnóstico automático.

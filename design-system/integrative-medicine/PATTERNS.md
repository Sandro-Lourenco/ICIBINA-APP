# Product patterns

## 1. Learning loop

```text
Watch / Read
  → Understand
  → Practice
  → Review
  → Continue
```

A UI deve facilitar o próximo passo e evitar menu hunting.

## 2. Continue learning

No dashboard do aluno, o bloco prioritário mostra um único próximo passo principal. Cursos adicionais aparecem depois.

## 3. Course discovery

Filtros úteis para o domínio:

```text
tema
nível
formato
carga horária
professor
trilha
status de crédito educacional (se aplicável)
```

Não criar filtros sem volume suficiente para justificá-los.

## 4. Evidence transparency

Em course detail e aula:

- credenciais próximas do nome do docente;
- review metadata acessível mas não dominante;
- referências no conteúdo, não apenas footer jurídico;
- disclosure disponível.

## 5. Publish checklist

Antes de publicação:

```text
conteúdo essencial preenchido
objetivos
currículo
preview
referências conforme policy
disclosure
review approvals conforme policy
preço/checkout config
a11y de mídia quando aplicável
```

## 6. Payment processing

Estados:

```text
iniciando checkout
redirecionado ao Asaas
retorno recebido
aguardando confirmação
confirmado -> matrícula
falhou/expirou -> tentativa nova
```

A interface nunca promove estado baseado em query param do redirect.

## 7. Operational remediation

Admin vê problema → detalhe → causa segura → ação permitida (retry/reconcile) → audit event. Nunca terminal/SQL livre.

## 8. Empty states

Empty state deve explicar o porquê e a próxima ação. Exemplo professor sem cursos:

> “Você ainda não criou cursos. Comece estruturando objetivos, módulos e aulas.”

CTA: `Criar primeiro curso`.

## 9. Progressive disclosure

- público: detalhes científicos aprofundados em seções;
- player: conteúdo principal primeiro, referências em seção próxima;
- admin: summary → drill-down;
- forms longos: seções e progress, sem wizard desnecessário.


## 10. Immersive learning composition

Para dashboard/player do aluno, evitar o padrão genérico “header + 12 stat cards”. A composição deve criar narrativa:

```text
orientação pessoal
→ próxima ação
→ progresso contextual
→ cursos em andamento
→ agenda/jornada
→ descoberta secundária
```

Imagem e motion servem essa narrativa; não substituem conteúdo.

## 11. Motion as continuity

Motion deve responder pelo menos uma pergunta:

```text
O que mudou?
De onde veio?
Para onde foi?
Qual estado está ativo?
Qual ação foi reconhecida?
```

Se não responde nenhuma, prefira não animar.

## 12. Visual depth without UI noise

Prioridade para profundidade:

```text
1. hierarchy
2. typography
3. photography
4. spacing
5. contrast
6. subtle overlay/elevation
7. motion
```

Não começar por glow, blur, gradient ou shadow.

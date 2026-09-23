# Content & Voice Guide

## 1. Voz

A marca fala como um **educador clínico contemporâneo**: clara, precisa, respeitosa e serena.

### Características

```text
Clara, não simplista
Confiante, não absoluta
Acolhedora, não informal demais
Científica, não burocrática
Humana, não “zen” genérica
```

## 2. Marketing

Prefira:

- “Compreenda os fundamentos…”
- “Explore abordagens e evidências…”
- “Desenvolva raciocínio…”
- “Atualize sua prática dentro do seu escopo profissional…”

Evite sem revisão jurídica/editorial:

- “cura”;
- “reverte doenças”;
- “resultado garantido”;
- “detox definitivo”;
- “100% natural = seguro”;
- superlativos clínicos não demonstrados.

## 3. CTAs

Público:

```text
Explorar cursos
Ver programa
Conhecer o professor
Começar curso
```

Aluno:

```text
Continuar aula
Revisar conteúdo
Fazer avaliação
Ver certificado
```

Professor:

```text
Salvar rascunho
Enviar para revisão
Visualizar como aluno
Publicar (quando policy permitir)
```

Admin:

```text
Revisar
Solicitar alterações
Reprocessar evento
Revogar acesso
```

Evitar “Clique aqui”.

## 4. Erros

Formato:

```text
O que aconteceu
O que o usuário pode fazer agora
ID de suporte quando útil
```

Não expor stack trace, provider secret ou detalhes de segurança.

## 5. Pagamento

Antes da confirmação por webhook:

> “Recebemos o retorno do pagamento e estamos confirmando a transação. Isso pode levar alguns instantes.”

Não escrever “Pagamento aprovado” baseado apenas em redirect do browser.

## 6. Conteúdo médico

- expandir siglas na primeira ocorrência;
- separar opinião do docente de evidência citada;
- mostrar data de revisão quando política exigir;
- linguagem de risco é direta, sem alarmismo;
- não personalizar conduta para um paciente real dentro do curso sem contexto legal/privacidade apropriado.

## 7. IA

Se houver assistente futuro:

- identificá-lo como IA;
- informar limites;
- impedir coleta desnecessária de dados pessoais/sensíveis;
- respostas educacionais devem apontar para fontes internas/conteúdo aprovado quando possível;
- não usar linguagem que o faça parecer médico responsável pelo usuário.


## 8. Dados de pacientes

Nunca peça ou normalize dados identificáveis de pacientes. Em notas, casos e uploads clínicos use o componente `PatientDataWarning` e a copy canônica de `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md`. Prefira casos sintéticos/desidentificados; não trate remoção de nome como anonimização comprovada.

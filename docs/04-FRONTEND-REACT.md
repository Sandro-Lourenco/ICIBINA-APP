# 04 — Frontend React

## Stack

```text
React 19.3
Vite 8
TypeScript strict
Tailwind CSS v4
shadcn/ui
21st.dev components como inspiração/código local
Lucide icons
Motion for React (motion/react)
TanStack Query v5
React Hook Form
Zod
Vitest + Testing Library
Playwright
```

O pacote de skills inclui uma skill React que pode citar 19.2; como a versão oficial atual é 19.3, em conflito de detalhes de versão, **React oficial prevalece**.

## Estrutura por feature

```text
frontend/src/
├─ app/
│  ├─ router/
│  ├─ providers/
│  └─ layouts/
├─ features/
│  ├─ auth/
│  ├─ catalog/
│  ├─ checkout/
│  ├─ student/
│  ├─ teacher/
│  └─ admin/
├─ shared/
│  ├─ api/
│  ├─ components/
│  ├─ config/
│  ├─ hooks/
│  ├─ schemas/
│  ├─ types/
│  └─ utils/
└─ styles/
```

Dentro de uma feature:

```text
student/
├─ api/
├─ components/
├─ pages/
├─ queries/
├─ schemas/
├─ hooks/
└─ index.ts
```

## API client

Centralize `fetch`.

```ts
export class ApiError extends Error {
  constructor(
    public status: number,
    public code: string,
    message: string,
    public details?: unknown,
  ) {
    super(message)
  }
}

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${env.apiUrl}${path}`, {
    ...init,
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...init?.headers,
    },
  })

  if (!response.ok) {
    const body = await response.json().catch(() => null)
    throw new ApiError(
      response.status,
      body?.error?.code ?? 'UNKNOWN_ERROR',
      body?.error?.message ?? 'Falha na requisição',
      body?.error?.details,
    )
  }

  return response.status === 204 ? (undefined as T) : response.json()
}
```

## Refresh de autenticação

O refresh token fica em cookie HttpOnly. O JS não deve ler esse token.

Estratégia:

```text
request -> 401 TOKEN_EXPIRED
    -> POST /auth/refresh com credentials include
        -> retry original uma única vez
```

Implemente mutex/single-flight para evitar 15 refreshes simultâneos quando uma página dispara múltiplas queries.

## TanStack Query

Use para dados do servidor:

```ts
queryKey: ['student', 'courses']
queryKey: ['course', courseId]
queryKey: ['teacher', 'course', courseId]
queryKey: ['admin', 'payments', filters]
```

Mutations devem invalidar somente queries afetadas.

Não copie resposta do servidor para Zustand.

## Rotas

```text
/
/cursos
/cursos/:slug
/professores/:slug
/login
/cadastro
/pagamento/processando

/aluno
/aluno/cursos
/aluno/cursos/:courseId/aulas/:lessonId
/aluno/avaliacoes
/aluno/certificados
/aluno/compras
/aluno/perfil

/professor
/professor/cursos
/professor/cursos/novo
/professor/cursos/:id/editar
/professor/cursos/:id/alunos
/professor/cursos/:id/analytics
/professor/avaliacoes
/professor/lives

/admin
/admin/usuarios
/admin/professores
/admin/cursos
/admin/pagamentos
/admin/webhooks
/admin/auditoria
/admin/operacoes
/admin/jobs
/admin/manutencao
/admin/configuracoes
```

## Guards

Guard no frontend melhora UX, **não segurança**.

```text
RequireAuth
RequireRole('teacher')
RequireRole('admin')
```

Toda autorização é repetida no backend.

## Bootstrap shadcn + primitive layer

Antes do primeiro intake de componente 21st no frontend real, siga `docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md`: Tailwind v4, aliases, `components.json`, tokens ICIBINA e primitive layer shadcn precisam estar configurados e revisados.

## Design system

A fonte canônica é `design-system/integrative-medicine/MASTER.md`, complementada por `pages/*.md`. O produto já possui direção visual definida; **não gere um novo design system por tarefa**.

Fluxo obrigatório para nova página/redesign/fluxo visual relevante:

1. leia o `MASTER.md`;
2. leia o page override correspondente;
3. execute `python scripts/check-frontend-agent-stack.py --strict`;
4. use UI/UX Pro Max para consulta/auditoria direcionada ao problema — nunca para substituir automaticamente o Master;
5. reutilize componente local existente;
6. se não houver equivalente local e for um padrão visual genérico, pesquise 21st.dev antes de hand-code (`21st-ui-explore` / `21st-cli-use` / `21st-ui-build`);
7. implemente com a skill React e a estrutura por feature deste documento;
8. use Motion somente para feedback/continuidade; Tier 2/3 consulta `$motion-experience-orchestrator` e Motion MCP público;
9. para UI relevante, rode `21st-ui-review` quando disponível e faça auditoria final com UI/UX Pro Max;
10. execute visual regression + axe nas rotas críticas.

O detalhamento e a matriz por tipo de tarefa estão em `docs/31-FRONTEND-AGENT-WORKFLOW.md`.

Tokens de referência existem em `design-system/integrative-medicine/tokens.css` e `tokens.json`. Não espalhe hex arbitrário em componentes.

Direção: **medical editorial + scientific calm + natural precision**; evitar estética mística/wellness genérica.

## Motion / antigo Framer Motion

O projeto usa o pacote moderno `motion`; pedidos que mencionem “Framer Motion” devem ser implementados com a API atual quando compatível. Para animação não trivial, consulte o **orquestrador local Motion** e o Motion MCP público antes de implementar; a skill upstream do Motion AI Kit não é redistribuída enquanto sua licença no commit pinado permanecer sem declaração verificável. Para hover/focus/transições simples, prefira CSS.

Import atual:

```ts
import { motion, AnimatePresence } from 'motion/react'
```

Use para:

- page/section transition discreta;
- expansão de cards;
- reorder visual no builder;
- feedback de upload;
- modal/sheet;
- progress indicator.

Evite animações longas no dashboard operacional.

Regras adicionais:

- prefira `transform` e `opacity` em animações frequentes;
- reduced-motion deve preservar estado final, foco e compreensão;
- pagamento, segurança, erros críticos e conteúdo clínico usam motion mínimo, sem bounce/choreography decorativa;
- quando Motion MCP/Motion+ oferecer auditoria/performance tooling autorizado, use-o nas animações complexas e registre o resultado no handoff.

## Estados obrigatórios

Todo componente que depende de rede precisa representar:

```text
loading
error
empty
success
```

Evite spinner para páginas inteiras; prefira skeleton que preserve layout.

## Acessibilidade

- contraste >= WCAG AA;
- foco visível;
- controles por teclado;
- touch target ~44x44px;
- label real em form;
- mensagem de erro associada ao campo;
- `aria-live` para status assíncrono importante;
- legenda/transcrição em vídeo quando disponível;
- não comunicar status apenas por cor.

## Performance

- route-level lazy loading;
- imagens AVIF/WebP com dimensões;
- player carregado somente quando necessário;
- prefetch moderado da próxima aula;
- tabelas administrativas virtualizadas apenas quando volume justificar;
- não carregar bibliotecas de charts na área pública se só o admin usa;
- Core Web Vitals monitorados em produção: LCP <= 2.5s, INP <= 200ms e CLS <= 0.1 no p75 como alvo de boa experiência.


### React 19.3
Para comportamento específico de versão, leia `docs/59-REACT-19.3-DELTA.md`; documentação oficial React prevalece sobre a skill externa.


## Experience System V5.7

Para UI, a implementação React deve seguir `docs/contracts/FRONTEND-CONTRACT.md` e o pipeline `docs/60-FRONTEND-DESIGN-EXCELLENCE-PIPELINE.md`. Surface profile, 21st sourcing e Motion grammar são parte do contrato de qualidade; não implementar uma estética paralela localmente.

# 25 — SEO e arquitetura pública

## 1. Separação de superfícies

Dashboards autenticados podem ser client-heavy SPA. Páginas públicas de aquisição precisam entregar HTML indexável e rápido.

Rotas SEO críticas:

```text
/
/cursos
/cursos/:slug
/professores/:slug
/trilhas/:slug        # se implementado
/artigos/:slug        # se implementado
```

## 2. Rendering contract

Para rotas públicas, adotar SSR/SSG/prerender compatível com o stack React/Vite. A decisão de biblioteca concreta pode ser implementada por ADR de frontend, mas o **contrato é obrigatório**:

- conteúdo principal presente no HTML inicial;
- status HTTP correto (404 real, redirect real);
- canonical estável;
- metadata por rota;
- hidratação sem layout shift relevante;
- dashboards privados não precisam ser indexáveis.

## 3. Metadados

Cada curso público:

```text
<title>
meta description
canonical
og:title
og:description
og:image
twitter card
```

Professor e organização também têm metadata específica.

## 4. Structured data

Quando aplicável e conforme diretrizes atuais do Google:

- `Course`;
- `ItemList` no catálogo/lista;
- `Organization`;
- `BreadcrumbList`;
- `ProfilePage` para docente quando semântica couber;
- `VideoObject` em previews públicos elegíveis.

Não colocar rating, acreditação, preço ou claims falsos apenas para rich results.

## 5. Sitemap e robots

Gerar sitemap a partir de recursos publicados. Não incluir drafts, páginas privadas ou URLs com filtros infinitos.

`robots.txt` não é mecanismo de autorização.

## 6. Slugs

- slug único e estável;
- mudança cria redirect 301 do slug anterior;
- tabela/history opcional para slugs alterados;
- não reutilizar slug antigo imediatamente para outro recurso.

## 7. Conteúdo médico e SEO

Confiança é prioridade sobre copy agressiva:

- autor/docente e credenciais;
- revisão e data de atualização;
- referências quando a página faz afirmações educacionais de saúde;
- disclosure;
- linguagem sem promessas clínicas não fundamentadas.

## 8. Quality gate

Antes de publicar rota pública:

```text
HTML sem JS contém conteúdo essencial
200/404/301 corretos
canonical correto
sitemap atualizado
structured data validado
LCP/INP/CLS dentro do budget ou issue registrada
```

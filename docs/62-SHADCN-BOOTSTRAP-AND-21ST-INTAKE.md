# 62 — shadcn/ui bootstrap e gate de intake do 21st.dev — V5.8

## Objetivo

Antes de permitir que 21st.dev adicione componentes ao frontend real, a ICIBINA precisa possuir uma fundação local previsível. `shadcn/ui` é **código local/primitive layer**, não uma dependência visual que redefine o Design System.

## Baseline revisada

- app: React 19.3 + Vite 8 + TypeScript;
- Tailwind CSS v4;
- shadcn CLI revisado/pinado em `toolchain-lock.json`;
- Lucide;
- tokens ICIBINA continuam autoridade visual.

## Sequência obrigatória no primeiro bootstrap do frontend

```text
criar frontend React/Vite real
        ↓
package.json + package-lock.json
        ↓
Tailwind v4 + alias @/*
        ↓
shadcn init com CLI pinado
        ↓
revisar components.json
        ↓
mapear tokens ICIBINA / globals
        ↓
instalar somente primitives base necessárias
        ↓
rodar lint/typecheck/test/build
        ↓
liberar 21st intake
```

Exemplo com o CLI **pinado**, não `latest` em automação reproduzível:

```bash
npx --yes shadcn@4.21.0 init
```

O comando pode mudar em upgrade futuro somente via PR que atualize `toolchain-lock.json` e revise o diff de `components.json`, CSS e dependências.

## `components.json` contract

Quando `frontend/package.json` real existir e o CLI shadcn for usado, `frontend/components.json` passa a ser obrigatório. Baseline esperada para app Vite client-side:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "css": "src/styles/globals.css",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks",
    "utils": "@/lib/utils"
  },
  "iconLibrary": "lucide"
}
```

`style`/`base` exatos são decisão explícita de bootstrap. Não aceite preset que sobrescreva a paleta, radius, typography ou surface profiles da ICIBINA sem revisão.

## Primitive boundary

```text
src/components/ui/       -> primitives locais shadcn/ICIBINA
src/shared/components/   -> composições reutilizáveis de produto
src/features/*           -> UI específica da feature
```

Não deixar o 21st instalar um segundo conjunto equivalente de `Button`, `Dialog`, `Input`, `Card`, `Tabs` etc. se a primitive local já existir.

## Gate antes de 21st.dev

Antes do primeiro `21st search/build` em implementação real:

```text
[ ] frontend/package.json + package-lock.json existem
[ ] Tailwind v4 ativo
[ ] alias do TypeScript/Vite resolvido
[ ] components.json revisado
[ ] tokens ICIBINA ligados ao CSS real
[ ] primitives base instaladas somente quando necessárias
[ ] lint/typecheck/build verdes
```

Só depois disso o fluxo `local primitive -> 21st search -> adapt -> review` pode operar sobre uma fundação estável.

## Reprodutibilidade

- CI usa `npm ci`;
- CLI shadcn não usa `latest` nos scripts automatizados;
- componentes adicionados pelo CLI entram no repositório como código revisável;
- dependências introduzidas por cada `shadcn add` ou 21st intake são revisadas e lockadas.

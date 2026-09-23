# ICIBINA Motion System

Motion for React (`motion/react`) é a implementação padrão para movimento não trivial. CSS continua preferido para feedback simples de hover/focus/color/opacity quando não há ganho de estado, layout ou continuidade.

## 1. Princípio

> Motion deve explicar mudança, preservar continuidade ou aumentar percepção de qualidade sem competir com o conteúdo médico.

## 2. Motion tiers

### Tier 0 — CSS micro feedback

Use para:

```text
hover/focus color
small opacity change
button press visual
simple border/shadow transition
```

Budget: **120–180ms**.

### Tier 1 — Component state

Use Motion para:

```text
popover/sheet/dialog enter-exit
alert/toast presence
accordion com conteúdo variável
skeleton → content crossfade
filter/result transition
```

Budget: **160–260ms**.

### Tier 2 — Layout continuity

Use:

```text
AnimatePresence
layout / layoutId
reorder
shared element continuity
progress visualization
expand/collapse with measured layout
```

Budget típico: **220–360ms**.

### Tier 3 — Immersive choreography

Permitido principalmente no Student Immersive e em marketing selecionado:

```text
hero staged entrance
course collection stagger
editorial reveal
route continuity dashboard → lesson
visual journey/progress transitions
```

Regras:

- máximo recomendado: 1 sequência principal por mudança de página;
- stagger pequeno, nunca uma cascata de dezenas de elementos;
- nenhum texto essencial fica invisível aguardando scroll-animation;
- animações de entrada não atrasam CTA primário;
- não animar métricas de forma que pareçam mudar de valor quando não mudaram.

### Tier 4 — Proibido / alto risco

Não usar como padrão:

```text
bounce em pagamento, auth ou alerta clínico
parallax obrigatório em leitura/aula
scroll-jacking
cursor custom que reduz usabilidade
infinite decorative animation no dashboard
animar width/height quando transform/layout resolve melhor
grande blur animado
múltiplos elementos competindo com vídeo/aula
```

## 3. Motion tokens

```text
micro        140ms
fast         180ms
standard     220ms
panel        300ms
page         380ms
page-max     420ms

standard easing: cubic-bezier(.2,.8,.2,1)
exit easing:     cubic-bezier(.4,0,1,1)
```

Springs somente quando a interação é fisicamente interpretável: drag, reorder, snap, shared layout. Para menus, alertas, pagamento e clínica, prefira easing determinístico.

## 4. Reduced motion

`prefers-reduced-motion: reduce` é uma modalidade de primeira classe:

- remove translate/scale choreography;
- reduz duração próxima de zero quando possível;
- preserva mudanças de opacity/status essenciais;
- não altera ordem, foco ou disponibilidade de conteúdo;
- progress não depende da animação para comunicar valor.

Todo componente Motion reutilizável deve documentar comportamento reduced-motion.

## 5. Performance

Obrigatório:

- preferir `transform` e `opacity`;
- evitar layout thrash e leitura/escrita repetida por frame;
- lazy-load motion-heavy surfaces quando razoável;
- não carregar animação avançada em admin/checkout sem necessidade;
- validar INP e main-thread em jornadas críticas;
- MotionScore é recomendado quando Motion+ estiver conectado, mas ausência de Motion+ não bloqueia a implementação básica.

## 6. Component recipes

### StudentHero

```text
background image: estática
image zoom: nenhum ou <= 1.02 somente na entrada
content: opacity + y(8–14px)
headline/body stagger: 40–60ms
CTA disponível imediatamente
```

### CourseCard

```text
hover: translateY(-2px) OU shadow change; não ambos agressivos
image: no máximo scale 1.01–1.02
press: 0.99 opcional
progress: transition 220–320ms quando valor realmente muda
```

### JourneyProgress

- valor textual renderizado imediatamente;
- ring/bar pode interpolar do valor anterior cacheado ao novo;
- sem contagem fake 0→N em toda navegação.

### Sidebar

- desktop fixa, sem animação constante;
- mobile sheet: enter/exit 220–300ms;
- seleção usa motion de highlight somente se não causar atraso na navegação.

### Route transitions

- usar somente em rotas de aprendizagem onde continuidade realmente ajuda;
- checkout/auth/admin preferem navegação direta;
- não bloquear browser back/forward;
- foco deve mover corretamente após a navegação.

## 7. Motion workflow

Para animação Tier 2/3:

1. carregar `$motion-experience-orchestrator`;
2. inspecionar versão instalada de `motion`;
3. buscar docs/exemplo apropriado quando MCP estiver disponível;
4. escolher CSS vs Motion conscientemente;
5. implementar reduced-motion;
6. revisar performance; usar MotionScore quando disponível;
7. registrar no handoff o que foi animado e por quê.


## 8. React implementation baseline

### Reduced motion

```tsx
import { motion, useReducedMotion } from "motion/react";

function Reveal({ children }: { children: React.ReactNode }) {
  const reduce = useReducedMotion();
  return (
    <motion.div
      initial={reduce ? false : { opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: reduce ? 0 : 0.28, ease: [0.2, 0.8, 0.2, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

### Presence

```tsx
<AnimatePresence mode="wait" initial={false}>
  <motion.section
    key={activeId}
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    exit={{ opacity: 0 }}
  />
</AnimatePresence>
```

Use exemplos como baseline de semântica, não como copy/paste obrigatório. Valores devem respeitar tokens e comportamento real do componente.

## 9. Motion evidence

Para Tier 2/3, registrar:

```text
motion_tier
interaction_goal
motion_components/APIs
reduced_motion_behavior
performance_check
MotionScore_result (se Motion+ disponível)
```


## 10. Motion MCP capabilities — default vs opt-in

**Licensing note:** a biblioteca runtime `motion` possui licença própria; o repositório separado `motiondivision/ai-kit` está `NOASSERTION` no lock V5.8 e não é redistribuído pelo projeto enquanto o commit pinado não expuser licença verificável.

### Motion MCP — default

O servidor `https://mcp.motion.dev` pode ser habilitado por padrão quando o plugin é construído. Use para documentação/exemplos públicos e capabilities disponibilizadas pelo servidor. A UI continua funcional se o MCP estiver temporariamente indisponível porque a arquitetura local e a documentação versionada do projeto não dependem do MCP em runtime.

### Motion+ MCP — opt-in

`https://mcp.motion.dev/plus` **não é registrado por padrão**. Habilite apenas quando a equipe possuir acesso e quiser usar capabilities premium, por exemplo MotionScore/metodologia, source premium ou tooling adicional disponibilizado pela conta.

```text
Best practices / skill local      -> disponível sem Motion+
Docs/exemplos públicos via MCP    -> Motion MCP quando conectado
MotionScore / premium source      -> Motion+ quando autorizado
Funcionalidade essencial do app   -> nunca depende de Motion+
```

O build de plugins usa `--include-motion-plus` somente por opt-in explícito. Não reconstruir conteúdo gated a partir de descrições.

## 11. UI/UX Pro Max motion outputs

UI/UX Pro Max pode retornar recomendações/snippets de GSAP conforme seu dial `--motion`. A ICIBINA usa **Motion for React como runtime padrão**. Portanto:

```text
UIUX motion suggestion -> extrair princípio/efeito -> implementar em Motion/CSS
```

Adicionar GSAP ao projeto exige decisão explícita e justificativa de capability que Motion/CSS não resolvam. Nunca carregar duas bibliotecas de animação apenas por conveniência de snippet.

## 12. 21st animation intake

Se um componente 21st trouxer outra animation library:

1. verificar se a dependência é realmente necessária;
2. preferir substituir por Motion/CSS local;
3. preservar behavior/a11y;
4. remover dependência transitiva desnecessária;
5. registrar exceção se mantida.

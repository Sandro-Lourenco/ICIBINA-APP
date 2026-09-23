# Accessibility specification — WCAG 2.2 AA

## Baseline

WCAG 2.2 AA é requisito de produto. Automação ajuda, mas não substitui teste manual com teclado e tecnologias assistivas.

## Keyboard

- skip link no início;
- ordem de foco acompanha ordem visual/lógica;
- modais fazem trap e restauram foco;
- drag/reorder possui alternativa por teclado;
- dropdown/combobox segue padrão ARIA aplicável.

## Focus

Foco é visível em todos os backgrounds. Nunca `outline: none` sem substituto equivalente.

## Contrast

- texto normal >= 4.5:1;
- texto grande conforme WCAG;
- controles/estados atendem contraste não textual aplicável;
- tokens críticos validados por `scripts/check-design-tokens.py`.

## Forms

- label persistente;
- error summary em formulários longos;
- erro associado ao campo;
- dados digitados preservados após erro;
- autocomplete tokens corretos em auth/perfil.

## Motion

`prefers-reduced-motion` reduz transições não essenciais. Não há autoplay de movimento decorativo obrigatório.

## Media

- caption/legenda quando fornecida/necessária;
- transcript para conteúdo educacional conforme política;
- imagens educacionais têm alt/descrição adequados; imagens decorativas alt vazio.

## Tables/charts

- headers/relationships semânticos;
- gráficos têm resumo textual/dados acessíveis quando informação não estiver disponível em outro lugar;
- status não depende apenas de cor.

## Responsive/reflow

Testar 320 CSS px e zoom 200%. Evitar scroll em dois eixos; exceção controlada para tabelas complexas com alternativa acessível.

## QA

Rotas críticas:

```text
axe automation
keyboard smoke
focus order
200% zoom
reduced motion
screen-reader manual sample por release relevante
```

Não instalar “accessibility overlay” como solução de conformidade.


## Dark mode gate

V5.3 valida também os semantic tokens do tema escuro. Focus indicator e bordas relevantes devem atingir pelo menos 3:1 contra a superfície adjacente; texto normal mantém 4.5:1.


## Immersive surfaces

`Student Immersive` continua sendo WCAG 2.2 AA. Dark/premium não reduz requisitos.

- overlays sobre foto devem ser testados com a imagem real, não apenas token isolado;
- foco deve permanecer visível sobre `surface`, imagem e overlay;
- texto não pode desaparecer quando a imagem falha/carrega lentamente;
- reduced-motion é obrigatório para Tier 2/3;
- hover transform não pode ser a única indicação de interatividade;
- charts/progress mantêm valor textual;
- serif editorial não é usada em controles, campos ou longos blocos de leitura técnica.


## Forced colors / high contrast

Rotas e primitives críticas devem ser testadas com `@media (forced-colors: active)` / Windows High Contrast. O objetivo não é recriar um tema separado, e sim deixar o user agent aplicar a paleta do usuário e corrigir apenas falhas reais.

- não dependa de `box-shadow`, gradient ou background image como único indicador de foco/seleção/status;
- prefira elementos semânticos nativos, porque forced colors usa semântica nativa para system colors;
- quando necessário, use system colors (`Canvas`, `CanvasText`, `ButtonText`, `Highlight`, `HighlightText`) em ajustes pequenos;
- `forced-color-adjust: none` é exceção e exige justificativa, porque desativa a paleta do usuário;
- teste também `prefers-contrast: more` quando suportado, sem diminuir contraste quando a preferência não for conhecida;
- charts/progress/status continuam com texto/ícone/padrão, nunca apenas cor.

Exemplo defensivo:

```css
@media (forced-colors: active) {
  .focusable-card:focus-visible {
    outline: 2px solid Highlight;
    outline-offset: 3px;
  }
}
```

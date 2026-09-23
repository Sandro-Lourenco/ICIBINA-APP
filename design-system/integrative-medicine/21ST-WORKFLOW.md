# 21st.dev — ICIBINA Component & Review Workflow

21st.dev é usado para acelerar exploração e implementação **sem descaracterizar** a ICIBINA.

## 0. Bootstrap gate

Antes do primeiro intake 21st em frontend real, cumpra `docs/62-SHADCN-BOOTSTRAP-AND-21ST-INTAKE.md`: Tailwind/aliases, `components.json`, tokens ICIBINA e primitive layer shadcn precisam estar estáveis. 21st não inaugura a primitive foundation.

## 1. Ordem obrigatória

```text
componente/padrão local existe?
   ├─ sim -> reutilizar/estender local
   └─ não -> 21st search
                 ↓
          candidato adequado?
          ├─ sim -> inspect/get -> adaptar
          └─ não -> construir local ou gerar somente se AI habilitada
```

## 2. `21st-ui-explore`

Usar somente quando:

- direção visual está realmente aberta;
- usuário pediu opções/variantes;
- redesign precisa comparar hipóteses de hierarchy/navigation/density.

Não usar para uma página cuja direção já está especificada no override.

As três direções precisam diferir por estrutura/ênfase/interação, não apenas cor.

## 3. `21st-ui-build`

Obrigatório para nova página/section/componente substancial quando 21st estiver disponível:

1. ler `.21st/design.json` + `.21st/DESIGN.md`;
2. inspecionar primitives locais;
3. `21st search "<necessidade específica>" --context auto`;
4. preferir local; instalar candidato apenas se reduz duplicação ou melhora materialmente a solução;
5. adaptar tokens, semantics, accessibility, loading/error/empty e responsive;
6. não manter dependência supérflua trazida pelo componente externo;
7. rodar `21st review` no resultado.

## 4. `21st-ui-review`

Obrigatório antes do handoff de:

```text
nova página
redesign
novo fluxo de compra/auth
student dashboard/player
course builder
admin table/filter complexos
```

Separar findings em:

- defect determinístico;
- drift do design system;
- a11y/interação;
- responsive;
- recomendação subjetiva.

Correção automática somente em defeito determinístico de baixa ambiguidade.

## 5. Design context

`.21st/design.json` é projeção do Master. Não pode inventar outra paleta/brand.

Decisões duráveis aprovadas podem ser registradas em `decisions`, mas mudanças de foundations devem voltar ao `MASTER.md` primeiro.

## 6. Component intake checklist

Antes de incorporar código 21st:

```text
[ ] licença/origem compreendida
[ ] dependências justificadas
[ ] tokens substituídos
[ ] sem hardcoded palette conflitante
[ ] keyboard/focus corretos
[ ] reduced motion quando aplicável
[ ] states loading/error/empty
[ ] mobile/tablet/desktop
[ ] testes necessários adicionados
[ ] nenhum duplicate primitive local
```

## 7. Publishing/sync

`21st-design-sync` publica tema externamente; **nunca executar sem autorização explícita**. Design context local não implica permissão de publicar nada.

# Page override — Player/aula

**Surface:** `Student Immersive` focada  
**UI/UX Pro Max dials:** variance 4 / motion 5 / density 5.

- Player dominante; imagem/decoração nunca compete com vídeo ou leitura.
- Currículo recolhível; desktop side panel, mobile sheet/drawer.
- Título + progresso + próximo item permanecem visíveis de forma previsível.
- Sections: resumo, transcrição, recursos, referências.
- Controles de velocidade/legenda quando suportados.
- `ClinicalCaution` e `EvidenceNote` nunca escondidos atrás de hover.
- Reading width: 760–880px para transcrição/texto.
- Dark immersive permitido como padrão de estudo, com surfaces separadas do player.
- Source Serif 4 somente em heading editorial opcional; transcrição e controles permanecem Inter.

## Motion

- curriculum drawer 220–300ms;
- mudança de lesson pode usar crossfade/continuidade curta <=320ms;
- progresso muda somente quando backend confirma estado;
- tabs usam indicador de seleção curto, sem page choreography;
- conclusão de aula pode ter feedback de sucesso discreto, nunca confete;
- reduced motion remove translação/scale e mantém foco/estado imediatamente.

## Performance

Player, transcript e media têm prioridade sobre animação. Não animar blur grande, canvas decorativo ou background contínuo durante reprodução.

# 57 — Proibição de dados identificáveis de pacientes e controles de PII

## Regra principal

**Patient-identifiable data prohibited.** A ICIBINA é plataforma educacional, não prontuário. Notas pessoais, formulários, comentários, uploads, exemplos de caso, prompts de IA e materiais do professor não devem conter dados que identifiquem um paciente real, salvo futuro fluxo jurídico/técnico explicitamente aprovado — fora deste baseline.

## Exemplos proibidos

- nome, CPF, telefone, e-mail, endereço ou identificador de prontuário ligado a caso clínico;
- fotos, vídeos, voz ou documentos que permitam identificar paciente;
- laudos, receitas, exames, DICOM ou prints de sistema com identificadores;
- combinação de idade/data/local/evento raro que torne o titular razoavelmente identificável;
- copiar prontuário para campo de nota, fórum, busca ou IA.

## Casos educacionais permitidos

Preferir dados **sintéticos**. Caso real somente após desidentificação aprovada e revisão editorial/compliance. “Remover o nome” sozinho não prova anonimização.

## UX obrigatória

Antes de campos de nota/caso/upload em contexto clínico, mostrar aviso curto e persistente:

> Não inclua nome, documento, prontuário, imagem ou qualquer dado que permita identificar um paciente. Use casos sintéticos ou devidamente desidentificados.

Adicionar componente `PatientDataWarning`. O aviso não substitui controles de backend.

## Controles técnicos

- limite de tipos/tamanho de upload + malware scan;
- detector de PII/PHI **quando aplicável** como sinal auxiliar, nunca como garantia de anonimização;
- conteúdo suspeito pode ser bloqueado/quarentenado e exigir revisão;
- logs nunca gravam payload clínico bruto;
- admin/moderação usa acesso mínimo e auditado;
- retenção/eliminação específica para conteúdo bloqueado/quarentenado;
- integrações de IA recebem somente conteúdo necessário e aprovado para aquele fluxo.

## API / erro estável

Quando o backend bloquear conteúdo, usar `PATIENT_IDENTIFIABLE_DATA_PROHIBITED` e mensagem sem ecoar o dado sensível detectado.

## Incidente

Se dado identificável for enviado apesar dos controles: restringir acesso, preservar auditoria mínima, acionar segurança/privacidade, avaliar obrigação de comunicação conforme LGPD/política institucional e remover/reter conforme base legal aplicável.

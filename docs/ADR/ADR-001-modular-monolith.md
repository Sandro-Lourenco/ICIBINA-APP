# ADR-001 — Modular Monolith + Ports/Adapters

**Status:** Accepted

## Context
O produto exige várias áreas e integrações, mas não há evidência de necessidade operacional para microservices no lançamento.

## Decision
Usar modular monolith com `domain/application/infrastructure/interface`, módulos de negócio explícitos e integração por ports/use cases/eventos.

## Alternatives
- Microservices: rejeitado por custo operacional e transacional prematuro.
- Monolith em camadas globais: rejeitado por acoplamento crescente.

## Consequences
Deploy simples, transações locais fortes, menor overhead; exige architecture tests para impedir erosão de módulos.

## Revisit when
Um módulo tiver necessidade comprovada de escala/equipe/deploy isolado que compense o custo distribuído.

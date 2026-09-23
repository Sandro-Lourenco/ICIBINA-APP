# ADR-009 — RBAC + Ownership/ABAC

**Status:** Accepted

## Decision
Roles dão capacidade ampla; ownership/atributos controlam o recurso concreto. Professor não acessa curso alheio apenas por possuir role `teacher`.

## Consequences
Use cases sensíveis precisam de testes cross-account/BOLA.

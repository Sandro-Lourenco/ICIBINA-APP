# Security CI enforcement

A documentação de segurança só conta como controlada quando há evidência automatizada ou revisão registrada.

## Pull request

- secret scanning;
- SAST CodeQL/Semgrep ou equivalente aprovado;
- Python: dependency audit + Bandit/Semgrep quando backend existir;
- frontend: `npm audit` + lint rules de segurança quando aplicável;
- filesystem/container/IaC scan com Trivy quando artefatos existirem.

## Release

- zero secret finding não justificado;
- zero Critical/High conhecido sem waiver aprovado e prazo;
- BOLA/authorization regression suite;
- payment/webhook security tests;
- admin MFA verification;
- dependency/SBOM evidence;
- container scan para imagens finais.

## Waiver

Waiver é explícito: finding, owner, racional, compensating control, expiração e ticket. “Aceito pelo agente” não é autorização.


## SBOM

Security e release geram SBOM CycloneDX com Trivy e validam o artefato com `scripts/check-sbom.py`. SBOM ausente/vazio não é PASS.

## Explicit security regression suites

Quando o backend existir, release executa suites pytest marcadas `authz` e `payments_security`; ausência dos markers no `pyproject.toml` falha o contrato de release.

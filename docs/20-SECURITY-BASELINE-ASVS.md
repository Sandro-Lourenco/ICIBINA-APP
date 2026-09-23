# 20 — Security Baseline

## Objetivo

A plataforma adota **OWASP ASVS 5.0 Level 2** como baseline de verificação de segurança para o produto web, complementado por threat modeling, testes BOLA/IDOR, hardening de infraestrutura e revisão humana antes de operações de alto risco.

Isto é um alvo técnico, não uma alegação de certificação.

## 1. Controles mínimos por área

### Identidade

- Argon2id calibrado;
- e-mail normalizado e unicidade case-insensitive;
- access token curto;
- refresh token randômico, hash no DB, rotation e family/reuse detection;
- sessão por dispositivo;
- reset de senha de uso único;
- revogação de sessões após reset/troca conforme política;
- MFA **obrigatório** para `admin` e `super_admin`;
- reautenticação recente para mudança de role, refund, secrets/config e operações críticas.

### Autorização

Matriz mínima:

| Recurso | Student | Teacher | Admin | Super admin | Ownership obrigatório |
|---|---:|---:|---:|---:|---:|
| Próprio perfil | R/W | R/W | R | R | sim |
| Curso publicado | R | R | R/W moderação | R/W | não |
| Curso em autoria | - | R/W | R | R | teacher_id |
| Matrícula própria | R | - | R/W controlado | R/W | user_id |
| Pagamento próprio | R | - | R restrito | R | user_id |
| Refund | - | - | política explícita | sim | n/a |
| Roles | - | - | limitado | R/W | n/a |
| Operações do sistema | - | - | limitado | R/W | n/a |

Toda rota privada tem teste negativo cross-account quando houver objeto possuído.

### Browser

- sem secrets;
- CSP estrita e iterativamente ajustada;
- HSTS em produção;
- `nosniff`;
- `Referrer-Policy`;
- `Permissions-Policy`;
- cookies `HttpOnly`, `Secure` e SameSite apropriado;
- proteção CSRF quando a arquitetura depender de cookies para autorização de requests mutáveis.

### Pagamento

- preço calculado no backend;
- callback do navegador não concede acesso;
- webhook autenticado + idempotente;
- provider event inbox durável;
- reconciliação;
- log financeiro auditável;
- PAN/CVV nunca armazenados.

### Uploads

- allowlist de tipo e verificação de conteúdo;
- tamanho máximo;
- chave gerada pelo servidor;
- bucket privado;
- URL assinada curta;
- processamento não confiável em worker isolado;
- malware scanning conforme tipo de upload/risco.

## 2. Security gates no CI

Obrigatórios antes de merge/release conforme aplicável:

```text
SAST
SCA/dependency scan
secret scan
unit/integration auth tests
BOLA regression suite
OpenAPI auth review/check
container/image scan quando houver imagem de produção
```

Bloqueadores:

- secret de produção no Git;
- critical/high exploitável sem aceite formal;
- teste de autorização crítico quebrado;
- downgrade de headers/CSP sem justificativa;
- endpoint administrativo novo sem audit event.

## 3. Logging e privacidade

Nunca registrar:

```text
password
raw refresh token
Authorization header
session cookie
Asaas API key
webhook auth token
PAN/CVV
```

PII deve ser registrada apenas quando essencial ao caso operacional e com retenção definida.

## 4. Processo de exceção

Exceção de segurança exige:

```text
owner
risco
escopo
compensating control
expiração
issue/ADR quando arquitetural
```

Exceções nunca ficam indefinidas.

## 5. Verificação pré-produção

- threat model revisado;
- ASVS L2 checklist rastreável;
- teste de autorização/BOLA;
- teste de sessão/replay;
- webhook replay/duplicate/out-of-order;
- dependency/secret scan;
- configuração TLS/headers;
- revisão de buckets e URLs assinadas;
- pentest proporcional ao risco antes de lançamento comercial relevante.

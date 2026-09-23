# 08 — Segurança e LGPD

> Baseline verificável: OWASP ASVS 5.0 Level 2 conforme `docs/20-SECURITY-BASELINE-ASVS.md`.

## Threat model mínimo

Proteja contra:

- credential stuffing/brute force;
- session theft;
- BOLA/IDOR;
- privilege escalation;
- XSS;
- CSRF quando auth usa cookies;
- injection;
- upload malicioso;
- open redirect;
- webhook spoofing/replay/duplicate delivery;
- manipulação de preço;
- exposição de segredo em frontend/log;
- abuso de endpoints caros.

## Autenticação

- Argon2id com parâmetros calibrados;
- refresh tokens aleatórios e armazenados como hash;
- rotação de refresh;
- revogação por sessão;
- rate limit em login/reset;
- resposta de forgot password que não enumere contas;
- MFA obrigatório em produção para `admin` e `super_admin`.

## Cookies

Exemplo em produção:

```text
HttpOnly=true
Secure=true
SameSite=Lax ou Strict conforme fluxo
Path=/api/v1/auth
```

Se arquitetura/domínios exigirem `SameSite=None`, implemente proteção CSRF explícita e revise CORS cuidadosamente.

## CORS

Produção:

```text
https://www.seudominio.com.br
https://app.seudominio.com.br
```

Nunca `*` com credentials.

## Autorização

Checklist em cada use case sensível:

```text
1. usuário autenticado?
2. role permite a ação?
3. recurso existe?
4. usuário possui/tem vínculo com esse recurso?
5. estado atual permite transição?
```

Faça testes negativos para outra conta/role.

## Pagamento

- chave Asaas somente no backend;
- preço vem do DB;
- checkout callback não confirma pagamento;
- webhook autenticado e idempotente;
- sem armazenamento de PAN/CVV;
- eventos reversos tratados;
- auditoria de ação administrativa.

## Upload

- allowlist de MIME + verificação real;
- limite de tamanho;
- nomes/chaves gerados pelo servidor;
- URL assinada curta;
- bucket privado para conteúdo pago;
- antivírus/scanner se usuários puderem subir documentos arbitrários;
- processamento em worker isolado.

## Headers

Configurar no proxy/app:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options: nosniff
Referrer-Policy
Permissions-Policy
frame-ancestors via CSP
```

## Secrets

Produção em secret manager. Nunca commitados.

CI deve procurar padrões de segredo. Rotacione imediatamente qualquer chave exposta.

## Logs

Redação automática para campos:

```text
password
access_token
refresh_token
authorization
cookie
api_key
asaas-access-token
creditCard*
cpf/cnpj quando não necessário
```

## LGPD — engenharia

Não é parecer jurídico, mas a arquitetura deve permitir:

- inventário/finalidade dos dados;
- minimização;
- controle de retenção;
- exportação dos dados do titular;
- correção;
- anonimização/eliminação quando aplicável;
- registro de consentimento quando a base for consentimento;
- resposta a incidente;
- processamento de solicitação de titular;
- separação de audit logs que precisem ser preservados por obrigação legítima/legal.

Não implemente “DELETE CASCADE em tudo” como mecanismo de direito de exclusão. Defina política campo a campo.

## Sessão/JWT — hardening

Para autenticação própria, documente e teste:

- `iss`, `aud`, `sub`, `iat`, `exp` e identificador de sessão/token;
- algoritmo permitido fixo no servidor, sem aceitar algoritmo vindo do token;
- rotação de chave com `kid` quando aplicável;
- tolerância de clock pequena e explícita;
- refresh token rotation com detecção de replay/reuse por família de sessão;
- logout da sessão atual e logout de todas as sessões;
- troca/reset de senha revoga sessões conforme política;
- ação administrativa sensível pode exigir reautenticação recente.

Se access/refresh forem cookies, trate CSRF explicitamente. Se access token ficar em memória e refresh em cookie HttpOnly, documente o fluxo de refresh e sua proteção.

## Retenção e privacidade

Antes de produção, criar matriz de retenção para:

```text
application logs
audit logs
webhook payloads
refresh sessions
password reset tokens
payment metadata
uploads/videos
analytics
```

Webhook bruto pode conter PII; limite acesso, retenção e campos indexados/logados.


## Dados de pacientes

A plataforma não é prontuário. Aplicar obrigatoriamente `docs/57-PATIENT-DATA-PROHIBITION-AND-PII-CONTROLS.md` em notas, uploads, casos clínicos e integrações de IA. Dados de saúde identificáveis não entram em logs nem são aceitos por conveniência educacional.

# Backend Contract — ICIBINA

Use este contrato como contexto inicial para tarefas FastAPI/backend.

## Invariantes

- Fluxo: `interface -> application -> domain`; `infrastructure` implementa ports.
- Router não executa SQLAlchemy nem regra de negócio; chama use case.
- Domain não importa FastAPI, SQLAlchemy, Redis, httpx, Asaas ou Pydantic de transporte.
- Application depende de ports/protocols, não de adapters concretos.
- SQLAlchemy fica em `infrastructure`; transação é coordenada por Unit of Work.
- Repository **não** chama `commit()` por conta própria, salvo adapter explicitamente documentado e aprovado.
- Toda I/O em caminho async deve ser async nativa ou isolada de forma explícita.
- Autorização = role + ownership/ABAC; teste BOLA negativo em recurso privado.
- Erros de API têm `code` estável; logs têm `request_id` e não contêm segredos.
- Preço e estado financeiro são decididos no backend.

## Contexto sob demanda

- fronteiras/transações: `docs/00-ARQUITETURA.md`
- API/OpenAPI: `docs/06-CONTRATO-API.md`
- segurança: `docs/20-SECURITY-BASELINE-ASVS.md`
- banco/ORM: `docs/contracts/DATABASE-CONTRACT.md`
- resiliência: `docs/24-RESILIENCIA-E-FAILURE-MODES.md`
- quality: `docs/contracts/QUALITY-CONTRACT.md`

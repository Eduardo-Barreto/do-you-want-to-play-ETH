# Backend

Este projeto é uma API para um sistema de auxílio à tomada de decisões para investimentos em criptoativos. A API fornece informações sobre criptoativos, previsões de preços e integrações com modelos de machine learning para auxiliar no processo de decisão. A API foi desenvolvida com **FastAPI**, utilizando **PostgreSQL** como banco de dados, e é dockerizada para fácil implantação.

## Estrutura do Projeto

```bash
backend/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── assets.py        # Rotas para os criptoativos
│   │   │   │   ├── predictions.py   # Rotas para previsões de preços
│   ├── core/
│   │   ├── config.py                # Configurações da aplicação
│   │   └── db.py                    # Conexão com o banco de dados
│   ├── models/
│   │   ├── prediction.py            # Modelo de Previsão de Preço
│   ├── schemas/
│   │   ├── prediction.py            # Schemas Pydantic para validação
│   ├── services/
│   │   ├── prediction_service.py    # Lógica de previsão de preços
│   ├── tests/                       # Testes da aplicação
│   ├── main.py                      # Ponto de entrada da API
├── docker-compose.yml                # Configuração Docker
├── Dockerfile                        # Dockerfile para a API
└── requirements.txt                  # Dependências do projeto
```

## Funcionalidades

- **Previsões de Preço**:
  - Criar previsões de preços de criptoativos.
- **Integração com Modelos de Machine Learning**:
  - Integração com modelos de previsão para auxiliar na tomada de decisões com base em dados históricos.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** — Framework rápido e eficiente para APIs.
- **[PostgreSQL](https://www.postgresql.org/)** — Sistema de gerenciamento de banco de dados relacional.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM para gerenciar o banco de dados.
- **[Docker](https://www.docker.com/)** — Contêineres para fácil implantação.

### Endpoints Principais

- **Previsões**:
  - `POST /api/v1/predictions/`: Cria uma nova previsão de preço.
  - `GET /api/v1/predictions/`: Retorna todas as previsões de preço.

### Documentação da API

A documentação interativa da API pode ser acessada via **Swagger** em:

```
http://localhost:8000/docs
```

Ou via **ReDoc** em:

```
http://localhost:8000/redoc
```

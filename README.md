# do-you-want-to-play-ETH

Este projeto é um sistema de auxílio à tomada de decisões para investimento em criptoativos, onde uma interface visual permite que o usuário selecione um ticker, visualize dados históricos e obtenha previsões de preços futuros. O sistema usa modelos de Machine Learning, como GRU, LSTM e ARIMA, para gerar previsões com base em dados históricos e está estruturado para rodar em containers Docker.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

- **Backend (FastAPI)**: Responsável por lidar com a lógica de previsão, integração com modelos e fornecer uma API para a interface.
- **Interface (Streamlit)**: Um frontend interativo onde o usuário pode selecionar os ativos, modelos e intervalos de previsão, e visualizar as previsões e dados históricos de preços.

### Estrutura de Arquivos

```plaintext
.
├── docker-compose.yml
├── notebooks/
│   ├── exploration.ipynb
│   ├── models/
│   │   ├── arima.ipynb
│   │   ├── gru.ipynb
│   │   ├── lstm.ipynb
│   └── requirements.txt
├── src/
│   ├── backend/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── interface/
│       ├── app.py
│       ├── Dockerfile
│       └── requirements.txt
└── README.md
```

## Tecnologias Utilizadas

- **FastAPI**: Framework para criação da API de backend.
- **PostgreSQL**: Banco de dados relacional para armazenar informações.
- **Docker**: Utilizado para containerizar a aplicação.
- **Streamlit**: Interface visual para interação com o usuário.
- **yFinance**: Para coleta de dados históricos de criptoativos.
- **Plotly**: Para visualização gráfica dos dados e previsões.

## Como Rodar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados.

### Passos para Rodar

1. **Clone o repositório:**

```bash
git clone https://github.com/Eduardo-Barreto/do-you-want-to-play-ETH.git
cd crypto-price-prediction
```

2. **Inicie os containers com Docker Compose:**

```bash
docker-compose up --build
```

Isso irá subir três containers:

- Um container para o banco de dados PostgreSQL.
- Um container para o backend FastAPI.
- Um container para a interface Streamlit.

3. **Acesse a interface:**

Abra o navegador e acesse a interface via [http://0.0.0.0:8501](http://0.0.0.0:8501).

## Funcionalidades

### Backend

- **Rota `/api/v1/predictions`**: Rota para gerar previsões de preços. Requisições POST nesta rota retornam previsões para um determinado ativo com base nos modelos especificados.

#### Exemplo de Requisição:

```json
{
  "ticker": "ETH-USD",
  "days_behind": 60,
  "days_ahead": 7,
  "model": "GRU"
}
```

#### Exemplo de Resposta:

```json
{
  "predictions": [
    {
      "ticker": "ETH-USD",
      "predicted_value": 2640.25,
      "prediction_date": "2024-09-29"
    },
    ...
  ]
}
```

### Interface (Streamlit)

- O usuário pode selecionar:
  - O **ticker** da criptomoeda (ex: ETH-USD, BTC-USD).
  - O número de **dias passados** para análise.
  - O número de **dias à frente** para previsão.
  - Os **modelos** a serem usados (GRU, LSTM, ARIMA).
- A interface exibe:
  - Dados históricos e previsões futuras em um gráfico interativo.
  - Linhas pontilhadas de diferentes cores para cada modelo de previsão.

## Configurações do Docker

### Arquivo `docker-compose.yml`

O arquivo `docker-compose.yml` define três serviços:

- **db**: Serviço do PostgreSQL.
- **backend**: Serviço do FastAPI.
- **interface**: Serviço do Streamlit.

### Variáveis de Ambiente

No backend, as variáveis de ambiente para conexão ao banco de dados são configuradas no arquivo `docker-compose.yml`.

```yaml
environment:
  POSTGRES_USER: admin
  POSTGRES_PASSWORD: password
  POSTGRES_DB: crypto_db
  POSTGRES_HOST: db
```

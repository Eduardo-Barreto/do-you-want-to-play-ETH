import streamlit as st
import requests
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("Previsão de Preços de Criptoativos")
st.write("Escolha o ticker e o intervalo de dias para prever.")


def fetch_predictions(ticker, days_behind, days_ahead, model):
    url = "http://backend:8000/api/v1/predictions"
    payload = {
        "ticker": ticker,
        "days_behind": days_behind,
        "days_ahead": days_ahead,
        "model": model,
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return pd.DataFrame(response.json()["predictions"]).rename(
            columns={"prediction_date": "Date"}
        )
    else:
        st.error(f"Erro ao obter previsões para o modelo {model}")
        return pd.DataFrame()


def fetch_historical_data(ticker, days_behind):
    start_date = pd.Timestamp.now() - pd.Timedelta(days=days_behind)
    df = yf.download(ticker, start=start_date)["Close"]
    df = df.reset_index()
    return df


tickers = [
    "ETH-USD",
    "BTC-USD",
    "ADA-USD",
    "BNB-USD",
    "XRP-USD",
    "DOGE-USD",
    "LTC-USD",
    "LINK-USD",
    "BCH-USD",
    "XLM-USD",
    "ETC-USD",
]

ticker = st.selectbox("Escolha o Ticker", tickers)
days_behind = st.slider("Dias Passados", 30, 365, 60)
days_ahead = st.slider("Dias à Frente (Previsão)", 1, 30, 7)

models = st.multiselect(
    "Escolha o(s) Modelo(s) de Previsão",
    options=["GRU", "LSTM", "ARIMA"],
    default=["GRU", "LSTM", "ARIMA"],
)

if st.button("Fazer Previsão"):
    with st.spinner("Carregando previsões..."):
        historical_data = fetch_historical_data(ticker, days_behind)

        predictions = {}
        for model in models:
            model_predictions = fetch_predictions(
                ticker, days_behind, days_ahead, model
            )
            if not model_predictions.empty:
                predictions[model] = model_predictions

    if predictions:
        st.write("Gráfico de Preço Histórico e Previsão")
        fig = px.line(
            historical_data,
            x="Date",
            y="Close",
            title=f"Preço de {ticker}",
            labels={"Close": "Preço Histórico"},
        )

        for model, pred_df in predictions.items():
            fig.add_scatter(
                x=pred_df["Date"],
                y=pred_df["predicted_value"],
                mode="lines",
                name=f"Previsão {model}",
                line=dict(dash="dot"),
            )

        st.plotly_chart(fig)
    else:
        st.error("Não foi possível obter previsões para nenhum modelo.")

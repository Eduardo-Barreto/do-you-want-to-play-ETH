import streamlit as st
import requests
import yfinance as yf
import pandas as pd
import plotly.express as px


st.title("Previsão de Preços de Criptoativos")
st.write("Escolha o ticker e o intervalo de dias para prever.")


ticker = st.selectbox("Escolha o Ticker", ["ETH-USD", "BTC-USD"])
days_behind = st.slider("Dias Passados", 30, 365, 60)
days_ahead = st.slider("Dias à Frente (Previsão)", 1, 30, 7)
model = st.selectbox("Escolha o Modelo de Previsão", ["GRU", "LSTM", "ARIMA"])


if st.button("Fazer Previsão"):
    url = "http://localhost:8000/api/v1/predictions"
    payload = {
        "ticker": ticker,
        "days_behind": days_behind,
        "days_ahead": days_ahead,
        "model": model,
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        predictions = response.json()["predictions"]
        st.success(f"Previsão feita com sucesso para {ticker}")

        predictions = pd.DataFrame(predictions)
        predictions = predictions.rename(columns={"prediction_date": "Date"})

        start_date = pd.Timestamp.now() - pd.Timedelta(days=days_behind)
        df = yf.download(ticker, start=start_date)["Close"]

        df = df.reset_index()

        df = pd.concat([df, predictions], axis=0, ignore_index=True)
        df["Date"] = pd.to_datetime(df["Date"])

        st.write("Gráfico de Preço Histórico e Previsão")
        fig = px.line(
            df, x="Date", y=["Close", "predicted_value"], title=f"Preço de {ticker}"
        )
        st.plotly_chart(fig)

    else:
        st.error("Erro ao obter as previsões")

import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    root_mean_squared_error,
)


def split_train_test(data, train_size, test_size):
    train_data = data[-train_size:-test_size]
    test_data = data[-test_size:]
    return train_data, test_data


def load_eth_data():
    return yf.download("ETH-USD", start="2020-01-01", interval="1d")


def get_metrics(test_data, predictions):
    return (
        mean_squared_error(test_data, predictions),
        mean_absolute_error(test_data, predictions),
        root_mean_squared_error(test_data, predictions),
    )


def plot_previsions(train_data, test_data, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(train_data.index, train_data, label="Dados de Treinamento")
    plt.plot(test_data.index, test_data, label="Dados Reais")
    plt.plot(test_data.index, predictions, color="red", label="Previsão")
    plt.title("Previsão do Preço de Fechamento do Ethereum")
    plt.xlabel("Data")
    plt.ylabel("Preço de Fechamento")
    plt.legend()
    plt.show()

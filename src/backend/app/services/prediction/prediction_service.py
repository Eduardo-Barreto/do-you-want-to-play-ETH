import yfinance as yf
import datetime
from sklearn.metrics import mean_squared_error
from app.services.prediction.arima import ARIMAModel
from app.services.prediction.gru import GRUModel
from app.services.prediction.lstm import LSTMModel


class PredictionService:
    def __init__(self):
        self.predictions = []

    def fetch_data(self, ticker, start, end):
        data = yf.download(ticker, start=start, end=end)
        return data["Close"]

    def predict(self, ticker, days_behind, days_ahead, model_type) -> list:
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days_behind)
        historical_data = self.fetch_data(ticker, start=start_date, end=end_date)

        model = None
        if model_type == "ARIMA":
            model = ARIMAModel()
        elif model_type == "GRU":
            model = GRUModel()
        elif model_type == "LSTM":
            model = LSTMModel()
        else:
            raise ValueError("Modelo não suportado")

        model.train(historical_data)
        predictions = model.predict(days_ahead)

        return predictions

    def evaluate_model(self):
        mse = mean_squared_error(
            [pred["actual_value"] for pred in self.predictions],
            [pred["predicted_value"] for pred in self.predictions],
        )
        return mse

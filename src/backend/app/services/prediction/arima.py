from app.services.prediction.base import PredictionModel
from statsmodels.tsa.arima.model import ARIMA


class ARIMAModel(PredictionModel):
    def train(self, train_data):
        model = ARIMA(train_data, order=(5, 1, 0))
        self.model = model.fit()

    def predict(self, days_ahead):
        predictions = self.model.forecast(steps=days_ahead)

        return predictions.tolist()

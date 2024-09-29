from app.services.prediction.base import PredictionModel
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler


class GRUModel(PredictionModel):
    def __init__(self):
        self.model = None

    def preprocess_data(self, data):
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))
        return scaled_data, scaler

    def create_dataset(self, data, time_step=1):
        sequences, labels = [], []
        for i in range(len(data) - time_step - 1):
            sequences.append(data[i : (i + time_step), 0])
            labels.append(data[i + time_step, 0])
        return np.array(sequences), np.array(labels)

    def train(self, train_data):
        time_step = train_data.shape[0] // 5

        self.scaled_data, self.scaler = self.preprocess_data(train_data)

        X, Y = self.create_dataset(self.scaled_data, time_step)
        X = X.reshape(X.shape[0], X.shape[1], 1)

        self.model = Sequential()
        self.model.add(GRU(64, return_sequences=True, input_shape=(X.shape[1], 1)))
        self.model.add(Dropout(0.2))
        self.model.add(GRU(64))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1))
        self.model.compile(optimizer="adam", loss="mean_squared_error")

        self.model.fit(X, Y, epochs=100, batch_size=32)

    def predict(self, days_ahead: int, time_step=60):
        last_data = self.scaled_data[-time_step:]
        last_data = last_data.reshape((1, time_step, 1))

        predictions = []
        for _ in range(days_ahead):
            pred = self.model.predict(last_data)
            predictions.append(pred[0, 0])
            reshaped_pred = pred.reshape((1, 1, 1))
            last_data = np.append(last_data[:, 1:, :], reshaped_pred, axis=1)

        return (
            self.scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
            .flatten()
            .tolist()
        )

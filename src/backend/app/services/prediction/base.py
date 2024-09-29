from abc import ABC, abstractmethod


class PredictionModel(ABC):
    @abstractmethod
    def train(self, train_data):
        pass

    @abstractmethod
    def predict(self, days_ahead: int):
        pass

from sqlalchemy import Column, Integer, Float, String
from app.core.db import Base


class PredictionModel(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    predicted_value = Column(Float)
    prediction_date = Column(String)

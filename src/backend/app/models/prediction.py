from sqlalchemy import Column, Integer, Float, String, DateTime
from app.core.db import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    predicted_value = Column(Float)
    actual_value = Column(Float, nullable=True)
    prediction_date = Column(String)

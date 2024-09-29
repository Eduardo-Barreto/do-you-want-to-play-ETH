from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String)
    predicted_value = Column(Float)
    actual_value = Column(Float, nullable=True)
    prediction_date = Column(DateTime, default=datetime.datetime.now)

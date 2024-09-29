from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class PredictionCreate(BaseModel):
    ticker: str = Field("ETH-USD", description="The stock ticker symbol")
    days_behind: Optional[int] = Field(
        60, description="Number of days to look back for historical data"
    )
    days_ahead: int = Field(1, description="Number of days to predict ahead")
    model: Optional[str] = Field("ARIMA", description="The model to use for prediction")


class PredictionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ticker: str
    predicted_value: float
    prediction_date: str


class PredictionsResponse(BaseModel):
    predictions: list[PredictionSchema]

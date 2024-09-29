from typing import Optional
from pydantic import BaseModel, Field


class PredictionCreate(BaseModel):
    ticker: str = Field(..., description="The stock ticker symbol")
    days_behind: Optional[int] = Field(
        60, description="Number of days to look back for historical data"
    )
    days_ahead: int = Field(..., description="Number of days to predict ahead")
    model: Optional[str] = Field("ARIMA", description="The model to use for prediction")

    class Config:
        json_schema_extra = {
            "example": {
                "ticker": "ETH",
                "days_behind": 60,
                "days_ahead": 7,
            }
        }


class PredictionsResponse(BaseModel):
    predictions: list[float]

    class Config:
        json_schema_extra = {
            "example": {
                "predictions": [100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0],
            }
        }

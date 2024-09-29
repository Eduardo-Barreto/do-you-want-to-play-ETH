from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.db import get_db
from app.services.prediction.prediction_service import PredictionService
from datetime import datetime
from app.models.prediction import PredictionModel
from app.schemas.prediction import (
    PredictionCreate,
    PredictionsResponse,
    PredictionSchema,
)
import pandas as pd

router = APIRouter(prefix="/predictions")
prediction_service = PredictionService()


@router.get(
    "/{ticker}",
    response_model=PredictionsResponse,
)
async def get_predictions(
    ticker: str,
    db: AsyncSession = Depends(get_db),
):
    predictions = await db.execute(
        select(PredictionModel).where(PredictionModel.ticker == ticker)
    )

    predictions = predictions.scalars().all()

    predictions = [
        PredictionSchema.model_validate(prediction) for prediction in predictions
    ]

    return PredictionsResponse(predictions=predictions)


@router.post(
    "/",
    response_model=PredictionsResponse,
)
async def create_prediction(
    prediction_request: PredictionCreate,
    db: AsyncSession = Depends(get_db),
):
    prediction_service = PredictionService()
    predictions_response = []

    try:
        predictions = prediction_service.predict(
            ticker=prediction_request.ticker,
            days_behind=prediction_request.days_behind,
            days_ahead=prediction_request.days_ahead,
            model_type=prediction_request.model,
        )

        for i, prediction in enumerate(predictions):
            date = (datetime.now() + pd.Timedelta(days=i)).strftime("%Y-%m-%d")
            prediction_entry = PredictionModel(
                ticker=prediction_request.ticker,
                predicted_value=prediction,
                prediction_date=date,
            )

            predictions_response.append(
                PredictionSchema.model_validate(prediction_entry)
            )
            db.add(prediction_entry)
            await db.commit()
            await db.refresh(prediction_entry)

        return PredictionsResponse(predictions=predictions_response)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

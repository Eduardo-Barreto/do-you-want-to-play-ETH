from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.services.prediction.prediction_service import PredictionService
from datetime import datetime
from app.models.prediction import Prediction
from app.schemas.prediction import PredictionCreate, PredictionsResponse
import pandas as pd

router = APIRouter()
prediction_service = PredictionService()


@router.post(
    "/predict",
    response_model=PredictionsResponse,
)
async def create_prediction(
    prediction_request: PredictionCreate,
    db: AsyncSession = Depends(get_db),
):
    prediction_service = PredictionService()

    try:
        predictions = prediction_service.predict(
            ticker=prediction_request.ticker,
            days_behind=prediction_request.days_behind,
            days_ahead=prediction_request.days_ahead,
            model_type=prediction_request.model,
        )

        for i, prediction in enumerate(predictions):
            date = (datetime.now() + pd.Timedelta(days=i)).strftime("%Y-%m-%d")
            prediction_entry = Prediction(
                ticker=prediction_request.ticker,
                predicted_value=prediction,
                prediction_date=date,
            )

            db.add(prediction_entry)
            await db.commit()
            await db.refresh(prediction_entry)

        return PredictionsResponse(predictions=predictions)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)

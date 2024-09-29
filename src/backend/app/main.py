from fastapi import FastAPI
from app.api.v1.endpoints import predictions

app = FastAPI()

app.include_router(predictions.router, prefix="/api/v1", tags=["predictions"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Crypto Prediction API"}

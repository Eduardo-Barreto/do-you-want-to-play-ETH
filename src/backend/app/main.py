from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import predictions
from app.core.db import init_db


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await init_db()
    print("Application startup")

    yield
    print("Application shutdown")


app = FastAPI(lifespan=app_lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(predictions.router, prefix="/api/v1", tags=["predictions"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Crypto Prediction API"}

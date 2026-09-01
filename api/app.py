from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Housing Price Prediction API",
    description=(
        "A machine learning API that predicts house prices "
        "using a trained Gradient Boosting Regressor."
    ),
    version="1.0.0"
)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "housing_price_model.joblib"
)

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Input Data Schema
# --------------------------------------------------

class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Housing Price Prediction API is running",
        "status": "success"
    }


# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True
    }


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(data: HouseData):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }
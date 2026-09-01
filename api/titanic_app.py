from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Titanic Survival Prediction API",
    description=(
        "A machine learning API that predicts Titanic passenger "
        "survival using a trained Gradient Boosting Classifier."
    ),
    version="1.0.0"
)


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "titanic_optimized_gradient_boosting.pkl"
)

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Input Data Schema
# --------------------------------------------------

class PassengerData(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: str
    Title: str


# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

def prepare_features(data: PassengerData):

    family_size = data.SibSp + data.Parch + 1

    fare_per_person = (
        data.Fare / family_size
        if family_size > 0
        else data.Fare
    )

    # The model was trained with Title_Mr and Title_Rare.
    title_mr = 1 if data.Title == "Mr" else 0

    common_titles = [
        "Mr",
        "Miss",
        "Mrs",
        "Master"
    ]

    title_rare = 1 if data.Title not in common_titles else 0

    sex_male = 1 if data.Sex.lower() == "male" else 0
    sex_female = 1 if data.Sex.lower() == "female" else 0

    embarked_s = 1 if data.Embarked.upper() == "S" else 0

    features = pd.DataFrame([{
        "cat__Title_Mr": title_mr,
        "num__FarePerPerson": fare_per_person,
        "num__Pclass": data.Pclass,
        "num__Age": data.Age,
        "num__Fare": data.Fare,
        "cat__Sex_male": sex_male,
        "num__FamilySize": family_size,
        "cat__Title_Rare": title_rare,
        "cat__Sex_female": sex_female,
        "cat__Embarked_S": embarked_s
    }])

    return features


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Titanic Survival Prediction API is running",
        "status": "success"
    }


# --------------------------------------------------
# Health Check
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
def predict(data: PassengerData):

    input_features = prepare_features(data)

    prediction = model.predict(input_features)

    result = int(prediction[0])

    return {
        "prediction": result,
        "survival_status": (
            "Survived"
            if result == 1
            else "Did Not Survive"
        )
    }
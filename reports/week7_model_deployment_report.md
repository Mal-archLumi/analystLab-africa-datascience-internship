# Week 7: Model Deployment & Real-World Application

## 1. Overview

Week 7 focused on taking the machine learning models developed during the previous weeks and converting them into usable real-world applications.

The deployment phase covered two machine learning projects:

1. House Price Prediction
2. Titanic Survival Prediction

The trained Gradient Boosting models were saved using Joblib and integrated into FastAPI prediction APIs. Streamlit interfaces were also created to allow users to provide input data and receive predictions through a simple web interface.

---

## 2. Objectives

The main objectives of Week 7 were to:

- Save trained machine learning models for reuse.
- Build prediction APIs using FastAPI.
- Load trained models without retraining.
- Create prediction endpoints.
- Test API requests and responses.
- Build interactive Streamlit user interfaces.
- Document the deployed machine learning applications.
- Prepare the projects for GitHub and professional presentation.

---

# 3. House Price Prediction Deployment

## 3.1 Model Used

The House Price Prediction project uses a Gradient Boosting Regressor developed during the previous weeks.

The model was selected because it achieved strong performance compared with the other regression models tested.

### Final Performance

| Metric | Score |
|---|---:|
| MAE | 967,227.33 |
| RMSE | 1,299,730.23 |
| R² | 0.6658 |

The model uses the following features:

- Area
- Bedrooms
- Bathrooms
- Stories
- Mainroad
- Guestroom
- Basement
- Hotwaterheating
- Airconditioning
- Parking
- Prefarea
- Furnishingstatus

---

## 3.2 Model Serialization

The trained model was saved using Joblib so that it could be loaded later without retraining.

The saved model is:

```text
models/housing_price_model.joblib
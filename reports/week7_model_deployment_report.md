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

3.3 FastAPI Implementation

A FastAPI application was created in:

api/app.py

The API loads the saved model and exposes prediction functionality.

Available Endpoints
GET /

Returns a basic API status message.

GET /health

Provides a health check confirming that the API and machine learning model are available.

POST /predict

Accepts house information and returns a predicted house price.

3.4 Housing API Input

The prediction endpoint accepts the following JSON structure:

{
  "area": 316,
  "bedrooms": 4,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": "no",
  "guestroom": "no",
  "basement": "yes",
  "hotwaterheating": "no",
  "airconditioning": "no",
  "parking": 1,
  "prefarea": "no",
  "furnishingstatus": "unfurnished"
}
3.5 Housing API Output

The API returns a predicted price.

Example:

{
  "predicted_price": 4502828.37
}

The prediction was successfully tested through the FastAPI Swagger documentation and returned an HTTP 200 OK response.

4. Titanic Survival Prediction Deployment
4.1 Model Used

The Titanic project uses an optimized Gradient Boosting Classifier.

The saved model is:

models/titanic_optimized_gradient_boosting.pkl

The model configuration is:

GradientBoostingClassifier(
    learning_rate=0.01,
    max_depth=4,
    n_estimators=300,
    random_state=42
)

The model was developed and optimized during the previous machine learning and feature engineering stages.

4.2 Feature Engineering

The Titanic model uses engineered features including:

Title
FarePerPerson
Pclass
Age
Fare
Sex
FamilySize
Embarked

The saved model contains the transformed feature representation required by the trained classifier.

4.3 FastAPI Implementation

A separate FastAPI application was created in:

api/titanic_app.py

The Titanic API runs on port 8001 to avoid conflicting with the Housing API.

Available Endpoints
GET /

Returns the API status.

GET /health

Checks whether the API and model are available.

POST /predict

Accepts passenger information and returns a survival prediction.

4.4 Titanic API Input

Example request:

{
  "Pclass": 1,
  "Sex": "female",
  "Age": 25,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 50,
  "Embarked": "S",
  "Title": "Miss"
}
4.5 Titanic API Output

Example response:

{
  "prediction": 1,
  "survival_status": "Survived"
}

The API successfully returned HTTP 200 OK responses during testing.

5. Streamlit User Interfaces

Streamlit applications were developed to provide simple graphical interfaces for interacting with the deployed models.

Housing

The Housing application is:

streamlit_app.py

Users can enter:

Property area
Number of bedrooms
Number of bathrooms
Number of stories
Road access
Guest room availability
Basement availability
Hot water heating
Air conditioning
Parking spaces
Preferred area
Furnishing status

The application sends the information to the prediction model and displays the estimated house price.

Titanic

The Titanic application is:

titanic_streamlit_app.py

Users can provide passenger information including:

Passenger class
Sex
Age
Siblings/spouses aboard
Parents/children aboard
Fare
Embarkation port
Passenger title

The application then generates a survival prediction.

6. API Testing

Both APIs were tested using FastAPI's automatically generated Swagger UI.

Housing API:

http://127.0.0.1:8000/docs

Titanic API:

http://127.0.0.1:8001/docs

Successful requests returned HTTP:

200 OK

The testing confirmed that:

The APIs start successfully.
The saved models load correctly.
Input validation works.
Prediction endpoints accept requests.
Predictions are returned successfully.
7. Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
FastAPI
Uvicorn
Streamlit
Pydantic
Git
GitHub
Jupyter Notebook
8. Project Structure
analystLab-africa-datascience-internship/
│
├── api/
│   ├── app.py
│   └── titanic_app.py
│
├── data/
│   ├── cleaned/
│   ├── Housing.csv
│   └── Titanic-Dataset.csv
│
├── figures/
│   ├── housing/
│   └── titanic/
│
├── models/
│   ├── housing_optimized_gradient_boosting.pkl
│   ├── housing_price_model.joblib
│   └── titanic_optimized_gradient_boosting.pkl
│
├── notebooks/
│   ├── week7_housing_model_deployment.ipynb
│   └── ...
│
├── reports/
│   ├── week7_model_deployment_report.md
│   └── ...
│
├── streamlit_app.py
├── titanic_streamlit_app.py
├── requirements.txt
└── README.md
9. Running the Applications
9.1 Activate the Virtual Environment
source .venv/bin/activate
9.2 Install Dependencies
pip install -r requirements.txt
9.3 Run Housing API
.venv/bin/python -m uvicorn api.app:app --reload --port 8000

Open:

http://127.0.0.1:8000/docs
9.4 Run Titanic API
.venv/bin/python -m uvicorn api.titanic_app:app --reload --port 8001

Open:

http://127.0.0.1:8001/docs
9.5 Run Housing Streamlit Application
python -m streamlit run streamlit_app.py
9.6 Run Titanic Streamlit Application
python -m streamlit run titanic_streamlit_app.py
10. Key Challenges

Several challenges were encountered during deployment.

Python Virtual Environment Configuration

Kali Linux uses an externally managed Python environment. Attempting to install packages globally resulted in a PEP 668 error.

This was resolved by creating a dedicated virtual environment:

python3 -m venv .venv

and installing the project dependencies inside it.

Uvicorn Environment Mismatch

The system-level Uvicorn executable initially used a different Python environment from the project virtual environment. This caused the API to fail when loading the Scikit-learn model.

The issue was resolved by explicitly running:

.venv/bin/python -m uvicorn

This ensured that FastAPI, Scikit-learn, Joblib, Pandas, and the saved models all used the same environment.

Model File Paths

The model files had initially been stored in a notebook-specific directory. The models were organized under the project's central models/ directory and the API paths were updated accordingly.

Streamlit Interface

The Streamlit application initially appeared empty because changes had not been saved. After saving the source code, the application loaded correctly.

11. Key Lessons Learned

Week 7 demonstrated that developing a machine learning model is only one stage of a complete machine learning workflow.

Key lessons included:

Machine learning models can be serialized using Joblib.
Saved models can be reused without retraining.
FastAPI can expose machine learning models through REST endpoints.
Pydantic provides structured input validation for APIs.
Swagger UI makes API testing easier.
Streamlit can provide a simple interface for non-technical users.
Python virtual environments are important for dependency isolation.
Deployment introduces practical issues involving file paths, dependencies, ports, and runtime environments.
Successful model deployment requires consistency between the training environment and production environment.
12. Conclusion

Week 7 successfully transformed the previously developed machine learning models into usable applications.

The House Price Prediction model and Titanic Survival Prediction model were both serialized, loaded into FastAPI applications, tested through prediction endpoints, and connected to Streamlit interfaces.

The completed workflow now covers the complete machine learning lifecycle:

Data
  ↓
Data Cleaning
  ↓
EDA
  ↓
Statistical Analysis
  ↓
Model Development
  ↓
Model Comparison
  ↓
Feature Engineering
  ↓
Model Optimization
  ↓
Model Serialization
  ↓
API Deployment
  ↓
User Interface
  ↓
Prediction

This demonstrates the transition from experimental machine learning notebooks to practical, user-facing machine learning applications.


Save and exit.

---

# Step 4 — Update requirements

Your simplified requirements are good:

```text
fastapi
uvicorn
streamlit
requests
pandas
numpy
scikit-learn
joblib

Keep them exactly like that for now.

Don't pin versions tonight. We are optimizing for getting the project completed, and the environment is already working.
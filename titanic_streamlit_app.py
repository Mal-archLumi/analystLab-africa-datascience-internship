import streamlit as st
import requests


st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)


st.title("🚢 Titanic Survival Predictor")
st.write(
    "Enter passenger information to predict whether "
    "the passenger would have survived the Titanic disaster."
)

st.divider()


# Passenger information
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    sex = st.selectbox(
        "Sex",
        ["female", "male"]
    )

    age = st.number_input(
        "Age",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

    sibsp = st.number_input(
        "Siblings / Spouses Aboard",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

with col2:
    parch = st.number_input(
        "Parents / Children Aboard",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    fare = st.number_input(
        "Fare",
        min_value=0.0,
        value=50.0
    )

    embarked = st.selectbox(
        "Port of Embarkation",
        ["S", "C", "Q"]
    )

    title = st.selectbox(
        "Title",
        ["Mr", "Miss", "Mrs", "Master", "Rare"]
    )


st.divider()


if st.button(
    "Predict Survival",
    type="primary",
    use_container_width=True
):

    payload = {
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked,
        "Title": title
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8001/predict",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            if result["prediction"] == 1:
                st.success(
                    "🎉 Prediction: Passenger Survived"
                )
            else:
                st.error(
                    "Prediction: Passenger Did Not Survive"
                )

            st.metric(
                "Prediction",
                result["survival_status"]
            )

        else:
            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the Titanic API. "
            "Make sure the FastAPI server is running on port 8001."
        )
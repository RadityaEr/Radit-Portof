import streamlit as st
import numpy as np
import joblib
import os
import sys
import sklearn

st.title("Environment Debug Info")
st.text(f"Python executable path: {sys.executable}")
st.text(f"scikit-learn version: {sklearn.__version__}")



def show_ml_project_a():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the model file
    model_path = os.path.join(script_dir, "best_gbr_model.pkl")

    # Load the model
    best_gbr_model = joblib.load(model_path)

    st.title("House Price Prediction")

    # User inputs for numerical features
    longitude = st.number_input("Longitude", format="%.6f")
    latitude = st.number_input("Latitude", format="%.6f")
    housing_median_age = st.number_input("Housing Median Age", min_value=0.0)
    median_income = st.number_input("Median Income", min_value=0.0)
    rooms_per_household = st.number_input("Rooms per Household", min_value=0.0)
    bedrooms_per_room = st.number_input("Bedrooms per Room", min_value=0.0)
    population_per_household = st.number_input("Population per Household", min_value=0.0)

    # Dropdown for ocean proximity
    ocean_proximity = st.selectbox("Ocean Proximity", [
        "1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"
    ])

    # One-hot encoding map
    ocean_mapping = {
        "1H OCEAN": [1, 0, 0, 0, 0],
        "INLAND": [0, 1, 0, 0, 0],
        "ISLAND": [0, 0, 1, 0, 0],
        "NEAR BAY": [0, 0, 0, 1, 0],
        "NEAR OCEAN": [0, 0, 0, 0, 1],
    }

    # Predict button
    if st.button("Predict"):
        input_data = np.array([
            longitude,
            latitude,
            housing_median_age,
            median_income,
            rooms_per_household,
            bedrooms_per_room,
            population_per_household,
            *ocean_mapping[ocean_proximity]
        ]).reshape(1, -1)

        prediction = best_gbr_model.predict(input_data)[0]
        st.success(f"Predicted Value: ${prediction:,.2f}")

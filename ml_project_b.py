import streamlit as st
import numpy as np
import joblib
import os

def show_ml_project_b():
    st.title("ML Project B: Customer Input Form")

    # Gender selection
    gender = st.selectbox("Gender", ["Male", "Female", "Rather not say"])

    # Senior Citizen status
    senior_citizen = st.radio("Are you a Senior Citizen?", ["Yes", "No"])

    # Dependents status
    has_dependents = st.radio("Do you have dependents?", ["Yes", "No"])

    # Partner status
    has_partner = st.radio("Do you have a partner?", ["Yes", "No"])

    # Contract type
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

    # Payment Method
    payment_method = st.selectbox(
        "Payment Method", 
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", 
         "Credit card (automatic)", "Prefer not to say"]
    )

    # Monthly Charges
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, format="%.2f")

    # Total Charges
    total_charges = st.number_input("Total Charges", min_value=0.0, format="%.2f")

    # Tenure
    tenure = st.number_input("Tenure (in months)", min_value=0.0, format="%.1f")

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the model file
    model_path = os.path.join(script_dir, "best_rfmodel.pkl")

    # Load the model
    best_rf_model = joblib.load(model_path)

    # Prediction button
    if st.button("Predict", key="predict_button"):
        # Convert inputs into appropriate format
        gender_val = 1 if gender == "Male" else 0
        senior_val = 1 if senior_citizen == "Yes" else 0
        partner_val = 1 if has_partner == "Yes" else 0
        dependents_val = 1 if has_dependents == "Yes" else 0

        contract_vals = {
            "Month-to-month": [1, 0, 0],
            "One year": [0, 1, 0],
            "Two year": [0, 0, 1]
        }
        contract_encoded = contract_vals[contract]

        payment_vals = {
            "Bank transfer (automatic)": [1, 0, 0, 0],
            "Credit card (automatic)": [0, 1, 0, 0],
            "Electronic check": [0, 0, 1, 0],
            "Mailed check": [0, 0, 0, 1],
            "Prefer not to say": [0, 0, 0, 0],
        }
        payment_encoded = payment_vals[payment_method]

        input_data = np.array([
            gender_val,
            senior_val,
            partner_val,
            dependents_val,
            tenure,
            1,  # Assuming PaperlessBilling = 1
            monthly_charges,
            *contract_encoded,
            *payment_encoded
        ]).reshape(1, -1)

        prediction = best_rf_model.predict(input_data)[0]

        if prediction == 1:
            st.error("This customer is predicted to **churn**.")
        else:
            st.success("This customer is predicted to **not churn**.")

import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("GB_ECG.joblib")

# Feature names (order matters)
FEATURE_NAMES = [
    "QRS_duration", "PR_interval", "QT_interval", "T_interval", "P_interval",
    "QRS", "T", "P", "QRST", "Heart_Rate", "RR_interval", "HRV", "SPO2", "Temperature", "Weight"
]

st.set_page_config(page_title="Parkinson's Prediction from ECG", layout="centered")

st.title("🩺 Parkinson's Disease Prediction using ECG Data")

st.markdown("""
Enter **15 ECG and vital parameters** as comma-separated values in this exact order:

**QRS_duration, PR_interval, QT_interval, T_interval, P_interval, QRS, T, P, QRST, Heart_Rate, RR_interval, HRV, SPO2, Temperature, Weight**
""")

# Example input
example = "106.4989,112.6618,302.4316,147.211,100.8603,1.4115,27.2654,104.8939,-34.8096,89,107.4648,58.5444,93.89,96.32,111.1086"
input_data = st.text_area("🔢 Enter your values below:", example, height=100)

if st.button("🔍 Predict"):
    try:
        values = [float(x.strip()) for x in input_data.split(",")]
        if len(values) != len(FEATURE_NAMES):
            st.error(f"⚠️ Expected {len(FEATURE_NAMES)} values, but got {len(values)}.")
        else:
            input_array = np.array(values).reshape(1, -1)
            prediction = model.predict(input_array)[0]

            # Save the input data and prediction result to session state
            st.session_state["ecg_input_data"] = input_data
            st.session_state["ecg_result"] = "Healthy" if prediction == 0 else "Parkinson's Disease"

            if prediction == 0:
                st.success("✅ The person is **Healthy**.")
            else:
                st.error("🚨 The person is predicted to have **Parkinson's Disease**.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

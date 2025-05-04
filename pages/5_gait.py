import streamlit as st
import joblib
import numpy as np
# from gait_final import GaitModel  # This should have GaitModel class and required functions

# Load models
chest_model = joblib.load("AB_Gait_Chest.joblib")
hand_model = joblib.load("AB_Gait_Hand.joblib")

# Function to preprocess input
def parse_input(input_str):
    try:
        values = list(map(float, input_str.strip().split(',')))
        if len(values) != 300:
            return None, "Input must contain exactly 300 comma-separated values."
        return np.array(values).reshape(1, -1), None
    except ValueError:
        return None, "Please enter only numeric values separated by commas."

# UI
st.title("Gait Analysis for Parkinson Detection")
st.markdown("This app analyzes gait data from **Chest** and **Hand** sensors to detect Parkinson’s Disease.")

# --- Chest Section ---
st.header("📍 Chest Gait Data")
chest_input = st.text_area("Enter 300 comma-separated values for chest sensor:")

if st.button("Analyze Chest"):
    chest_array, error = parse_input(chest_input)
    if error:
        st.error(error)
    else:
        prediction = chest_model.predict(chest_array)[0]
        result = "🟢 Healthy" if prediction == 0 else "🔴 Parkinson"
        st.success(f"**Chest Gait Prediction:** {result}")

                # Save to session
        st.session_state["gait_chest_result"] = result
        st.session_state["gait_chest_data"] = chest_array

# --- Divider ---
st.markdown("---")

# --- Hand Section ---
st.header("📍 Hand Gait Data")
hand_input = st.text_area("Enter 300 comma-separated values for hand sensor:")

if st.button("Analyze Hand"):
    hand_array, error = parse_input(hand_input)
    if error:
        st.error(error)
    else:
        prediction = hand_model.predict(hand_array)[0]
        result = "🟢 Healthy" if prediction == 0 else "🔴 Parkinson"
        st.success(f"**Hand Gait Prediction:** {result}")

         # Save to session
        st.session_state["gait_hand_result"] = result
        st.session_state["gait_hand_data"] = hand_array

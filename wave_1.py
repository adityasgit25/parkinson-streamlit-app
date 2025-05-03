import streamlit as st
import joblib
from keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model_path = "Wave_KNNC.joblib"
    return joblib.load(model_path)

loaded_model = load_model()

# Prediction function
def predict_parkinson(image_file):
    try:
        # Preprocess the image
        img = Image.open(image_file).convert("L")  # Convert to grayscale
        img = img.resize((210, 210))  # Resize to match training size
        img_array = image.img_to_array(img)  # Convert to numpy array
        mean_intensity = np.mean(img_array)  # Extract mean pixel intensity
        mean_intensity = np.array([[mean_intensity]])  # Reshape for model

        # Make prediction
        prediction = loaded_model.predict(mean_intensity)[0]

        # Interpret the prediction
        if prediction == 0:
            return "The Patient is Healthy"
        elif prediction == 1:
            return "The Patient is affected by Parkinson's Disease"
        else:
            return "Unknown Prediction"
    except Exception as e:
        return f"Error during prediction: {e}"

# Streamlit interface
st.title("Parkinson's Disease Detection from Wave Drawings")
st.write("Upload a wave drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# Image upload
uploaded_file = st.file_uploader("Choose a wave drawing image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Perform prediction
    result = predict_parkinson(uploaded_file)
    st.write("Prediction Result:")
    st.success(result)

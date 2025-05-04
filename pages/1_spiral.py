import streamlit as st

st.set_page_config(page_title="Spiral Model", page_icon="🌀")

import joblib
from keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO




# Load the trained model
@st.cache_resource
def load_model():
    model_path = "Spiral_DTC.joblib"
    return joblib.load(model_path)

loaded_model = load_model()

# Prediction function
def predict_parkinson(image_file):
    try:
        # Preprocess the image
        img = Image.open(image_file)
        img = img.resize((210, 210))  # Resize to model's expected input
        img_array = image.img_to_array(img)
        img_array = img_array.mean()  # Calculate the mean pixel value
        img_array = np.array(img_array).reshape(1, -1)  # Reshape for prediction

        # Make prediction
        prediction = loaded_model.predict(img_array)[0]

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
st.title("Parkinson's Disease Detection from Spiral Drawings")
st.write("Upload a spiral drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# Image upload
uploaded_file = st.file_uploader("Choose a spiral drawing image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Perform prediction
    result = predict_parkinson(uploaded_file)
    st.write("Prediction Result:")
    st.success(result)

    # Store result in session state
    st.session_state["spiral_result"] = result

    # Save image bytes for report
    uploaded_file.seek(0)  # Reset file pointer
    image_bytes = uploaded_file.read()
    st.session_state["spiral_image_bytes"] = image_bytes

    st.info("✅ Spiral result and image saved for report.")

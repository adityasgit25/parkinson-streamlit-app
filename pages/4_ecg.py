# import streamlit as st
# import numpy as np
# import joblib
# from PIL import Image
# import io

# # Load the pre-trained Gradient Boosting model
# model = joblib.load('GB_ECG.joblib')

# # Set page configuration
# st.set_page_config(page_title="Parkinson's Disease Prediction", layout="wide")

# # Title and description
# st.title("Parkinson's Disease Prediction from ECG Data")
# st.markdown("""
# This application predicts whether a patient has Parkinson's disease based on ECG parameters.
# Please enter the required 8 values and upload two images for analysis. Results and images will be displayed below.
# """)



# st.header("Input ECG Parameters")
# st.write("Enter the following 8 values separated by commas in this order: QRS_duration, PR_interval, QT_interval, T_interval, Heart_Rate, HRV, SPO2, Temperature")

# # Text input for comma-separated values
# input_string = st.text_input("Enter values (comma-separated):", "")

# # Image upload section
# st.header("Upload Images")
# st.write("Please upload two images related to the patient's ECG or medical records.")

# # File uploaders for two images
# image1 = st.file_uploader("Upload First Image", type=["jpg", "png", "jpeg"], key="image1")
# image2 = st.file_uploader("Upload Second Image", type=["jpg", "png", "jpeg"], key="image2")

# # Prediction button
# if st.button("Predict"):
#     # Validate inputs
#     if not input_string:
#         st.error("Please enter the ECG parameter values.")
#     elif not image1 or not image2:
#         st.error("Please upload both images.")
#     else:
#         try:
#             # Process input string
#             input_list = [float(x.strip()) for x in input_string.split(',')]
            
#             # Validate number of inputs
#             if len(input_list) != 8:
#                 st.error(f"Error: You entered {len(input_list)} values. Exactly 8 are required.")
#             else:
#                 # Prepare input for prediction
#                 input_data = np.array([input_list])  # Shape: (1, 8)
                
#                 # Perform prediction
#                 prediction = model.predict(input_data)
                
#                 # Store prediction and images in session state
#                 st.session_state["ecg_result"] = "The patient is predicted to have Parkinson's disease." if prediction[0] == 1 else "The patient is predicted to be healthy."
#                 st.session_state.image1_bytes = image1.read()
#                 st.session_state.image2_bytes = image2.read()
                
#                 # Display success message
#                 st.success("Prediction completed!")
                
#         except ValueError:
#             st.error("Invalid input format. Please enter numeric values separated by commas.")

# # Result section
# st.header("Prediction Results")

# # Initialize session state if not already done
# if "ecg_result" not in st.session_state:
#     st.session_state.prediction = None
# if 'image1_bytes' not in st.session_state:
#     st.session_state.image1_bytes = None
# if 'image2_bytes' not in st.session_state:
#     st.session_state.image2_bytes = None

# # Display prediction if available
# if st.session_state["ecg_result"]:
#     st.write(f"**Prediction**: {st.session_state["ecg_result"]}")
    
#     # Display uploaded images
#     st.subheader("Uploaded Images")
#     img_col1, img_col2 = st.columns(2)
    
#     with img_col1:
#         if st.session_state.image1_bytes:
#             st.image(st.session_state.image1_bytes, caption="First Image", use_column_width=True)
    
#     with img_col2:
#         if st.session_state.image2_bytes:
#             st.image(st.session_state.image2_bytes, caption="Second Image", use_column_width=True)
# else:
#     st.write("No prediction yet. Please enter values, upload images, and click 'Predict'.")

# # # Clear results button at the bottom
# # if st.button("Clear Results"):
# #     st.session_state.prediction = None
# #     st.session_state.image1_bytes = None
# #     st.session_state.image2_bytes = None
# #     st.experimental_rerun()



import streamlit as st
import numpy as np
import joblib
from PIL import Image
import io

# ECG parameter names
ECG_PARAM_NAMES = [
    "QRS_duration", "PR_interval", "QT_interval", "T_interval",
    "Heart_Rate", "HRV", "SPO2", "Temperature"
]

# Load the pre-trained Gradient Boosting model
model = joblib.load('GB_ECG.joblib')

# Set page configuration
st.set_page_config(page_title="Parkinson's Disease Prediction", layout="wide")

# Title and description
st.title("Parkinson's Disease Prediction from ECG Data")
st.markdown("""
This application predicts whether a patient has Parkinson's disease based on ECG parameters.
Please enter the required 8 values and upload two images for analysis. Results and images will be displayed below.
""")

st.header("Input ECG Parameters")
st.write("Enter the following 8 values separated by commas in this order: QRS_duration, PR_interval, QT_interval, T_interval, Heart_Rate, HRV, SPO2, Temperature")

# Text input for comma-separated values
input_string = st.text_input("Enter values (comma-separated):", "")

# Image upload section
st.header("Upload Images")
st.write("Please upload two images related to the patient's ECG or medical records.")

# File uploaders for two images
image1 = st.file_uploader("Upload ECG Image 1", type=["jpg", "png", "jpeg"], key="ecg_image1")
image2 = st.file_uploader("Upload ECG Image 2", type=["jpg", "png", "jpeg"], key="ecg_image2")

# Initialize session state if not already done
if "ecg_result" not in st.session_state:
    st.session_state["ecg_result"] = None
if "ecg_image1_bytes" not in st.session_state:
    st.session_state["ecg_image1_bytes"] = None
if "ecg_image2_bytes" not in st.session_state:
    st.session_state["ecg_image2_bytes"] = None

# Prediction button
if st.button("Predict"):
    # Validate inputs
    if not input_string:
        st.error("Please enter the ECG parameter values.")
    elif not image1 or not image2:
        st.error("Please upload both images.")
    else:
        try:
            # Process input string
            input_list = [float(x.strip()) for x in input_string.split(',')]
            
            # Validate number of inputs
            if len(input_list) != 8:
                st.error(f"Error: You entered {len(input_list)} values. Exactly 8 are required.")
            else:
                # Prepare input for prediction
                input_data = np.array([input_list])  # Shape: (1, 8)
                
                # Perform prediction
                prediction = model.predict(input_data)
                
                # Store prediction and images in session state
                st.session_state["ecg_result"] = (
                    "The patient is predicted to have Parkinson's disease."
                    if prediction[0] == 1 else
                    "The patient is predicted to be healthy."
                )
                st.session_state["ecg_image1_bytes"] = image1.read()
                st.session_state["ecg_image2_bytes"] = image2.read()
                # Store ECG data as a dict with parameter names
                st.session_state["ecg_input_data"] = dict(zip(ECG_PARAM_NAMES, input_list))

                # Display success message
                st.success("Prediction completed!")
                
        except ValueError:
            st.error("Invalid input format. Please enter numeric values separated by commas.")

# Result section
st.header("Prediction Results")

# Display prediction if available
if st.session_state["ecg_result"]:
    st.write(f"**Prediction**: {st.session_state['ecg_result']}")
    
    # Display ECG input data
    if "ecg_input_data" in st.session_state:
        st.subheader("ECG Input Data")
        st.table(st.session_state["ecg_input_data"])

    # Display uploaded images
    st.subheader("Uploaded ECG Images")
    img_col1, img_col2 = st.columns(2)
    
    with img_col1:
        if st.session_state["ecg_image1_bytes"]:
            st.image(st.session_state["ecg_image1_bytes"], caption="ECG Image 1", use_column_width=True)
    
    with img_col2:
        if st.session_state["ecg_image2_bytes"]:
            st.image(st.session_state["ecg_image2_bytes"], caption="ECG Image 2", use_column_width=True)
else:
    st.write("No prediction yet. Please enter values, upload images, and click 'Predict'.")

# # Clear results button at the bottom (optional)
# if st.button("Clear Results"):
#     st.session_state["ecg_result"] = None
#     st.session_state["ecg_image1_bytes"] = None
#     st.session_state["ecg_image2_bytes"] = None
#     st.experimental_rerun()
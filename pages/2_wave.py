# import streamlit as st

# # ✅ Move set_page_config to the first line
# st.set_page_config(page_title="Wave Model", page_icon="🌊")

# import joblib
# from keras.preprocessing import image
# # from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image
# from io import BytesIO



# # Load the trained model
# @st.cache_resource
# def load_model():
#     model_path = "Wave_KNNC.joblib"
#     return joblib.load(model_path)

# loaded_model = load_model()

# # Prediction function
# def predict_parkinson(image_file):
#     try:
#         # Preprocess the image
#         img = Image.open(image_file).convert("L")  # Convert to grayscale
#         img = img.resize((210, 210))  # Resize to match training size
#         img_array = image.img_to_array(img)  # Convert to numpy array
#         mean_intensity = np.mean(img_array)  # Extract mean pixel intensity
#         mean_intensity = np.array([[mean_intensity]])  # Reshape for model

#         # Make prediction
#         prediction = loaded_model.predict(mean_intensity)[0]

#         # Interpret the prediction
#         if prediction == 0:
#             return "The Patient is Healthy"
#         elif prediction == 1:
#             return "The Patient is affected by Parkinson's Disease"
#         else:
#             return "Unknown Prediction"
#     except Exception as e:
#         return f"Error during prediction: {e}"

# # Streamlit interface
# st.title("Parkinson's Disease Detection from Wave Drawings")
# st.write("Upload a wave drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# # Image upload
# uploaded_file = st.file_uploader("Choose a wave drawing image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Display the uploaded image
#     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

#     # Perform prediction
#     result = predict_parkinson(uploaded_file)
#     st.write("Prediction Result:")
#     st.success(result)


#      # Save the result in session state
#     st.session_state["wave_result"] = result

#     # Save the image in session state as bytes for later report generation
#     uploaded_file.seek(0)  # Reset the file pointer to the start
#     image_bytes = uploaded_file.read()
#     st.session_state["wave_image_bytes"] = image_bytes

#     st.info("✅ Wave result and image saved for report.")







#---------------------------------------------------
# this is with the reference image
# USE THIS IF TREMOR LATER ONE DOESN'T WORKS!
# import streamlit as st
# # Set page config at the top
# st.set_page_config(page_title="Wave Model", page_icon="🌊")

# import joblib
# import numpy as np
# import pandas as pd
# from PIL import Image
# from io import BytesIO
# import cv2
# from scipy.signal import correlate2d
# from skimage.metrics import structural_similarity as ssim
# import matplotlib.pyplot as plt

# # Load the trained model
# @st.cache_resource
# def load_model():
#     # model_path = "Wave_KNNC.joblib"
#     model_path = "Wave_CATBC.joblib"
#     return joblib.load(model_path)

# # Load the reference wave image
# @st.cache_resource
# def load_reference_image():
#     try:
#         # Load the reference image from file
#         ref_img_path = "reference_wave.jpeg"
#         ref_img = cv2.imread(ref_img_path, cv2.IMREAD_GRAYSCALE)
        
#         # Resize to match our processing dimensions
#         ref_img = cv2.resize(ref_img, (210, 210))
        
#         return ref_img
#     except Exception as e:
#         st.error(f"Error loading reference image: {e}")
#         # Create a fallback simulated wave if the image can't be loaded
#         ref_img = np.zeros((210, 210), dtype=np.uint8)
#         # Create a simple sine wave pattern
#         for x in range(210):
#             y = int(105 + 50 * np.sin(x * 0.05))
#             if 0 <= y < 210:
#                 ref_img[y, x] = 255
#                 ref_img[y+1, x] = 255
#                 ref_img[y-1, x] = 255
#         return ref_img

# loaded_model = load_model()
# reference_wave = load_reference_image()

# # Image preprocessing
# def preprocess_image(image_file):
#     img = Image.open(image_file).convert("L")  # Convert to grayscale
#     img = img.resize((210, 210))  # Resize to match training size
#     img_array = np.array(img)
#     return img_array

# # Calculate similarity metrics
# def calculate_similarity(user_img, ref_img):
#     # Ensure both images are properly shaped
#     user_img = cv2.resize(user_img, (210, 210))
#     ref_img = cv2.resize(ref_img, (210, 210))
    
#     # 1. Structural Similarity Index (SSIM)
#     ssim_score, _ = ssim(user_img, ref_img, full=True)
    
#     # 2. Cross-Correlation
#     cross_corr = np.max(correlate2d(user_img, ref_img, mode='same'))
#     normalized_corr = cross_corr / (np.sum(user_img) * np.sum(ref_img))
    
#     # 3. Mean Squared Error
#     mse = np.mean((user_img - ref_img) ** 2)
#     max_pixel = 255.0
#     psnr = 10 * np.log10((max_pixel ** 2) / mse) if mse > 0 else 100
    
#     return {
#         "SSIM": ssim_score,
#         "Normalized Correlation": normalized_corr,
#         "PSNR": psnr,
#         "MSE": mse
#     }

# # Prediction function
# def predict_parkinson(image_file):
#     try:
#         # Preprocess the image
#         img_array = preprocess_image(image_file)
        
#         # Extract mean pixel intensity for the model
#         mean_intensity = np.mean(img_array)
#         mean_intensity = np.array([[mean_intensity]])
        
#         # Make model prediction
#         prediction = loaded_model.predict(mean_intensity)[0]

#         # # Use all pixels as features (flattened)
#         # flat_pixels = img_array.flatten().reshape(1, -1)
#         # prediction = loaded_model.predict(flat_pixels)[0]
        
#         # Interpret the model prediction
#         if prediction == 0:
#             model_result = "The Patient is Healthy"
#         elif prediction == 1:
#             model_result = "The Patient is affected by Parkinson's Disease"
#         else:
#             model_result = "Unknown Prediction"
            
#         return model_result, img_array
        
#     except Exception as e:
#         return f"Error during prediction: {e}", None

# # Function to visualize the comparison
# def create_comparison_visualization(user_img, ref_img):
#     fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
#     # User's wave
#     ax1.imshow(user_img, cmap='gray')
#     ax1.set_title("User's Wave Drawing")
#     ax1.axis('off')
    
#     # Reference wave
#     ax2.imshow(ref_img, cmap='gray')
#     ax2.set_title("Reference Wave")
#     ax2.axis('off')
    
#     # Overlay both
#     ax3.imshow(ref_img, cmap='gray', alpha=0.5)
#     ax3.imshow(user_img, cmap='hot', alpha=0.5)
#     ax3.set_title("Overlay Comparison")
#     ax3.axis('off')
    
#     plt.tight_layout()
#     return fig

# # Streamlit interface
# st.title("Parkinson's Disease Detection from Wave Drawings")
# st.write("Upload a wave drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# # Show the reference wave
# st.subheader("Reference Wave Pattern")
# st.image(reference_wave, caption="Standard Wave Pattern for Comparison", use_column_width=True)

# # Image upload
# uploaded_file = st.file_uploader("Choose a wave drawing image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Display the uploaded image
#     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
#     # Perform prediction
#     result, processed_img = predict_parkinson(uploaded_file)
    
#     if processed_img is not None:
#         # Display prediction result
#         st.subheader("Prediction Result:")
#         st.success(result)
        
#         # Create and display comparison visualization
#         st.subheader("Visual Comparison:")
#         comparison_fig = create_comparison_visualization(processed_img, reference_wave)
#         st.pyplot(comparison_fig)
        
#         # Save the result in session state
#         st.session_state["wave_result"] = result
        
#         # Save the image in session state as bytes for later report generation
#         uploaded_file.seek(0)  # Reset the file pointer to the start
#         image_bytes = uploaded_file.read()
#         st.session_state["wave_image_bytes"] = image_bytes
        
#         st.info("✅ Wave result and image saved for report.")
#     else:
#         st.error(result)  # Display the error message



# WITH TREMOR CALCULATION
import streamlit as st
# Set page config at the top
st.set_page_config(page_title="Wave Model", page_icon="🌊")

import joblib
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO
import cv2
from scipy.signal import correlate2d
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

# Load the trained model
@st.cache_resource
def load_model():
    model_path = "Wave_CATBC.joblib"
    return joblib.load(model_path)

# Load the reference wave image
@st.cache_resource
def load_reference_image():
    try:
        ref_img_path = "reference_wave.jpeg"
        ref_img = cv2.imread(ref_img_path, cv2.IMREAD_GRAYSCALE)
        ref_img = cv2.resize(ref_img, (210, 210))
        return ref_img
    except Exception as e:
        st.error(f"Error loading reference image: {e}")
        ref_img = np.zeros((210, 210), dtype=np.uint8)
        for x in range(210):
            y = int(105 + 50 * np.sin(x * 0.05))
            if 0 <= y < 210:
                ref_img[y, x] = 255
                ref_img[y+1, x] = 255
                ref_img[y-1, x] = 255
        return ref_img

loaded_model = load_model()
reference_wave = load_reference_image()

# Image preprocessing
def preprocess_image(image_file):
    img = Image.open(image_file).convert("L")  
    img = img.resize((210, 210))  
    img_array = np.array(img)
    return img_array

# Calculate similarity metrics (for tremor analysis)
def calculate_similarity(user_img, ref_img):
    user_img = cv2.resize(user_img, (210, 210))
    ref_img = cv2.resize(ref_img, (210, 210))
    
    ssim_score, _ = ssim(user_img, ref_img, full=True)
    cross_corr = np.max(correlate2d(user_img, ref_img, mode='same'))
    normalized_corr = cross_corr / (np.sum(user_img) * np.sum(ref_img))
    mse = np.mean((user_img - ref_img) ** 2)
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse) if mse > 0 else 100
    
    tremor_percentage = (1 - ssim_score) * 100  # Higher SSIM means less tremor, so we calculate the percentage based on SSIM
    
    return {
        "SSIM": ssim_score,
        "Normalized Correlation": normalized_corr,
        "PSNR": psnr,
        "MSE": mse,
        "Tremor Percentage": tremor_percentage
    }

# Prediction function
# Updated Prediction function with SSIM calculation
def predict_parkinson(image_file):
    try:
        # Preprocess the image
        img_array = preprocess_image(image_file)
        
        # Calculate similarity metrics
        similarity_metrics = calculate_similarity(img_array, reference_wave)
        
        # Extract mean pixel intensity for the model
        mean_intensity = np.mean(img_array)
        mean_intensity = np.array([[mean_intensity]])
        
        # Make model prediction
        prediction = loaded_model.predict(mean_intensity)[0]

        # Interpret the model prediction
        if prediction == 0:
            model_result = "The Patient is Healthy"
        elif prediction == 1:
            model_result = "The Patient is affected by Parkinson's Disease"
        else:
            model_result = "Unknown Prediction"
            
        # Return the result, SSIM, and processed image
        return model_result, similarity_metrics, img_array
        
    except Exception as e:
        return f"Error during prediction: {e}", None, None
    

# Function to visualize the comparison
def create_comparison_visualization(user_img, ref_img):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    ax1.imshow(user_img, cmap='gray')
    ax1.set_title("User's Wave Drawing")
    ax1.axis('off')
    
    ax2.imshow(ref_img, cmap='gray')
    ax2.set_title("Reference Wave")
    ax2.axis('off')
    
    ax3.imshow(ref_img, cmap='gray', alpha=0.5)
    ax3.imshow(user_img, cmap='hot', alpha=0.5)
    ax3.set_title("Overlay Comparison")
    ax3.axis('off')
    
    plt.tight_layout()
    return fig

# Streamlit interface
st.title("Parkinson's Disease Detection from Wave Drawings")
st.write("Upload a wave drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# Show the reference wave
st.subheader("Reference Wave Pattern")
st.image(reference_wave, caption="Standard Wave Pattern for Comparison", use_column_width=True)

# Image upload
uploaded_file = st.file_uploader("Choose a wave drawing image", type=["png", "jpg", "jpeg"])

# Streamlit interface updates to display SSIM score
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Perform prediction and get similarity metrics
    result, similarity_metrics, processed_img = predict_parkinson(uploaded_file)
    
    if processed_img is not None:
        # Display prediction result
        st.subheader("Prediction Result:")
        st.success(result)
        
        # Display similarity metrics
        st.subheader("Similarity Metrics:")
        st.write(f"SSIM Score: {similarity_metrics['SSIM']:.4f}")
        st.write(f"Normalized Correlation: {similarity_metrics['Normalized Correlation']:.4f}")
        st.write(f"PSNR: {similarity_metrics['PSNR']:.4f} dB")
        st.write(f"MSE: {similarity_metrics['MSE']:.4f}")
        
        # Create and display comparison visualization
        st.subheader("Visual Comparison:")
        comparison_fig = create_comparison_visualization(processed_img, reference_wave)
        st.pyplot(comparison_fig)
        
        # Save the result in session state
        st.session_state["wave_result"] = result
        
        # Save the image in session state as bytes for later report generation
        uploaded_file.seek(0)  # Reset the file pointer to the start
        image_bytes = uploaded_file.read()
        st.session_state["wave_image_bytes"] = image_bytes
        
        st.info("✅ Wave result and image saved for report.")
    else:
        st.error(result)  # Display the error message

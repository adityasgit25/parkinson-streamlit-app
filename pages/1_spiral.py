# import streamlit as st

# st.set_page_config(page_title="Spiral Model", page_icon="🌀")

# import joblib
# from keras.preprocessing import image
# import numpy as np
# from PIL import Image
# from io import BytesIO




# # Load the trained model
# @st.cache_resource
# def load_model():
#     model_path = "Spiral_DTC.joblib"
#     return joblib.load(model_path)

# loaded_model = load_model()

# # Prediction function
# def predict_parkinson(image_file):
#     try:
#         # Preprocess the image
#         img = Image.open(image_file)
#         img = img.resize((210, 210))  # Resize to model's expected input
#         img_array = image.img_to_array(img)
#         img_array = img_array.mean()  # Calculate the mean pixel value
#         img_array = np.array(img_array).reshape(1, -1)  # Reshape for prediction

#         # Make prediction
#         prediction = loaded_model.predict(img_array)[0]

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
# st.title("Parkinson's Disease Detection from Spiral Drawings")
# st.write("Upload a spiral drawing, and the model will predict if the patient is healthy or affected by Parkinson's Disease.")

# # Image upload
# uploaded_file = st.file_uploader("Choose a spiral drawing image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Display the uploaded image
#     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

#     # Perform prediction
#     result = predict_parkinson(uploaded_file)
#     st.write("Prediction Result:")
#     st.success(result)

#     # Store result in session state
#     st.session_state["spiral_result"] = result

#     # Save image bytes for report
#     uploaded_file.seek(0)  # Reset file pointer
#     image_bytes = uploaded_file.read()
#     st.session_state["spiral_image_bytes"] = image_bytes

#     st.info("✅ Spiral result and image saved for report.")




# this is with the reference image.
# import streamlit as st
# import joblib
# import numpy as np
# from PIL import Image
# import cv2
# from keras.preprocessing import image
# from io import BytesIO
# import os
# import base64

# # Page configuration
# st.set_page_config(page_title="Spiral Analysis", page_icon="🌀", layout="wide")

# # Hide code with CSS
# st.markdown("""
# <style>
#     /* Hide all code-related elements */
#     .stCodeBlock, pre, code, .CodeMirror, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
#         display: none !important;
#     }
    
#     /* Hide streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
    
#     /* Custom styling */
#     .stApp {
#         background-color: #1E1E2E !important;
#         color: #E0E0E0;
#     }
    
#     h1, h2, h3 {
#         color: #64B5F6;
#         font-weight: 500;
#     }
    
#     .content-card {
#         background-color: #2A2A40;
#         border-radius: 10px;
#         padding: 1.5rem;
#         margin-bottom: 1.5rem;
#     }
    
#     .result-card {
#         padding: 1rem;
#         border-radius: 8px;
#         margin-top: 1rem;
#     }
    
#     .result-card.healthy {
#         background-color: rgba(76, 175, 80, 0.2);
#         border-left: 4px solid #4CAF50;
#     }
    
#     .result-card.parkinsons {
#         background-color: rgba(244, 67, 54, 0.2);
#         border-left: 4px solid #F44336;
#     }
    
#     .metric-card {
#         background-color: rgba(100, 181, 246, 0.1);
#         border-radius: 8px;
#         padding: 1rem;
#         text-align: center;
#         margin-bottom: 1rem;
#     }
    
#     .metric-value {
#         font-size: 1.8rem;
#         font-weight: 500;
#         color: #64B5F6;
#     }
    
#     .metric-label {
#         font-size: 0.9rem;
#         color: #BDBDBD;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Load the trained model
# @st.cache_resource
# def load_model():
#     try:
#         model_path = "Spiral_DTC.joblib"
#         return joblib.load(model_path)
#     except:
#         st.warning("Model file not found. Using simulation mode.")
#         return None

# # Function to load reference spiral image
# @st.cache_data
# def load_reference_spiral():
#     try:
#         # Try to load the reference spiral from a file
#         reference_img = Image.open("reference_spiral.jpeg")
#         return reference_img
#     except:
#         # If reference file doesn't exist, use the uploaded image as reference
#         return None

# # Function to calculate overlap between two images
# def calculate_overlap(img1, img2):
#     """Calculate how much two binary images overlap."""
#     # Convert both images to grayscale if they're not already
#     if img1.mode != 'L':
#         img1 = img1.convert('L')
#     if img2.mode != 'L':
#         img2 = img2.convert('L')
    
#     # Resize both images to the same dimensions
#     img1 = img1.resize((210, 210))
#     img2 = img2.resize((210, 210))
    
#     # Convert PIL images to numpy arrays
#     arr1 = np.array(img1)
#     arr2 = np.array(img2)
    
#     # Threshold to create binary images
#     _, binary1 = cv2.threshold(arr1, 127, 255, cv2.THRESH_BINARY)
#     _, binary2 = cv2.threshold(arr2, 127, 255, cv2.THRESH_BINARY)
    
#     # Calculate intersection and union
#     intersection = np.logical_and(binary1, binary2).sum()
#     union = np.logical_or(binary1, binary2).sum()
    
#     # Calculate IoU (Intersection over Union)
#     iou = intersection / union if union > 0 else 0
    
#     return iou * 100  # Return as percentage

# # Function to calculate tremor metrics
# def calculate_tremor_metrics(img):
#     """Calculate tremor metrics from the spiral image."""
#     if img.mode != 'L':
#         img = img.convert('L')
    
#     img = img.resize((210, 210))
#     img_array = np.array(img)
    
#     # Edge detection to find the lines
#     edges = cv2.Canny(img_array, 100, 200)
    
#     # Calculate line thickness variation
#     # More variation indicates more tremor
#     thickness_variation = np.std(edges.sum(axis=0) + edges.sum(axis=1))
    
#     # Normalize to a 0-100 scale
#     tremor_score = min(100, max(0, thickness_variation / 50))
    
#     return tremor_score

# # Prediction function
# def predict_parkinson(image_file, loaded_model):
#     try:
#         # Preprocess the image
#         img = Image.open(image_file)
#         img = img.resize((210, 210))
#         img_array = image.img_to_array(img)
#         img_array = img_array.mean()  # Calculate the mean pixel value
#         img_array = np.array(img_array).reshape(1, -1)  # Reshape for prediction
        
#         # Make prediction
#         if loaded_model:
#             prediction = loaded_model.predict(img_array)[0]
            
#             # Interpret the prediction
#             if prediction == 0:
#                 return "Healthy", 0
#             elif prediction == 1:
#                 return "Affected by Parkinson's Disease", 1
#             else:
#                 return "Unknown Prediction", -1
#         else:
#             # Simulation mode
#             # Calculate a tremor score and use it for prediction
#             tremor_score = calculate_tremor_metrics(img)
#             if tremor_score < 50:
#                 return "Healthy", 0
#             else:
#                 return "Affected by Parkinson's Disease", 1
#     except Exception as e:
#         return f"Error during prediction: {e}", -1

# # Main app
# st.title("Spiral Drawing Analysis")

# # Load model
# loaded_model = load_model()

# # Load reference spiral
# reference_spiral = load_reference_spiral()

# # Create tabs for different features
# tab1, tab2 = st.tabs(["Spiral Test", "How It Works"])

# with tab1:
#     st.markdown("""
#     <div class="content-card">
#         <h3>Spiral Drawing Test</h3>
#         <p>This test evaluates hand tremors and motor control by analyzing how well you can draw a spiral. 
#         Draw a spiral on paper, take a photo, and upload it to assess your motor function.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Image upload
#     uploaded_file = st.file_uploader("Upload a spiral drawing image", type=["png", "jpg", "jpeg"])
    
#     if uploaded_file is not None:
#         # Create columns for layout
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Display the uploaded image
#             uploaded_img = Image.open(uploaded_file)
#             st.image(uploaded_img, caption="Uploaded Spiral", use_column_width=True)
        
#         with col2:
#             # Display reference spiral
#             if reference_spiral:
#                 st.image(reference_spiral, caption="Reference Spiral", use_column_width=True)
#             else:
#                 st.info("No reference spiral available. Using uploaded image as reference.")
#                 reference_spiral = uploaded_img
        
#         # Perform prediction
#         result_text, result_code = predict_parkinson(uploaded_file, loaded_model)
        
#         # Calculate overlap with reference image if available
#         overlap_percentage = calculate_overlap(uploaded_img, reference_spiral)
        
#         # Calculate tremor metrics
#         tremor_score = calculate_tremor_metrics(uploaded_img)
        
#         # Display results
#         result_class = "healthy" if result_code == 0 else "parkinsons"
#         st.markdown(f"""
#         <div class="result-card {result_class}">
#             <h3>Analysis Result</h3>
#             <p style="font-size: 1.2rem; font-weight: 500;">Prediction: {result_text}</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Display metrics
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown(f"""
#             <div class="metric-card">
#                 <div class="metric-value">{overlap_percentage:.1f}%</div>
#                 <div class="metric-label">REFERENCE PATTERN MATCH</div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown(f"""
#             <div class="metric-card">
#                 <div class="metric-value">{tremor_score:.1f}%</div>
#                 <div class="metric-label">TREMOR DETECTION</div>
#             </div>
#             """, unsafe_allow_html=True)
        
#         # Explanation of results
#         st.markdown("""
#         <div class="content-card">
#             <h4>What These Results Mean</h4>
#             <p><b>Reference Pattern Match:</b> Measures how closely your spiral matches the ideal reference pattern. Lower values may indicate difficulties in following the pattern.</p>
#             <p><b>Tremor Detection:</b> Quantifies the amount of tremor or shakiness detected in your drawing. Higher values indicate more significant tremor.</p>
#             <p>These metrics, combined with our machine learning model, help assess the likelihood of Parkinson's-related motor symptoms.</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Store results in session state
#         st.session_state["spiral_result"] = result_text
#         st.session_state["spiral_overlap"] = overlap_percentage
#         st.session_state["spiral_tremor"] = tremor_score
        
#         # Save image for report
#         uploaded_file.seek(0)  # Reset file pointer
#         image_bytes = uploaded_file.read()
#         st.session_state["spiral_image_bytes"] = image_bytes
        
#         st.success("✅ Spiral test results saved for your medical report")

# with tab2:
#     st.markdown("""
#     <div class="content-card">
#         <h3>How the Spiral Test Works</h3>
#         <p>The spiral drawing test is a clinical assessment tool used by neurologists to evaluate fine motor control and detect signs of tremor.</p>
        
#         <h4>Scientific Background</h4>
#         <p>Parkinson's disease affects the basal ganglia, which control smooth, coordinated movements. This can manifest as:</p>
#         <ul>
#             <li><b>Resting tremor</b>: Involuntary shaking that occurs when muscles are relaxed</li>
#             <li><b>Action tremor</b>: Tremor that occurs during voluntary movement</li>
#             <li><b>Micrographia</b>: Abnormally small, cramped handwriting</li>
#         </ul>
        
#         <h4>Our Analysis Method</h4>
#         <p>Our system analyzes spiral drawings using several techniques:</p>
#         <ol>
#             <li><b>Pattern Matching</b>: Comparing your drawing to an ideal spiral reference</li>
#             <li><b>Tremor Quantification</b>: Measuring the frequency and amplitude of oscillations</li>
#             <li><b>Line Quality Analysis</b>: Assessing smoothness, pressure, and consistency</li>
#             <li><b>Machine Learning Classification</b>: Using a model trained on thousands of examples</li>
#         </ol>
        
#         <h4>Interpreting Results</h4>
#         <p>This test is one of several assessments used for Parkinson's screening. A single test cannot provide a definitive diagnosis, but combined with other evaluations, it offers valuable insights for healthcare professionals.</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Bottom navigation
# st.markdown("""
# <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
#     <a href="/patientInfo" style="text-decoration: none;">
#         <div style="background-color: #3A3A5A; color: white; padding: 0.5rem 1rem; border-radius: 5px;">
#             ← Patient Info
#         </div>
#     </a>
#     <a href="/wave" style="text-decoration: none;">
#         <div style="background-color: #3A3A5A; color: white; padding: 0.5rem 1rem; border-radius: 5px;">
#             Wave Test →
#         </div>
#     </a>
# </div>
# """, unsafe_allow_html=True)





##  THIS IS WITHOUT ANY CALCULATION JUST UPLOADED IMAGE, REF. IMAGE AND RESULT
import streamlit as st
import joblib
from keras.preprocessing import image
import numpy as np
from PIL import Image
import cv2
from skimage.metrics import structural_similarity as ssim

# Page configuration
st.set_page_config(page_title="Spiral Analysis", page_icon="🌀", layout="wide")

# Hide code with CSS
st.markdown("""
<style>
    .stCodeBlock, pre, code, .CodeMirror, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
        display: none !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background-color: #1E1E2E !important; color: #E0E0E0;}
    h1, h2, h3 {color: #64B5F6; font-weight: 500;}
    .content-card {background-color: #2A2A40; border-radius: 10px; padding: 1.5rem; margin-bottom: 1.5rem;}
    .result-card {padding: 1rem; border-radius: 8px; margin-top: 1rem;}
    .result-card.healthy {background-color: rgba(76, 175, 80, 0.2); border-left: 4px solid #4CAF50;}
    .result-card.parkinsons {background-color: rgba(244, 67, 54, 0.2); border-left: 4px solid #F44336;}
</style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    try:
        # model_path = "Spiral_DTC.joblib"
        model_path = "Spiral_CATBC.joblib"
        return joblib.load(model_path)
    except:
        st.warning("Model file not found. Using simulation mode.")
        return None

# Function to load reference spiral image
@st.cache_data
def load_reference_spiral():
    try:
        return Image.open("reference_spiral.jpeg")
    except:
        return None
    
def calculate_ssim_tremor(user_img: Image.Image, ref_img: Image.Image) -> float:
    # Resize and convert to grayscale
    user_gray = cv2.cvtColor(np.array(user_img.resize((210, 210))), cv2.COLOR_RGB2GRAY)
    ref_gray = cv2.cvtColor(np.array(ref_img.resize((210, 210))), cv2.COLOR_RGB2GRAY)

    # Compute SSIM between user and reference
    score, _ = ssim(user_gray, ref_gray, full=True)

    # Invert SSIM to express as tremor deviation
    tremor_percent = (1 - score) * 100
    return round(tremor_percent, 2), round(score * 100, 2)

# Prediction function
def predict_parkinson(image_file, loaded_model):
    try:
        img = Image.open(image_file)
        img = img.resize((210, 210))
        img_array = image.img_to_array(img)
        img_array = img_array.mean()
        img_array = np.array(img_array).reshape(1, -1)
        if loaded_model:
            prediction = loaded_model.predict(img_array)[0]
            if prediction == 0:
                return "Healthy", 0
            elif prediction == 1:
                return "Affected by Parkinson's Disease", 1
            else:
                return "Unknown Prediction", -1
        else:
            # Simulation mode: random result
            import random
            return ("Healthy", 0) if random.random() < 0.5 else ("Affected by Parkinson's Disease", 1)
    except Exception as e:
        return f"Error during prediction: {e}", -1

# Main app
st.title("Spiral Drawing Analysis")

st.markdown("""
<div class="content-card">
    <h3>Spiral Drawing Test</h3>
    <p>Draw the spiral shown on the right on a blank paper, take a photo, and upload it below. The model will predict if the patient is healthy or affected by Parkinson's Disease.</p>
</div>
""", unsafe_allow_html=True)

# Load model and reference spiral
loaded_model = load_model()
reference_spiral = load_reference_spiral()

# Show reference spiral image for user to see and draw
if reference_spiral:
    st.image(reference_spiral, caption="Reference Spiral (Please copy this)", use_column_width=True)
else:
    st.warning("Reference spiral image not found. Please add 'reference_spiral.jpeg' to the project directory.")

# Image upload
uploaded_file = st.file_uploader("Upload your spiral drawing image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    uploaded_img = Image.open(uploaded_file)
    st.image(uploaded_img, caption="Your Uploaded Spiral", use_column_width=True)

    # Perform prediction
    result_text, result_code = predict_parkinson(uploaded_file, loaded_model)

    # Display results
    result_class = "healthy" if result_code == 0 else "parkinsons"
    st.markdown(f"""
    <div class="result-card {result_class}">
        <h3>Analysis Result</h3>
        <p style="font-size: 1.2rem; font-weight: 500;">Prediction: {result_text}</p>
    </div>
    """, unsafe_allow_html=True)

    if reference_spiral:
        tremor_percent, similarity_score = calculate_ssim_tremor(uploaded_img, reference_spiral)
        st.markdown(f"""
        <div class="result-card">
            <h3>Tremor Analysis (SSIM)</h3>
            <p style="font-size: 1.1rem;">Structural Similarity: <strong>{similarity_score}%</strong></p>
            <p style="font-size: 1.1rem;">Estimated Tremor Deviation: <strong>{tremor_percent}%</strong></p>
        </div>
        """, unsafe_allow_html=True)
        st.session_state["spiral_tremor_percent"] = tremor_percent

    # Store results in session state
    st.session_state["spiral_result"] = result_text
    uploaded_file.seek(0)
    image_bytes = uploaded_file.read()
    st.session_state["spiral_image_bytes"] = image_bytes
    st.success("✅ Spiral test result and image saved for your medical report")
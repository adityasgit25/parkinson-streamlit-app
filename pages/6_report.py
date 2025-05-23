import streamlit as st
from PIL import Image
from io import BytesIO
from fpdf import FPDF
import datetime
import base64
import pandas as pd 

# Feature names (order matters)
FEATURE_NAMES = [
    "QRS_duration", "PR_interval", "QT_interval", "T_interval", "P_interval",
    "QRS", "T", "P", "QRST", "Heart_Rate", "RR_interval", "HRV", "SPO2", "Temperature", "Weight"
]

st.set_page_config(page_title="Final Report", page_icon="📄")


st.title("📄 Parkinson's Disease - Final Report")


# General utility to decode any session image bytes
def get_image_from_session(key):
    if key in st.session_state:
        return Image.open(BytesIO(st.session_state[key]))
    return None

# Utility to decode session image bytes for wave image
def get_wave_image_from_session():
    if "wave_image_bytes" in st.session_state:
        return Image.open(BytesIO(st.session_state["wave_image_bytes"]))
    return None

# Get current date
date_str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# Display Patient Info
st.subheader("👤 Patient Information")
patient_info = {
    "Name": st.session_state.get("patient_name", "N/A"),
    "Age": st.session_state.get("patient_age", "N/A"),
    "Height": st.session_state.get("patient_height", "N/A"),
    "Weight": st.session_state.get("patient_weight", "N/A"),
    "Contact": st.session_state.get("patient_contact", "N/A"),
}

for key, val in patient_info.items():
    st.write(f"**{key}:** {val}")

test_display_mapping = {
    "Spiral": "spiral_result",
    "Wave": "wave_result",
    "Voice": "voice_result",
    "ECG": "ecg_result",
    "Gait (Left Hand)": "gait_chest_result",  # internally still saved as gait_chest_result
    "Gait (Right Hand)": "gait_hand_result",  # internally still saved as gait_hand_result
}

for test, key in test_display_mapping.items():
    result = st.session_state.get(key, "Not Available")
    st.write(f"**{test} Test Result:** {result}")

# Show spiral image if available
spiral_img = get_image_from_session("spiral_image_bytes")
if spiral_img:
    st.subheader("🌀 Spiral Drawing")
    st.image(spiral_img, caption="Uploaded Spiral Drawing", use_column_width=True)

spiral_tremor_percent = st.session_state.get("spiral_tremor_percent")
if spiral_tremor_percent is not None:
    st.write(f"**Spiral Tremor Severity:** {spiral_tremor_percent:.2f}%")
else:
    st.write("**Spiral Tremor Severity:** Not Available")


# Show wave image if available
wave_img = get_wave_image_from_session()
if wave_img:
    st.subheader("🌊 Wave Drawing")
    st.image(wave_img, caption="Uploaded Wave Drawing", use_column_width=True)


# Show left hand gait image if available
left_hand_img = get_image_from_session("left_hand_image_bytes")
if left_hand_img:
    st.subheader("👈 Left Hand Gait Analysis")
    st.image(left_hand_img, caption="Left Hand Gait Image", use_column_width=True)

# Show right hand gait image if available
right_hand_img = get_image_from_session("right_hand_image_bytes")
if right_hand_img:
    st.subheader("👉 Right Hand Gait Analysis")
    st.image(right_hand_img, caption="Right Hand Gait Image", use_column_width=True)

# Show voice features if available
voice_features = st.session_state.get("voice_features")
if isinstance(voice_features, dict) and voice_features:
    st.subheader("Voice Features")
    st.table(pd.DataFrame([voice_features]))
else:
    st.write("Voice features not available.")

# Display ECG Test Result and Input Data
st.subheader("🫀 ECG Test Results")
ecg_result = st.session_state.get("ecg_result", "Not Available")
ecg_data = st.session_state.get("ecg_input_data", "Not Available")

st.write(f"**ECG Test Result:** {ecg_result}")

# If ECG data is available, display all values with parameter names
if isinstance(ecg_data, dict):
    st.write("**ECG Data:**")
    for key, value in ecg_data.items():
        st.write(f"{key}: {value}")
else:
    st.write("**ECG Data:** Not Available")

# Show ECG images if available
ecg_img1 = get_image_from_session("ecg_image1_bytes")
ecg_img2 = get_image_from_session("ecg_image2_bytes")
if ecg_img1 or ecg_img2:
    st.subheader("ECG Images")
    col1, col2 = st.columns(2)
    with col1:
        if ecg_img1:
            st.image(ecg_img1, caption="ECG Image 1", use_column_width=True)
    with col2:
        if ecg_img2:
            st.image(ecg_img2, caption="ECG Image 2", use_column_width=True)

# st.subheader("🏃 Gait Test Details")

# if st.session_state.get("gait_chest_data") is not None:
#     st.markdown("**Left Hand Gait Sensor Data:**")
#     for i, value in enumerate(st.session_state["gait_chest_data"][0]):
#         st.write(f"Feature {i+1}: {value}")
# else:
#     st.warning("Left hand gait data is not available yet.")

# if st.session_state.get("gait_hand_data") is not None:
#     st.markdown("**Right Hand Gait Sensor Data:**")
#     for i, value in enumerate(st.session_state["gait_hand_data"][0]):
#         st.write(f"Feature {i+1}: {value}")
# else:
#     st.warning("Right hand gait data is not available yet.")

# --- PDF Generation ---
st.subheader("📥 Export Report as PDF")

# def generate_pdf():
#     pdf = FPDF()
#     pdf.add_page()

#      # Add BMSIT&M Logo at top-left corner (adjust path and size as needed)
#     logo_path = "bmsit_logo.png"  # <-- Make sure this path is correct and image is available
#     pdf.image(logo_path, x=10, y=8, w=30)

#     # Heading next to logo
#     pdf.set_font("Arial", 'B', 14)
#     pdf.set_xy(45, 10)
#     pdf.multi_cell(0, 10, "FYP2025 | INITIATIVE BY STUDENTS OF BMSIT&M", align='L')
    
#     # Title centered below
#     pdf.ln(20)
#     pdf.set_font("Arial", 'B', 16)
#     pdf.cell(0, 10, "Parkinson's Disease Prediction Report", ln=True, align='C')
#     pdf.ln(10)

#     pdf.set_font("Arial", size=12)


#     # Patient Info
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Patient Information", ln=True)
#     pdf.set_font("Arial", size=12)
#     for key, val in patient_info.items():
#         pdf.cell(0, 10, f"{key}: {val}", ln=True)
#     pdf.ln(5)

#     # Test Results
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Test Results", ln=True)
#     pdf.set_font("Arial", size=12)
#     for test, key in test_display_mapping.items():
#         result = st.session_state.get(key, "Not Available")
#         pdf.cell(0, 10, f"{test} Test: {result}", ln=True)
    
#     # Spiral Drawing Details
#     spiral_tremor_percent = st.session_state.get("spiral_tremor_percent")
#     if spiral_tremor_percent is not None:
#         pdf.set_font("Arial", 'B', 14)
#         pdf.cell(0, 10, "Spiral Drawing Details", ln=True)
#         pdf.set_font("Arial", size=12)
#         pdf.cell(0, 10, f"Spiral Tremor Severity: {spiral_tremor_percent:.2f}%", ln=True)

#         # Voice Test Results
#     voice_result = st.session_state.get("voice_result", "Not Available")
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Voice Test Results", ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, f"Voice Test Result: {voice_result}", ln=True)

#     # Voice Features Table
#     voice_features = st.session_state.get("voice_features")
#     if isinstance(voice_features, dict) and voice_features:
#         pdf.cell(0, 10, "Voice Features:", ln=True)
#         for key, value in voice_features.items():
#             pdf.cell(0, 10, f"{key}: {value}", ln=True)
#     else:
#         pdf.cell(0, 10, "Voice features not available.", ln=True)
#     pdf.ln(5)

#      # ECG Test Results
#     ecg_result = st.session_state.get("ecg_result", "Not Available")
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "ECG Test Results", ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, f"ECG Test Result: {ecg_result}", ln=True)

#     # ECG Images
#     if ecg_img1:
#         pdf.ln(5)
#         img_path = "ecg_img1_temp.jpg"
#         ecg_img1.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)
#     if ecg_img2:
#         pdf.ln(5)
#         img_path = "ecg_img2_temp.jpg"
#         ecg_img2.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     # Include all ECG input values in the report
#     ecg_data = st.session_state.get("ecg_input_data", "Not Available")
#     if isinstance(ecg_data, dict):
#         for key, value in ecg_data.items():
#             pdf.cell(0, 10, f"{key}: {value}", ln=True)
#     else:
#         pdf.cell(0, 10, "ECG Data: Not Available", ln=True)
#     pdf.ln(5)

#     # Add predictions if available
    

#     # Gait Detailed Data
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Gait Test Details", ln=True)
#     pdf.set_font("Arial", size=12)

#     left_result = st.session_state.get("gait_chest_result", "Not Available")
#     right_result = st.session_state.get("gait_hand_result", "Not Available")

#     pdf.cell(0, 10, f"Left Hand Gait Prediction: {left_result}", ln=True)
#     pdf.cell(0, 10, f"Right Hand Gait Prediction: {right_result}", ln=True)
#     pdf.ln(5)

#     # chest_data = st.session_state.get("gait_chest_data")
#     # if chest_data is not None:
#     #     pdf.cell(0, 10, "Left Hand Gait Sensor Data:", ln=True)
#     #     for i, val in enumerate(chest_data):
#     #         pdf.cell(0, 10, f"  Feature {i+1}: {val}", ln=True)

#     # hand_data = st.session_state.get("gait_hand_data")
#     # if hand_data is not None:
#     #     pdf.cell(0, 10, "Right Hand Gait Sensor Data:", ln=True)
#     #     for i, val in enumerate(hand_data):
#     #         pdf.cell(0, 10, f"  Feature {i+1}: {val}", ln=True)


#     # Date
#     pdf.set_font("Arial", 'I', 10)
#     pdf.cell(0, 10, f"Generated on: {date_str}", ln=True)

#     # Spiral image
#     if spiral_img:
#         pdf.ln(5)
#         img_path = "spiral_temp.jpg"
#         spiral_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     # Wave image for PDF
#     if wave_img:
#         pdf.ln(5)
#         img_path = "wave_temp.jpg"
#         wave_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)
    
#      # Add left hand gait image if available
#     if left_hand_img:
#         pdf.ln(5)
#         img_path = "left_hand_temp.jpg"
#         left_hand_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     # Add right hand gait image if available
#     if right_hand_img:
#         pdf.ln(5)
#         img_path = "right_hand_temp.jpg"
#         right_hand_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)
    
#     # Doctor Contact Details
#     pdf.ln(10)
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Doctor Contact - Details", ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, "Dr. Rakesh Kumar N, BAMS, MD(Dravyaguna)", ln=True)
#     pdf.cell(0, 10, "Phone: +91-9611206680", ln=True)

#     # Thank You Message
#     pdf.ln(10)
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, "Thank You! We Help to Heal", ln=True, align='C')

#     # return pdf.output(dest="S").encode("latin1")
#     return pdf.output(dest="S").encode("latin-1", errors="replace")


# def generate_pdf():
#     def safe_text(text):
#         return str(text).encode("latin-1", errors="replace").decode("latin-1")

#     pdf = FPDF()
#     pdf.add_page()

#     # Add BMSIT&M Logo
#     logo_path = "bmsit_logo.png"
#     pdf.image(logo_path, x=10, y=8, w=30)

#     # Header
#     pdf.set_font("Arial", 'B', 14)
#     pdf.set_xy(45, 10)
#     pdf.multi_cell(0, 10, safe_text("FYP2025 | INITIATIVE BY STUDENTS OF BMSIT&M"), align='L')
    
#     pdf.ln(20)
#     pdf.set_font("Arial", 'B', 16)
#     pdf.cell(0, 10, safe_text("Parkinson's Disease Prediction Report"), ln=True, align='C')
#     pdf.ln(10)

#     pdf.set_font("Arial", size=12)

#     # Patient Info
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Patient Information"), ln=True)
#     pdf.set_font("Arial", size=12)
#     for key, val in patient_info.items():
#         pdf.cell(0, 10, safe_text(f"{key}: {val}"), ln=True)
#     pdf.ln(5)

#     # Test Results
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Test Results"), ln=True)
#     pdf.set_font("Arial", size=12)
#     for test, key in test_display_mapping.items():
#         result = st.session_state.get(key, "Not Available")
#         pdf.cell(0, 10, safe_text(f"{test} Test: {result}"), ln=True)

#     # Spiral Drawing
#     spiral_tremor_percent = st.session_state.get("spiral_tremor_percent")
#     if spiral_tremor_percent is not None:
#         pdf.set_font("Arial", 'B', 14)
#         pdf.cell(0, 10, safe_text("Spiral Drawing Details"), ln=True)
#         pdf.set_font("Arial", size=12)
#         pdf.cell(0, 10, safe_text(f"Spiral Tremor Severity: {spiral_tremor_percent:.2f}%"), ln=True)

#     # Voice
#     voice_result = st.session_state.get("voice_result", "Not Available")
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Voice Test Results"), ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, safe_text(f"Voice Test Result: {voice_result}"), ln=True)

#     voice_features = st.session_state.get("voice_features")
#     if isinstance(voice_features, dict) and voice_features:
#         pdf.cell(0, 10, safe_text("Voice Features:"), ln=True)
#         for key, value in voice_features.items():
#             pdf.cell(0, 10, safe_text(f"{key}: {value}"), ln=True)
#     else:
#         pdf.cell(0, 10, safe_text("Voice features not available."), ln=True)
#     pdf.ln(5)

#     # ECG
#     ecg_result = st.session_state.get("ecg_result", "Not Available")
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("ECG Test Results"), ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, safe_text(f"ECG Test Result: {ecg_result}"), ln=True)

#     if ecg_img1:
#         pdf.ln(5)
#         img_path = "ecg_img1_temp.jpg"
#         ecg_img1.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)
#     if ecg_img2:
#         pdf.ln(5)
#         img_path = "ecg_img2_temp.jpg"
#         ecg_img2.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     ecg_data = st.session_state.get("ecg_input_data", "Not Available")
#     if isinstance(ecg_data, dict):
#         for key, value in ecg_data.items():
#             pdf.cell(0, 10, safe_text(f"{key}: {value}"), ln=True)
#     else:
#         pdf.cell(0, 10, safe_text("ECG Data: Not Available"), ln=True)
#     pdf.ln(5)

#     # Gait
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Gait Test Details"), ln=True)
#     pdf.set_font("Arial", size=12)
#     left_result = st.session_state.get("gait_chest_result", "Not Available")
#     right_result = st.session_state.get("gait_hand_result", "Not Available")
#     pdf.cell(0, 10, safe_text(f"Left Hand Gait Prediction: {left_result}"), ln=True)
#     pdf.cell(0, 10, safe_text(f"Right Hand Gait Prediction: {right_result}"), ln=True)
#     pdf.ln(5)

#     pdf.set_font("Arial", 'I', 10)
#     pdf.cell(0, 10, safe_text(f"Generated on: {date_str}"), ln=True)

#     # Spiral Image
#     if spiral_img:
#         pdf.ln(5)
#         img_path = "spiral_temp.jpg"
#         spiral_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     if wave_img:
#         pdf.ln(5)
#         img_path = "wave_temp.jpg"
#         wave_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     if left_hand_img:
#         pdf.ln(5)
#         img_path = "left_hand_temp.jpg"
#         left_hand_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     if right_hand_img:
#         pdf.ln(5)
#         img_path = "right_hand_temp.jpg"
#         right_hand_img.convert("RGB").save(img_path)
#         pdf.image(img_path, w=100)

#     # Doctor Info
#     pdf.ln(10)
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Doctor Contact - Details"), ln=True)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(0, 10, safe_text("Dr. Rakesh Kumar N, BAMS, MD(Dravyaguna)"), ln=True)
#     pdf.cell(0, 10, safe_text("Phone: +91-9611206680"), ln=True)

#     pdf.ln(10)
#     pdf.set_font("Arial", 'B', 14)
#     pdf.cell(0, 10, safe_text("Thank You! We Help to Heal"), ln=True, align='C')

#     return pdf.output(dest="S").encode("latin-1", errors="replace")


# This looks more professional, switch to previous version if it breaks
def generate_pdf():
    def safe_text(text):
        """Ensure text is compatible with PDF encoding"""
        return str(text).encode("latin-1", errors="replace").decode("latin-1")
    
    # Initialize PDF with standard A4 format
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # Set document properties
    pdf.set_title("Parkinson's Disease Assessment Report")
    pdf.set_author("BMSIT&M FYP2025 Team")
    pdf.set_creator("BMSIT&M Parkinson's Disease Assessment System")
    
    # Add header with logo
    logo_path = "bmsit_logo.png"
    pdf.image(logo_path, x=10, y=8, w=25)
    
    # Institution header
    pdf.set_font("Arial", 'B', 12)
    pdf.set_xy(40, 10)
    pdf.cell(0, 6, safe_text("BMS Institute of Technology and Management"), 0, 1, 'L')
    pdf.set_xy(40, 16)
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 6, safe_text("FYP2025 | Student Research Initiative"), 0, 1, 'L')
    
    # Add horizontal separator
    pdf.line(10, 25, 200, 25)
    
    # Report title
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, safe_text("Parkinson's Disease Assessment Report"), 0, 1, 'C')
    pdf.ln(5)
    
    # Patient information section
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("Patient Information"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    for key, val in patient_info.items():
        pdf.cell(40, 8, safe_text(f"{key}:"), 0, 0)
        pdf.cell(0, 8, safe_text(f"{val}"), 0, 1)
    pdf.ln(5)
    
    # Test results section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("Assessment Results"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    for test, key in test_display_mapping.items():
        result = st.session_state.get(key, "Not Available")
        pdf.cell(60, 8, safe_text(f"{test} Test:"), 0, 0)
        pdf.cell(0, 8, safe_text(f"{result}"), 0, 1)
    pdf.ln(5)
    
    # Spiral drawing analysis
    spiral_tremor_percent = st.session_state.get("spiral_tremor_percent")
    if spiral_tremor_percent is not None:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, safe_text("Spiral Drawing Analysis"), 0, 1, 'L', True)
        pdf.ln(2)
        
        pdf.set_font("Arial", '', 10)
        pdf.cell(60, 8, safe_text("Tremor Severity:"), 0, 0)
        pdf.cell(0, 8, safe_text(f"{spiral_tremor_percent:.2f}%"), 0, 1)
        
        # Add spiral image if available
        if spiral_img:
            pdf.ln(3)
            img_path = "spiral_temp.jpg"
            spiral_img.convert("RGB").save(img_path)
            pdf.cell(60, 8, safe_text("Spiral Drawing Sample:"), 0, 1)
            pdf.image(img_path, x=15, w=80)
            
        if wave_img:
            pdf.ln(3)
            img_path = "wave_temp.jpg"
            wave_img.convert("RGB").save(img_path)
            pdf.cell(60, 8, safe_text("Wave Drawing Sample:"), 0, 1)
            pdf.image(img_path, x=15, w=80)
        pdf.ln(5)
    
    # Voice analysis section
    voice_result = st.session_state.get("voice_result", "Not Available")
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("Voice Analysis"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    pdf.cell(60, 8, safe_text("Voice Assessment Result:"), 0, 0)
    pdf.cell(0, 8, safe_text(f"{voice_result}"), 0, 1)
    
    voice_features = st.session_state.get("voice_features")
    if isinstance(voice_features, dict) and voice_features:
        pdf.ln(2)
        pdf.cell(0, 8, safe_text("Voice Acoustic Features:"), 0, 1)
        
        # Create a table for voice features
        for key, value in voice_features.items():
            pdf.cell(80, 6, safe_text(f"{key}"), 'L', 0)
            pdf.cell(0, 6, safe_text(f"{value}"), 'R', 1)
    pdf.ln(5)
    
    # ECG analysis section
    ecg_result = st.session_state.get("ecg_result", "Not Available")
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("ECG Analysis"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    pdf.cell(60, 8, safe_text("ECG Assessment Result:"), 0, 0)
    pdf.cell(0, 8, safe_text(f"{ecg_result}"), 0, 1)
    
    # ECG data parameters
    ecg_data = st.session_state.get("ecg_input_data", "Not Available")
    if isinstance(ecg_data, dict):
        pdf.ln(2)
        pdf.cell(0, 8, safe_text("ECG Parameters:"), 0, 1)
        for key, value in ecg_data.items():
            pdf.cell(80, 6, safe_text(f"{key}"), 'L', 0)
            pdf.cell(0, 6, safe_text(f"{value}"), 'R', 1)
    
    # ECG images
    if ecg_img1:
        pdf.ln(3)
        img_path = "ecg_img1_temp.jpg"
        ecg_img1.convert("RGB").save(img_path)
        pdf.cell(60, 8, safe_text("ECG Visualization 1:"), 0, 1)
        pdf.image(img_path, x=15, w=100)
        
    if ecg_img2:
        pdf.ln(3)
        img_path = "ecg_img2_temp.jpg"
        ecg_img2.convert("RGB").save(img_path)
        pdf.cell(60, 8, safe_text("ECG Visualization 2:"), 0, 1)
        pdf.image(img_path, x=15, w=100)
    pdf.ln(5)
    
    # Gait analysis section
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("Gait Analysis"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    left_result = st.session_state.get("gait_chest_result", "Not Available")
    right_result = st.session_state.get("gait_hand_result", "Not Available")
    pdf.cell(60, 8, safe_text("Left Hand Gait Assessment:"), 0, 0)
    pdf.cell(0, 8, safe_text(f"{left_result}"), 0, 1)
    pdf.cell(60, 8, safe_text("Right Hand Gait Assessment:"), 0, 0)
    pdf.cell(0, 8, safe_text(f"{right_result}"), 0, 1)
    
    # Gait images
    if left_hand_img:
        pdf.ln(3)
        img_path = "left_hand_temp.jpg"
        left_hand_img.convert("RGB").save(img_path)
        pdf.cell(60, 8, safe_text("Left Hand Movement Sample:"), 0, 1)
        pdf.image(img_path, x=15, w=80)
        
    if right_hand_img:
        pdf.ln(3)
        img_path = "right_hand_temp.jpg"
        right_hand_img.convert("RGB").save(img_path)
        pdf.cell(60, 8, safe_text("Right Hand Movement Sample:"), 0, 1)
        pdf.image(img_path, x=15, w=80)
    pdf.ln(10)
    
    # Add footer with doctor contact details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("Medical Professional Contact"), 0, 1, 'L', True)
    pdf.ln(2)
    
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 6, safe_text("Dr. Rakesh Kumar N, BAMS, MD(Dravyaguna)"), 0, 1)
    pdf.cell(0, 6, safe_text("Phone: +91-9611206680"), 0, 1)
    
    # Generation date
    pdf.ln(10)
    pdf.set_font("Arial", 'I', 8)
    pdf.cell(0, 6, safe_text(f"Report generated on: {date_str}"), 0, 1)
    
    # Disclaimer
    pdf.ln(5)
    pdf.set_font("Arial", 'I', 8)
    pdf.multi_cell(0, 4, safe_text("Disclaimer: This assessment is provided for informational purposes only and does not constitute a medical diagnosis. Please consult with a qualified healthcare professional for proper diagnosis and treatment."), 0, 'L')
    
    # Final message
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, safe_text("BMSIT&M - We Help to Heal"), 0, 1, 'C')
    
    return pdf.output(dest="S").encode("latin-1", errors="replace")

# Download button
pdf_bytes = generate_pdf()
b64 = base64.b64encode(pdf_bytes).decode()
href = f'<a href="data:application/pdf;base64,{b64}" download="parkinson_report.pdf">📄 Download Report as PDF</a>'
st.markdown(href, unsafe_allow_html=True)




import streamlit as st
from PIL import Image
from io import BytesIO
from fpdf import FPDF
import datetime
import base64

# Feature names (order matters)
FEATURE_NAMES = [
    "QRS_duration", "PR_interval", "QT_interval", "T_interval", "P_interval",
    "QRS", "T", "P", "QRST", "Heart_Rate", "RR_interval", "HRV", "SPO2", "Temperature", "Weight"
]

st.set_page_config(page_title="Final Report", page_icon="📄")


st.title("📄 Parkinson's Disease - Final Report")

# Utility to decode session image bytes
def get_image_from_session():
    if "spiral_image_bytes" in st.session_state:
        return Image.open(BytesIO(st.session_state["spiral_image_bytes"]))
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

# Display Test Results
st.subheader("🧪 Test Results Summary")
test_names = ["Spiral", "Wave", "Voice", "ECG", "Gait (Chest)", "Gait (Hand)"]
for test in test_names:
    key = test.lower().replace(" ", "_").replace("(", "").replace(")", "") + "_result"
    result = st.session_state.get(key, "Not Available")
    st.write(f"**{test} Test Result:** {result}")

# Show spiral image if available
spiral_img = get_image_from_session()
if spiral_img:
    st.subheader("🌀 Spiral Drawing")
    st.image(spiral_img, caption="Uploaded Spiral Drawing", use_column_width=True)

# Show wave image if available
wave_img = get_wave_image_from_session()
if wave_img:
    st.subheader("🌊 Wave Drawing")
    st.image(wave_img, caption="Uploaded Wave Drawing", use_column_width=True)

# Display ECG Test Result and Input Data
st.subheader("🫀 ECG Test Results")
ecg_result = st.session_state.get("ecg_result", "Not Available")
ecg_data = st.session_state.get("ecg_input_data", "Not Available")

# Display the result
# st.write(f"**ECG Test Result:** {ecg_result}")

# If ECG data is available, display the 15 values clearly
if ecg_data != "Not Available":
    st.write("**ECG Data:**")
    for i, value in enumerate(ecg_data[:15]):
        st.write(f"{FEATURE_NAMES[i]}: {value}")
else:
    st.write("**ECG Data:** Not Available")

st.subheader("🏃 Gait Test Details")

if "gait_chest_data" in st.session_state:
    st.markdown("**Chest Sensor Data:**")
    for i, value in enumerate(st.session_state["gait_chest_data"]):
        st.write(f"Feature {i+1}: {value}")

if "gait_hand_data" in st.session_state:
    st.markdown("**Hand Sensor Data:**")
    for i, value in enumerate(st.session_state["gait_hand_data"]):
        st.write(f"Feature {i+1}: {value}")

# --- PDF Generation ---
st.subheader("📥 Export Report as PDF")

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Parkinson's Disease Prediction Report", ln=True, align='C')
    pdf.ln(10)

    # Patient Info
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Patient Information", ln=True)
    pdf.set_font("Arial", size=12)
    for key, val in patient_info.items():
        pdf.cell(0, 10, f"{key}: {val}", ln=True)
    pdf.ln(5)

    # Test Results
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Test Results", ln=True)
    pdf.set_font("Arial", size=12)
    for test in test_names:
        result = st.session_state.get(f"{test.lower()}_result", "Not Available")
        pdf.cell(0, 10, f"{test} Test: {result}", ln=True)
    pdf.ln(5)

     # ECG Test Results
    ecg_result = st.session_state.get("ecg_result", "Not Available")
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "ECG Test Results", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"ECG Test Result: {ecg_result}", ln=True)

    # Include 15 ECG input values in the report
    ecg_data = st.session_state.get("ecg_data", "Not Available")
    if ecg_data != "Not Available":
        for i, value in enumerate(ecg_data[:15]):
            pdf.cell(0, 10, f"{FEATURE_NAMES[i]}: {value}", ln=True)
    else:
        pdf.cell(0, 10, "ECG Data: Not Available", ln=True)
    pdf.ln(5)

    # Gait Detailed Data
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Gait Test Details", ln=True)
    pdf.set_font("Arial", size=12)

    chest_data = st.session_state.get("gait_chest_data")
    if chest_data is not None:
        pdf.cell(0, 10, "Chest Sensor Data:", ln=True)
        for i, val in enumerate(chest_data):
            pdf.cell(0, 10, f"  Feature {i+1}: {val}", ln=True)

    hand_data = st.session_state.get("gait_hand_data")
    if hand_data is not None:
        pdf.cell(0, 10, "Hand Sensor Data:", ln=True)
        for i, val in enumerate(hand_data):
            pdf.cell(0, 10, f"  Feature {i+1}: {val}", ln=True)


    # Date
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 10, f"Generated on: {date_str}", ln=True)

    # Spiral image
    if spiral_img:
        pdf.ln(5)
        img_path = "spiral_temp.jpg"
        spiral_img.save(img_path)
        pdf.image(img_path, w=100)

    # Wave image for PDF
    if wave_img:
        pdf.ln(5)
        img_path = "wave_temp.jpg"
        wave_img.save(img_path)
        pdf.image(img_path, w=100)

    return pdf.output(dest="S").encode("latin1")

# Download button
pdf_bytes = generate_pdf()
b64 = base64.b64encode(pdf_bytes).decode()
href = f'<a href="data:application/pdf;base64,{b64}" download="parkinson_report.pdf">📄 Download Report as PDF</a>'
st.markdown(href, unsafe_allow_html=True)

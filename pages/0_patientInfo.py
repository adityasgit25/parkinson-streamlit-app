import streamlit as st

st.title("📝 Enter Patient Information")

# Input form
with st.form("patient_info_form"):
    name = st.text_input("Patient Name", max_chars=50)
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    height = st.number_input("Height (in cm)", min_value=30.0, max_value=250.0, step=0.1, format="%.1f")
    weight = st.number_input("Weight (in kg)", min_value=2.0, max_value=300.0, step=0.1, format="%.1f")
    contact = st.text_input("Contact Number", max_chars=15)

    submitted = st.form_submit_button("Save Patient Info")

if submitted:
    # Save in session_state
    st.session_state["patient_name"] = name
    st.session_state["patient_age"] = age
    st.session_state["patient_height"] = height
    st.session_state["patient_weight"] = weight
    st.session_state["patient_contact"] = contact

    st.success("✅ Patient information saved successfully!")

# Show existing info if already saved
if "patient_name" in st.session_state:
    st.markdown("---")
    st.subheader("Saved Information:")
    st.write(f"**Name:** {st.session_state['patient_name']}")
    st.write(f"**Age:** {st.session_state['patient_age']}")
    st.write(f"**Height:** {st.session_state['patient_height']} cm")
    st.write(f"**Weight:** {st.session_state['patient_weight']} kg")
    st.write(f"**Contact:** {st.session_state['patient_contact']}")

import streamlit as st

st.set_page_config(page_title="Parkinson's Detection App", page_icon="🧠")

st.title("Welcome to Parkinson's Detection App")
st.write("Select a test from the sidebar to proceed.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Spiral Test 🌀", "Wave Test 🌊", "Voice Test 🎤"])

if page == "Spiral Test 🌀":
    st.switch_page("pages/1_spiral")
elif page == "Wave Test 🌊":
    st.switch_page("pages/2_wave")
elif page == "Voice Test 🎤":
    st.switch_page("pages/3_voice")

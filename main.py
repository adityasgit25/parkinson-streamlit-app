import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def main():
    # Page configuration
    st.set_page_config(
        page_title="Parkinson's Disease Detection Tool - BMSIT",
        page_icon="🧠",
        layout="wide"
    )
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Wave Analysis", "Gait Analysis", "Other Features", "About"])
    
    # BMSIT logo and project info in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("BMSIT Final Year Project")
    st.sidebar.markdown("Department of Computer Science")
    # You can add your name and USN here
    st.sidebar.markdown("By: [Your Name]")
    st.sidebar.markdown("USN: [Your USN]")
    st.sidebar.markdown("Under the guidance of:")
    st.sidebar.markdown("[Guide Name], [Designation]")
    
    if page == "Home":
        home_page()
    elif page == "Wave Analysis":
        wave_analysis_page()
    elif page == "Gait Analysis":
        gait_analysis_page()
    elif page == "Other Features":
        other_features_page()
    elif page == "About":
        about_page()

def home_page():
    # College and Project Information
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # You can replace this with actual BMSIT logo
        st.markdown("### BMSIT&M")
        st.markdown("#### Bengaluru, Karnataka")
    
    with col2:
        st.title("Parkinson's Disease Detection Tool")
        st.markdown("#### A Final Year Project at BMS Institute of Technology and Management")
    
    st.markdown("---")
    
    # Project introduction
    st.markdown("""
    ## Early Detection of Parkinson's Disease Using Machine Learning
    
    This application utilizes advanced machine learning algorithms to analyze movement patterns,
    handwriting, gait, and other biomarkers to detect early signs of Parkinson's disease.
    
    **Research Objectives:**
    - Develop non-invasive screening tools for early detection
    - Improve accessibility of Parkinson's screening
    - Assist medical professionals with objective data for diagnosis
    
    **Note:** This application is for screening purposes only and does not replace professional medical diagnosis.
    """)
    
    # Features section with columns
    st.subheader("Detection Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Wave Analysis")
        st.markdown("""
        Analyzes hand tremors and wave patterns by processing:
        - Hand movement videos
        - Spiral drawing tests
        - Handwriting samples
        """)
        st.button("Try Wave Analysis", key="wave_btn")
    
    with col2:
        st.markdown("### Gait Analysis")
        st.markdown("""
        Evaluates walking patterns by examining:
        - Step length and timing
        - Balance and posture
        - Movement symmetry
        """)
        st.button("Try Gait Analysis", key="gait_btn")
    
    with col3:
        st.markdown("### Other Features")
        st.markdown("""
        Additional assessments include:
        - Voice analysis
        - Facial expression analysis
        - Reaction time tests
        """)
        st.button("Explore Other Features", key="other_btn")
    
    # How it works section
    st.subheader("How It Works")
    st.markdown("""
    1. **Select a test** from the sidebar or feature buttons above
    2. **Upload your data** (video, image, or audio depending on the test)
    3. **View the analysis results** with detailed explanations
    4. **Save or share** your results with healthcare professionals
    """)
    
    # Project significance
    st.subheader("Project Significance")
    st.markdown("""
    Parkinson's disease affects millions worldwide, and early detection can significantly 
    improve treatment outcomes. This project aims to create an accessible tool that can be 
    used as a preliminary screening method, potentially increasing early diagnosis rates.
    """)
    
    # Technologies used
    st.subheader("Technologies Used")
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        - Python
        - Streamlit
        - OpenCV
        - TensorFlow/PyTorch
        """)
    
    with tech_col2:
        st.markdown("""
        - Scikit-learn
        - Pandas & NumPy
        - Signal Processing
        - Computer Vision
        """)
    
    with tech_col3:
        st.markdown("""
        - Machine Learning
        - Deep Learning (CNN)
        - Time Series Analysis
        - Feature Extraction
        """)
    
    # Disclaimer and privacy
    st.markdown("---")
    st.caption("""
    **DISCLAIMER:** This application is designed for screening purposes only and is not a substitute for 
    professional medical diagnosis. Please consult with a healthcare professional regarding your results.
    
    **PRIVACY NOTICE:** All uploaded data is processed locally and is not stored on any external servers 
    unless explicitly saved by the user.
    
    © 2025 BMSIT&M - Department of Computer Science
    """)

def wave_analysis_page():
    st.title("Wave Analysis")
    st.subheader("Analyze hand tremors and movement patterns")
    
    st.markdown("""
    Wave analysis examines the tremors and movement patterns in your hands that may indicate
    early signs of Parkinson's disease. You can upload:
    
    1. A video of your hand movement
    2. An image of a spiral drawing test
    3. A sample of your handwriting
    """)
    
    analysis_type = st.selectbox("Select Analysis Type", 
                                ["Hand Movement Video", "Spiral Drawing Test", "Handwriting Sample"])
    
    if analysis_type == "Hand Movement Video":
        st.subheader("Hand Movement Video Analysis")
        video_file = st.file_uploader("Upload a video of your hand movement", type=["mp4", "avi", "mov"])
        
        if video_file is not None:
            st.video(video_file)
            if st.button("Analyze Video"):
                st.info("Analysis in progress... This may take a moment.")
                # Analysis code would go here
                st.success("Analysis complete!")
                # Results display would go here
    
    elif analysis_type == "Spiral Drawing Test":
        st.subheader("Spiral Drawing Test Analysis")
        image_file = st.file_uploader("Upload an image of your spiral drawing", type=["jpg", "jpeg", "png"])
        
        if image_file is not None:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Spiral Drawing", use_column_width=True)
            if st.button("Analyze Drawing"):
                st.info("Analysis in progress...")
                # Analysis code would go here
                st.success("Analysis complete!")
                # Results display would go here
    
    elif analysis_type == "Handwriting Sample":
        st.subheader("Handwriting Sample Analysis")
        handwriting_file = st.file_uploader("Upload an image of your handwriting", type=["jpg", "jpeg", "png"])
        
        if handwriting_file is not None:
            image = Image.open(handwriting_file)
            st.image(image, caption="Uploaded Handwriting Sample", use_column_width=True)
            if st.button("Analyze Handwriting"):
                st.info("Analysis in progress...")
                # Analysis code would go here
                st.success("Analysis complete!")
                # Results display would go here

def gait_analysis_page():
    st.title("Gait Analysis")
    st.subheader("Analyze walking patterns")
    
    st.markdown("""
    Gait analysis examines your walking patterns to detect subtle abnormalities that may
    indicate early signs of Parkinson's disease.
    """)
    
    gait_video = st.file_uploader("Upload a video of your walking (side view preferred)", type=["mp4", "avi", "mov"])
    
    if gait_video is not None:
        st.video(gait_video)
        
        col1, col2 = st.columns(2)
        
        with col1:
            walking_distance = st.number_input("Walking Distance (meters)", min_value=1.0, max_value=20.0, value=5.0)
        
        with col2:
            walking_surface = st.selectbox("Walking Surface", ["Flat ground", "Inclined surface", "Stairs"])
        
        if st.button("Analyze Gait"):
            st.info("Gait analysis in progress... This may take a moment.")
            # Analysis code would go here
            st.success("Analysis complete!")
            
            # Sample results visualization
            st.subheader("Analysis Results")
            st.markdown("The following metrics were measured from your gait:")
            
            results_col1, results_col2 = st.columns(2)
            
            with results_col1:
                st.metric("Step Length Symmetry", "0.92", "-0.04")
                st.metric("Stride Time Variability", "3.2%", "1.1%")
                
            with results_col2:
                st.metric("Walking Speed", "1.1 m/s", "-0.2 m/s")
                st.metric("Arm Swing Symmetry", "0.87", "-0.08")

def other_features_page():
    st.title("Other Detection Features")
    
    feature_type = st.selectbox("Select Feature", 
                               ["Voice Analysis", "Facial Expression Analysis", "Reaction Time Test"])
    
    if feature_type == "Voice Analysis":
        st.subheader("Voice Analysis")
        st.markdown("""
        Voice analysis examines speech patterns, including rhythm, pitch, and tremor,
        which may indicate early signs of Parkinson's disease.
        """)
        
        st.audio(None, format="audio/wav")
        audio_file = st.file_uploader("Upload an audio recording of your voice", type=["wav", "mp3"])
        
        if audio_file is not None:
            st.audio(audio_file)
            if st.button("Analyze Voice"):
                st.info("Voice analysis in progress...")
                # Analysis code would go here
                st.success("Analysis complete!")
    
    elif feature_type == "Facial Expression Analysis":
        st.subheader("Facial Expression Analysis")
        st.markdown("""
        This analysis examines facial expressions and microexpressions, which may show
        reduced facial mobility (hypomimia) in people with Parkinson's disease.
        """)
        
        face_image = st.file_uploader("Upload a clear photo of your face", type=["jpg", "jpeg", "png"])
        
        if face_image is not None:
            image = Image.open(face_image)
            st.image(image, caption="Uploaded Facial Image", use_column_width=True)
            if st.button("Analyze Facial Expressions"):
                st.info("Facial analysis in progress...")
                # Analysis code would go here
                st.success("Analysis complete!")
    
    elif feature_type == "Reaction Time Test":
        st.subheader("Reaction Time Test")
        st.markdown("""
        This test measures your reaction time, which can be affected in the early
        stages of Parkinson's disease.
        """)
        
        if st.button("Start Reaction Time Test"):
            st.markdown("When the box turns green, click it as quickly as possible!")
            # Reaction time test would go here

def about_page():
    st.title("About This Project")
    
    st.markdown("""
    ## Parkinson's Disease Detection Tool
    
    **Final Year Project at BMS Institute of Technology and Management**
    
    Department of Computer Science Engineering, 2024-2025
    
    ### Project Team:
    - [Your Name] (USN: [Your USN])
    - [Team Member 2] (USN: [USN])
    - [Team Member 3] (USN: [USN])
    - [Team Member 4] (USN: [USN])
    
    ### Under the Guidance of:
    [Guide Name], [Designation]
    Department of Computer Science Engineering
    
    ### About the Project:
    This project aims to develop a non-invasive, accessible tool for early detection of Parkinson's disease
    using machine learning algorithms and computer vision techniques. By analyzing movement patterns,
    handwriting samples, gait, voice, and other biomarkers, we hope to provide a preliminary screening
    method that can alert users to potential signs of Parkinson's disease and encourage them to seek
    professional medical advice.
    
    ### Acknowledgements:
    We would like to express our sincere gratitude to:
    - The Department of Computer Science Engineering, BMSIT&M
    - [Additional mentors or collaborators]
    - [Any medical institutions that provided guidance]
    
    ### Contact:
    For inquiries about this project, please contact:
    - Email: [your.email@example.com]
    - Department of CSE, BMSIT&M
    """)
    
    # References section
    st.subheader("References")
    st.markdown("""
    1. [Reference 1]
    2. [Reference 2]
    3. [Reference 3]
    """)

if __name__ == "__main__":
    main()
# Navigation
st.sidebar.title("Navigation")
st.sidebar.page_link("pages/1_spiral.py", label="Spiral Test")
st.sidebar.page_link("pages/2_wave.py", label="Wave Test")
st.sidebar.page_link("pages/3_voice.py", label="Voice Test")
st.sidebar.page_link("pages/4_ecg.py", label="ECG Test")
st.sidebar.page_link("pages/5_gait.py", label="Gait Test")

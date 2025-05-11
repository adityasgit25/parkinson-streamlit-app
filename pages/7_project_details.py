import streamlit as st

st.set_page_config(page_title="Project Details", page_icon="📄")

st.markdown("""
<style>
    .project-title {
        font-size: 2rem;
        color: #4285F4;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .section-header {
        font-size: 1.3rem;
        color: #64B5F6;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .content-card {
        background-color: #2A2A40;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        color: #E0E0E0;
    }
    .team-list {
        margin-left: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .guide {
        color: #FFD700;
        font-weight: 600;
    }
    .member {
        color: #90CAF9;
        font-weight: 500;
    }
    .video-link {
        color: #4CAF50;
        font-weight: 600;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="project-title">Enhancing Parkinson\'s Disease Management through Machine Learning Based System for Early Detection and Stage-Wise Assessment</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">Project Abstract</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
Parkinson’s disease (PD) is a chronic, progressive neurodegenerative disorder marked by both motor and non-motor impairments, which frequently go undetected until the disease reaches an advanced stage. This project introduces a robust, multi-modal diagnostic framework designed for the early detection and stage-wise assessment of PD, leveraging advanced machine learning algorithms. The system synthesizes diverse physiological and behavioral data, including gait dynamics, spiral and wave drawing patterns, vocal biomarkers, ECG readings, and blood oxygen saturation (SpO₂) levels.

To enhance user engagement and ensure intuitive data acquisition, a gamified interface is employed—featuring typing-based assessments, guided breathing modules, and interactive mouse-controlled coordination games. Complementing the software suite, a custom-built hardware prototype has been developed using microcontrollers and biomedical sensors to ensure accurate, real-time physiological signal acquisition.

Furthermore, the platform encompasses essential support features, such as integrated patient assistance, direct access to medical professionals, and automated health report generation. This comprehensive system aims to facilitate continuous monitoring, support timely clinical interventions, and ultimately contribute to improved diagnostic accuracy and patient outcomes in Parkinson’s care.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header">Project Team</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
<span class="guide">Guide:</span> Dr. Anil Kumar D, Professor, Dept of ECE, BMSIT&M<br><br>
<span class="member">Members:</span>
<ul class="team-list">
    <li>Adithya R Hiremath, 1BY21EC004, Dept. Of ECE, BMSIT&M</li>
    <li>Aditya Maheshwari, 1BY21EC006, Dept. Of ECE, BMSIT&M</li>
    <li>Amrithavarshini M, 1BY21EC011, Dept. Of ECE, BMSIT&M</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header">Project Video</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
<span class="video-link">[Project video will be uploaded here soon]</span>
</div>
""", unsafe_allow_html=True)
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Parkinson's Game Tests",
    page_icon="🎮",
    layout="wide"
)

# Custom styles (optional)
st.markdown("""
    <style>
        h1, h2, h3 {
            color: #64B5F6;
        }
        .content-card {
            background-color: #2A2A40;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            color: #E0E0E0;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<h1 class="main-header">Game-Based Cognitive & Motor Tests</h1>', unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="content-card">
    <p>These interactive games are designed to assess subtle motor, visual, and cognitive symptoms commonly associated with Parkinson’s Disease. Each game captures distinct behavioral data to help in the detection and monitoring process.</p>
</div>
""", unsafe_allow_html=True)

# Game Descriptions
st.markdown('<h2 class="sub-header">Explore the Games</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="content-card">
        <h3>⌨️ Typing Racer</h3>
        <p>This game challenges users to type random sequences quickly and accurately. It helps assess fine motor control, reaction time, and cognitive load.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-card">
        <h3>✨ Build Your Constellation</h3>
        <p>In this game, users draw lines to connect stars. This evaluates hand stability, precision, and spatial coordination—important markers in motor health.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="content-card">
        <h3>🌬️ Follow the Breathe</h3>
        <p>A calm-paced activity where users synchronize their clicks with a guided breathing animation, measuring rhythm perception and self-control.</p>
    </div>
    """, unsafe_allow_html=True)

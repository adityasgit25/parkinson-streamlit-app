# import streamlit as st
# import base64
# from PIL import Image
# import os


# # Configure the page
# st.set_page_config(
#     page_title="Parkinson's Disease Detection",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Add this CSS to hide only the default sidebar navigation links
# hide_default_nav = """
#     <style>
#         div[data-testid="stSidebarNav"] ul {display: none;}
#     </style>
# """
# st.markdown(hide_default_nav, unsafe_allow_html=True)

# # More targeted CSS to hide only code blocks while preserving other content
# st.markdown("""
# <style>
#     /* Hide only code blocks with more specific selectors */
#     .stCodeBlock code, div.stCodeBlock code, [data-testid="stCodeBlock"] code {
#         display: none !important;
#     }
    
#     /* Hide code editor elements */
#     .CodeMirror, .CodeMirror-scroll {
#         display: none !important;
#     }
    
#     /* Hide code blocks but preserve normal pre elements */
#     pre.language-python, pre.python, pre.code {
#         display: none !important;
#     }
    
#     /* Hide streamlit-specific code containers */
#     .stCodeBlock, .css-4zfol6, .css-keje6w {
#         display: none !important;
#     }
    
#     /* Make sure normal content stays visible */
#     .content-card, .team-member, div[style*="background-color: rgba(100, 181, 246, 0.1)"] {
#         display: block !important;
#         visibility: visible !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Custom CSS for dark theme matching the provided screenshots
# st.markdown("""
# <style>
#     /* Reset and global styling */
#     .stApp {
#         background-color: #1E1E2E !important;
#         color: #E0E0E0;
#     }
    
#     /* Sidebar styling */
#     section[data-testid="stSidebar"] {
#         background-color: #1E1E2E;
#         border-right: 1px solid #3A3A5A;
#     }
    
#     .sidebar-header {
#         font-size: 1.5rem;
#         font-weight: 500;
#         color: #64B5F6;
#         text-align: center;
#         margin-bottom: 1rem;
#         padding-bottom: 0.5rem;
#     }
    
#     /* Navigation links */
#     div.stButton > button {
#         background-color: transparent;
#         color: #E0E0E0;
#         border: none;
#         text-align: left;
#         padding: 0.75rem 1rem;
#         width: 100%;
#         font-size: 1rem;
#         border-radius: 8px;
#         margin-bottom: 0.25rem;
#         transition: background-color 0.2s;
#     }
    
#     div.stButton > button:hover {
#         background-color: rgba(100, 181, 246, 0.1);
#         color: #64B5F6;
#     }
    
#     div.stButton > button.active {
#         background-color: #64B5F6;
#         color: #1E1E2E;
#     }
    
#     /* Headers */
#     h1, h2, h3 {
#         color: #64B5F6;
#         font-weight: 500;
#     }
    
#     /* Content cards */
#     .content-card {
#         background-color: #2A2A40;
#         border-radius: 10px;
#         padding: 1.5rem;
#         margin-bottom: 1.5rem;
#     }
    
#     /* Feature buttons */
#     .feature-button {
#         background-color: #4285F4;
#         color: white;
#         font-weight: 500;
#         text-align: center;
#         padding: 0.75rem;
#         border-radius: 8px;
#         margin: 0.5rem 0;
#         cursor: pointer;
#         transition: background-color 0.3s;
#     }
    
#     .feature-button:hover {
#         background-color: #5C9EFF;
#     }
    
#     /* Team member */
#     .team-member {
#         padding: 0.75rem;
#         margin-bottom: 0.5rem;
#         background-color: #2A2A40;
#         border-radius: 5px;
#     }
    
#     /* Override Streamlit's default header styling */
#     .main-header {
#         font-size: 2rem;
#         color: #64B5F6;
#         font-weight: 500;
#     }
    
#     .sub-header {
#         font-size: 1.5rem;
#         color: #64B5F6;
#         font-weight: 500;
#         margin-top: 1rem;
#         margin-bottom: 0.5rem;
#     }
    
#     /* Custom horizontal line */
#     .custom-divider {
#         border-top: 1px solid #3A3A5A;
#         margin: 1.5rem 0;
#     }
    
#     /* Footer */
#     .footer {
#         color: #9E9E9E;
#         text-align: center;
#         padding: 1rem 0;
#         font-size: 0.85rem;
#     }
    
#     /* Hide Streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
    
#     /* Fix active navigation highlight */
#     .active-nav {
#         background-color: rgba(100, 181, 246, 0.2);
#         border-radius: 8px;
#     }
# </style>
# """, unsafe_allow_html=True)


# st.markdown("""
#     <div style="background-color: #AED6F1; padding: 10px; text-align: center;">
#         <img src="https://upload.wikimedia.org/wikipedia/en/6/65/B.M.S._Institute_of_Technology_and_Management_logo.png" style="height: 80px; margin-right: 20px; vertical-align: middle;">
#         <span style="display: inline-block; vertical-align: middle;">
#             <h1 style="margin: 0; color: #000; font-size: 24px;">BMS INSTITUTE OF TECHNOLOGY AND MANAGEMENT</h1>
#             <h2 style="margin: 5px 0 0 0; color: #000; font-size: 18px;">FINAL YEAR PROJECT - DEPT OF ECE</h2>
#         </span>
#     </div>
# """, unsafe_allow_html=True)

# # Sidebar navigation function
# def nav_page(page_name, icon="", active=False):
#     active_class = "active-nav" if active else ""
#     return f"""
#     <a href="/{page_name}" target="_self" style="text-decoration: none; color: inherit;">
#         <div class="nav-link {active_class}" style="padding: 0.75rem 1rem; margin-bottom: 0.25rem; border-radius: 8px;">
#             {icon} {page_name.replace('_', ' ').title()}
#         </div>
#     </a>
#     """

# # Sidebar
# with st.sidebar:
#     # st.markdown('<div class="sidebar-header">Parkinson\'s Disease<br>Detection System</div>', unsafe_allow_html=True)
    
#     # # Try to load college logo
#     # try:
#     #     logo = Image.open("logo.jpeg")
#     #     st.image(logo, width=150)
#     # except:
#     #     st.info("Place your college logo as 'logo.png' in the root directory")
    
#     # st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
#     # Navigation
#     current_page = "Home"
    
#     # Custom navigation links using HTML for better styling control
#     st.markdown(nav_page("Home", icon="🏠", active=(current_page=="Home")), unsafe_allow_html=True)
#     st.markdown(nav_page("patientInfo", icon="👤", active=(current_page=="patientInfo")), unsafe_allow_html=True)
#     st.markdown(nav_page("spiral", icon="🌀", active=(current_page=="spiral")), unsafe_allow_html=True)
#     st.markdown(nav_page("wave", icon="〰️", active=(current_page=="wave")), unsafe_allow_html=True)
#     st.markdown(nav_page("voice", icon="🎙️", active=(current_page=="voice")), unsafe_allow_html=True)
#     st.markdown(nav_page("ecg", icon="💓", active=(current_page=="ecg")), unsafe_allow_html=True)
#     st.markdown(nav_page("gait", icon="🚶", active=(current_page=="gait")), unsafe_allow_html=True)
#     st.markdown(nav_page("report", icon="📊", active=(current_page=="report")), unsafe_allow_html=True)
#     st.markdown(nav_page("game", icon="🎮", active=(current_page=="game")), unsafe_allow_html=True)
    
#     st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
#     # Team members
#     st.markdown("### Team Members")
#     team_members = [
#         {"name": "Adithya Hiremath", "usn": "1BY21EC004"},
#         {"name": "Aditya Maheshwari", "usn": "1BY21EC006"},
#         {"name": "Amrithavarshini M", "usn": "1BY21EC011"},
#     ]
    
#     for member in team_members:
#         st.markdown(f"""
#         <div class="team-member">
#             <b>{member['name']}</b><br>
#             <small>{member['usn']}</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
#     st.markdown('<div class="footer">© 2025 BMS Institute of Technology</div>', unsafe_allow_html=True)

# # Main content
# st.markdown('<h1 class="main-header">Parkinson\'s Disease Detection Portal</h1>', unsafe_allow_html=True)
# st.markdown('<p style="color: #9E9E9E; text-align: center;">Final Year Project - Department of ECE<br>BMS Institute of Technology and Management</p>', unsafe_allow_html=True)

# # Project introduction
# st.markdown('<h2 class="sub-header">About the Project</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <p>This project aims to develop a comprehensive system for early detection and monitoring of Parkinson's disease using multiple biomarkers and AI-based analysis. Our system incorporates five different modalities:</p>
#     <ul>
#         <li><b>Spiral Drawing Test</b>: Analysis of hand tremors through spiral drawing tasks</li>
#         <li><b>Wave Drawing Test</b>: Assessment of motor control through wave pattern drawings</li>
#         <li><b>Voice Analysis</b>: Detection of vocal biomarkers associated with Parkinson's</li>
#         <li><b>ECG Analysis</b>: Monitoring cardiac patterns that may indicate neurological disorders</li>
#         <li><b>Gait Analysis</b>: Evaluation of walking patterns for signs of Parkinson's disease</li>
#     </ul>
#     <p>The system uses machine learning algorithms to analyze the data collected from these tests and provides a comprehensive report that can assist medical professionals in diagnosis.</p>
# </div>
# """, unsafe_allow_html=True)

# # Feature buttons
# st.markdown('<h2 class="sub-header">Detection Features</h2>', unsafe_allow_html=True)
# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.markdown("""
#     <a href="/spiral" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Spiral Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <a href="/wave" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Wave Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <a href="/voice" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Voice Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col4:
#     st.markdown("""
#     <a href="/ecg" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             ECG Analysis
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col5:
#     st.markdown("""
#     <a href="/gait" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Gait Analysis
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# # How to use the website
# st.markdown('<h2 class="sub-header">How to Use This Platform</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <h4 style="color: #64B5F6;">Step-by-Step Guide:</h4>
#     <ol>
#         <li><b>Enter Patient Information</b>: Start by entering the patient's details in the Patient Info section.</li>
#         <li><b>Perform Tests</b>: Navigate through each test (Spiral, Wave, Voice, ECG, Gait) and follow the instructions to collect data.</li>
#         <li><b>View Analysis</b>: After completing the tests, the system will analyze the results using machine learning models.</li>
#         <li><b>Generate Report</b>: Visit the Report section to view a comprehensive analysis and download the results.</li>
#         <li><b>Consult Doctor</b>: Share the report with a healthcare professional for proper diagnosis and consultation.</li>
#     </ol>
#     <p><i>Note: This system is designed as a screening tool and should not replace professional medical diagnosis.</i></p>
# </div>
# """, unsafe_allow_html=True)

# # Data Collection Game
# st.markdown('<h2 class="sub-header">Typing Game for Data Collection</h2>', unsafe_allow_html=True)
# col1, col2 = st.columns([2, 1])

# with col1:
#     st.markdown("""
#     <div class="content-card">
#         <h4 style="color: #64B5F6;">Help Advance Research by Playing Our Game</h4>
#         <p>We've developed a simple typing game that helps us collect valuable data for improving our Parkinson's detection algorithms. By participating, you contribute to medical research while having fun!</p>
#         <h5 style="color: #64B5F6;">How to Play:</h5>
#         <ul>
#             <li>Type the words that appear on the screen as quickly and accurately as possible</li>
#             <li>The game measures your typing patterns and speed</li>
#             <li>Complete as many rounds as you'd like</li>
#             <li>All data is anonymized and used only for research purposes</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
#         <a href="/game" target="_self" style="text-decoration: none;">
#             <div style="background-color: #4CAF50; color: white; font-size: 1.1rem; font-weight: 500; padding: 15px 30px; border-radius: 8px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); transition: all 0.3s;">
#                 Play Game Now
#             </div>
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

# # Doctor contact info
# st.markdown('<h2 class="sub-header">Patient Assistance</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <h4 style="color: #64B5F6;">Consult with Specialists</h4>
#     <p>Our system connects you with neurologists specialized in movement disorders. Feel free to contact them for consultations with your report.</p>
    
#     <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem;">
#         <div style="flex: 1; min-width: 250px; background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6;">
#             <h5 style="color: #64B5F6;">Dr. Rajesh Kumar</h5>
#             <p>Neurologist, Movement Disorders Specialist<br>
#             📞 +91 9876543210<br>
#             📧 dr.rajesh@example.com<br>
#             🏥 City Neurology Center, 2nd Floor</p>
#         </div>
#         <div style="flex: 1; min-width: 250px; background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6;">
#             <h5 style="color: #64B5F6;">Dr. Priya Sharma</h5>
#             <p>Parkinson's Disease Specialist<br>
#             📞 +91 9876543211<br>
#             📧 dr.priya@example.com<br>
#             🏥 Movement Disorders Clinic, Main Street</p>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # Quick links
# st.markdown('<h2 class="sub-header">Quick Links</h2>', unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#     <a href="/patientInfo" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">Begin Assessment</h4>
#             <p>Start by entering patient information</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <a href="/report" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">View Report</h4>
#             <p>See comprehensive analysis results</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <a href="/game" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">Play Data Collection Game</h4>
#             <p>Contribute to research while having fun</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# # Add JavaScript for proper navigation
# st.markdown("""
# <script>
# document.addEventListener('DOMContentLoaded', function() {
#     const navLinks = document.querySelectorAll('a[href^="/"]');
#     navLinks.forEach(link => {
#         link.addEventListener('click', function(e) {
#             e.preventDefault();
#             const page = this.getAttribute('href').replace('/', '');
#             if (page === '') {
#                 window.location.href = '/';
#             } else {
#                 window.location.href = page;
#             }
#         });
#     });
# });
# </script>
# """, unsafe_allow_html=True)

# # Hidden functionality to initialize session state if needed
# if 'initialized' not in st.session_state:
#     st.session_state.initialized = True
#     # You can add any initial session state variables here







# import streamlit as st
# import base64
# from PIL import Image
# import os

# # Configure the page
# st.set_page_config(
#     page_title="Parkinson's Disease Detection",
#     page_icon="🧠",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # This CSS will hide all code elements and Streamlit's default components
# st.markdown("""
# <style>
#     /* Hide all code-related elements */
#     .stCodeBlock, pre, code, .CodeMirror, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
#         display: none !important;
#     }
    
#     /* Hide streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
    
#     /* Hide default sidebar navigation */
#     div[data-testid="stSidebarNav"] ul {display: none;}
    
#     /* Custom styling for dark theme */
#     .stApp {
#         background-color: #1E1E2E !important;
#         color: #E0E0E0;
#     }
    
#     /* Sidebar styling */
#     section[data-testid="stSidebar"] {
#         background-color: #1E1E2E;
#         border-right: 1px solid #3A3A5A;
#     }
    
#     .sidebar-header {
#         font-size: 1.5rem;
#         font-weight: 500;
#         color: #64B5F6;
#         text-align: center;
#         margin-bottom: 1rem;
#         padding-bottom: 0.5rem;
#     }
    
#     /* Navigation links */
#     div.stButton > button {
#         background-color: transparent;
#         color: #E0E0E0;
#         border: none;
#         text-align: left;
#         padding: 0.75rem 1rem;
#         width: 100%;
#         font-size: 1rem;
#         border-radius: 8px;
#         margin-bottom: 0.25rem;
#         transition: background-color 0.2s;
#     }
    
#     div.stButton > button:hover {
#         background-color: rgba(100, 181, 246, 0.1);
#         color: #64B5F6;
#     }
    
#     div.stButton > button.active {
#         background-color: #64B5F6;
#         color: #1E1E2E;
#     }
    
#     /* Headers */
#     h1, h2, h3 {
#         color: #64B5F6;
#         font-weight: 500;
#     }
    
#     /* Content cards */
#     .content-card {
#         background-color: #2A2A40;
#         border-radius: 10px;
#         padding: 1.5rem;
#         margin-bottom: 1.5rem;
#     }
    
#     /* Feature buttons */
#     .feature-button {
#         background-color: #4285F4;
#         color: white;
#         font-weight: 500;
#         text-align: center;
#         padding: 0.75rem;
#         border-radius: 8px;
#         margin: 0.5rem 0;
#         cursor: pointer;
#         transition: background-color 0.3s;
#     }
    
#     .feature-button:hover {
#         background-color: #5C9EFF;
#     }
    
#     /* Team member */
#     .team-member {
#         padding: 0.75rem;
#         margin-bottom: 0.5rem;
#         background-color: #2A2A40;
#         border-radius: 5px;
#     }
    
#     /* Override Streamlit's default header styling */
#     .main-header {
#         font-size: 2rem;
#         color: #64B5F6;
#         font-weight: 500;
#     }
    
#     .sub-header {
#         font-size: 1.5rem;
#         color: #64B5F6;
#         font-weight: 500;
#         margin-top: 1rem;
#         margin-bottom: 0.5rem;
#     }
    
#     /* Custom horizontal line */
#     .custom-divider {
#         border-top: 1px solid #3A3A5A;
#         margin: 1.5rem 0;
#     }
    
#     /* Footer */
#     .footer {
#         color: #9E9E9E;
#         text-align: center;
#         padding: 1rem 0;
#         font-size: 0.85rem;
#     }
    
#     /* Fix active navigation highlight */
#     .active-nav {
#         background-color: rgba(100, 181, 246, 0.2);
#         border-radius: 8px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # College header with logo
# st.markdown("""
#     <div style="background-color: #AED6F1; padding: 10px; text-align: center;">
#         <img src="https://upload.wikimedia.org/wikipedia/en/6/65/B.M.S._Institute_of_Technology_and_Management_logo.png" style="height: 80px; margin-right: 20px; vertical-align: middle;">
#         <span style="display: inline-block; vertical-align: middle;">
#             <h1 style="margin: 0; color: #000; font-size: 24px;">BMS INSTITUTE OF TECHNOLOGY AND MANAGEMENT</h1>
#             <h2 style="margin: 5px 0 0 0; color: #000; font-size: 18px;">FINAL YEAR PROJECT - DEPT OF ECE</h2>
#         </span>
#     </div>
# """, unsafe_allow_html=True)

# # Function to create navigation links
# def nav_page(page_name, icon="", active=False):
#     active_class = "active-nav" if active else ""
#     return f"""
#     <a href="/{page_name}" target="_self" style="text-decoration: none; color: inherit;">
#         <div class="nav-link {active_class}" style="padding: 0.75rem 1rem; margin-bottom: 0.25rem; border-radius: 8px;">
#             {icon} {page_name.replace('_', ' ').title()}
#         </div>
#     </a>
#     """

# # Sidebar navigation
# with st.sidebar:
#     current_page = "Home"
    
#     # Navigation links
#     st.markdown(nav_page("Home", icon="🏠", active=(current_page=="Home")), unsafe_allow_html=True)
#     st.markdown(nav_page("patientInfo", icon="👤", active=(current_page=="patientInfo")), unsafe_allow_html=True)
#     st.markdown(nav_page("spiral", icon="🌀", active=(current_page=="spiral")), unsafe_allow_html=True)
#     st.markdown(nav_page("wave", icon="〰️", active=(current_page=="wave")), unsafe_allow_html=True)
#     st.markdown(nav_page("voice", icon="🎙️", active=(current_page=="voice")), unsafe_allow_html=True)
#     st.markdown(nav_page("ecg", icon="💓", active=(current_page=="ecg")), unsafe_allow_html=True)
#     st.markdown(nav_page("gait", icon="🚶", active=(current_page=="gait")), unsafe_allow_html=True)
#     st.markdown(nav_page("report", icon="📊", active=(current_page=="report")), unsafe_allow_html=True)
#     st.markdown(nav_page("game", icon="🎮", active=(current_page=="game")), unsafe_allow_html=True)
    
#     st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
#     # Team members section
#     st.markdown("### Team Members")
#     team_members = [
#         {"name": "Adithya Hiremath", "usn": "1BY21EC004"},
#         {"name": "Aditya Maheshwari", "usn": "1BY21EC006"},
#         {"name": "Amrithavarshini M", "usn": "1BY21EC011"},
#     ]
    
#     for member in team_members:
#         st.markdown(f"""
#         <div class="team-member">
#             <b>{member['name']}</b><br>
#             <small>{member['usn']}</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
#     st.markdown('<div class="footer">© 2025 BMS Institute of Technology</div>', unsafe_allow_html=True)

# # Main content
# st.markdown('<h1 class="main-header">Parkinson\'s Disease Detection Portal</h1>', unsafe_allow_html=True)
# st.markdown('<p style="color: #9E9E9E; text-align: center;">Final Year Project - Department of ECE<br>BMS Institute of Technology and Management</p>', unsafe_allow_html=True)

# # Project introduction
# st.markdown('<h2 class="sub-header">About the Project</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <p>This project aims to develop a comprehensive system for early detection and monitoring of Parkinson's disease using multiple biomarkers and AI-based analysis. Our system incorporates five different modalities:</p>
#     <ul>
#         <li><b>Spiral Drawing Test</b>: Analysis of hand tremors through spiral drawing tasks</li>
#         <li><b>Wave Drawing Test</b>: Assessment of motor control through wave pattern drawings</li>
#         <li><b>Voice Analysis</b>: Detection of vocal biomarkers associated with Parkinson's</li>
#         <li><b>ECG Analysis</b>: Monitoring cardiac patterns that may indicate neurological disorders</li>
#         <li><b>Gait Analysis</b>: Evaluation of walking patterns for signs of Parkinson's disease</li>
#     </ul>
#     <p>The system uses machine learning algorithms to analyze the data collected from these tests and provides a comprehensive report that can assist medical professionals in diagnosis.</p>
# </div>
# """, unsafe_allow_html=True)

# # Feature buttons
# st.markdown('<h2 class="sub-header">Detection Features</h2>', unsafe_allow_html=True)
# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.markdown("""
#     <a href="/spiral" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Spiral Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <a href="/wave" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Wave Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <a href="/voice" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Voice Test
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col4:
#     st.markdown("""
#     <a href="/ecg" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             ECG Analysis
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col5:
#     st.markdown("""
#     <a href="/gait" target="_self" style="text-decoration: none;">
#         <div class="feature-button">
#             Gait Analysis
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# # How to use the website
# st.markdown('<h2 class="sub-header">How to Use This Platform</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <h4 style="color: #64B5F6;">Step-by-Step Guide:</h4>
#     <ol>
#         <li><b>Enter Patient Information</b>: Start by entering the patient's details in the Patient Info section.</li>
#         <li><b>Perform Tests</b>: Navigate through each test (Spiral, Wave, Voice, ECG, Gait) and follow the instructions to collect data.</li>
#         <li><b>View Analysis</b>: After completing the tests, the system will analyze the results using machine learning models.</li>
#         <li><b>Generate Report</b>: Visit the Report section to view a comprehensive analysis and download the results.</li>
#         <li><b>Consult Doctor</b>: Share the report with a healthcare professional for proper diagnosis and consultation.</li>
#     </ol>
#     <p><i>Note: This system is designed as a screening tool and should not replace professional medical diagnosis.</i></p>
# </div>
# """, unsafe_allow_html=True)

# # Data Collection Game
# st.markdown('<h2 class="sub-header">Typing Game for Data Collection</h2>', unsafe_allow_html=True)
# col1, col2 = st.columns([2, 1])

# with col1:
#     st.markdown("""
#     <div class="content-card">
#         <h4 style="color: #64B5F6;">Help Advance Research by Playing Our Game</h4>
#         <p>We've developed a simple typing game that helps us collect valuable data for improving our Parkinson's detection algorithms. By participating, you contribute to medical research while having fun!</p>
#         <h5 style="color: #64B5F6;">How to Play:</h5>
#         <ul>
#             <li>Type the words that appear on the screen as quickly and accurately as possible</li>
#             <li>The game measures your typing patterns and speed</li>
#             <li>Complete as many rounds as you'd like</li>
#             <li>All data is anonymized and used only for research purposes</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
#         <a href="/game" target="_self" style="text-decoration: none;">
#             <div style="background-color: #4CAF50; color: white; font-size: 1.1rem; font-weight: 500; padding: 15px 30px; border-radius: 8px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); transition: all 0.3s;">
#                 Play Game Now
#             </div>
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

# # Doctor contact info
# st.markdown('<h2 class="sub-header">Patient Assistance</h2>', unsafe_allow_html=True)
# st.markdown("""
# <div class="content-card">
#     <h4 style="color: #64B5F6;">Consult with Specialists</h4>
#     <p>Our system connects you with neurologists specialized in movement disorders. Feel free to contact them for consultations with your report.</p>
    
#     <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1rem;">
#         <div style="flex: 1; min-width: 250px; background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6;">
#             <h5 style="color: #64B5F6;">Dr. Rajesh Kumar</h5>
#             <p>Neurologist, Movement Disorders Specialist<br>
#             📞 +91 9876543210<br>
#             📧 dr.rajesh@example.com<br>
#             🏥 City Neurology Center, 2nd Floor</p>
#         </div>
#         <div style="flex: 1; min-width: 250px; background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6;">
#             <h5 style="color: #64B5F6;">Dr. Priya Sharma</h5>
#             <p>Parkinson's Disease Specialist<br>
#             📞 +91 9876543211<br>
#             📧 dr.priya@example.com<br>
#             🏥 Movement Disorders Clinic, Main Street</p>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # Quick links
# st.markdown('<h2 class="sub-header">Quick Links</h2>', unsafe_allow_html=True)
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("""
#     <a href="/patientInfo" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">Begin Assessment</h4>
#             <p>Start by entering patient information</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <a href="/report" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">View Report</h4>
#             <p>See comprehensive analysis results</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown("""
#     <a href="/game" target="_self" style="text-decoration: none;">
#         <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
#             <h4 style="color: #64B5F6;">Play Data Collection Game</h4>
#             <p>Contribute to research while having fun</p>
#         </div>
#     </a>
#     """, unsafe_allow_html=True)

# # JavaScript for navigation
# st.markdown("""
# <script>
# document.addEventListener('DOMContentLoaded', function() {
#     const navLinks = document.querySelectorAll('a[href^="/"]');
#     navLinks.forEach(link => {
#         link.addEventListener('click', function(e) {
#             e.preventDefault();
#             const page = this.getAttribute('href').replace('/', '');
#             if (page === '') {
#                 window.location.href = '/';
#             } else {
#                 window.location.href = page;
#             }
#         });
#     });
# });
# </script>
# """, unsafe_allow_html=True)

# # Initialize session state if needed
# if 'initialized' not in st.session_state:
#     st.session_state.initialized = True

import streamlit as st
import base64
from PIL import Image
import os

# Configure the page
st.set_page_config(
    page_title="Parkinson's Disease Detection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# This CSS will hide all code elements and Streamlit's default components
st.markdown("""
<style>
    /* Hide all code-related elements */
    .stCodeBlock, pre, code, .CodeMirror, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
        display: none !important;
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Hide default sidebar navigation */
    div[data-testid="stSidebarNav"] ul {display: none;}
    
    /* Custom styling for dark theme */
    .stApp {
        background-color: #1E1E2E !important;
        color: #E0E0E0;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #1E1E2E;
        border-right: 1px solid #3A3A5A;
    }
    
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: 500;
        color: #64B5F6;
        text-align: center;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
    }
    
    /* Navigation links */
    div.stButton > button {
        background-color: transparent;
        color: #E0E0E0;
        border: none;
        text-align: left;
        padding: 0.75rem 1rem;
        width: 100%;
        font-size: 1rem;
        border-radius: 8px;
        margin-bottom: 0.25rem;
        transition: background-color 0.2s;
    }
    
    div.stButton > button:hover {
        background-color: rgba(100, 181, 246, 0.1);
        color: #64B5F6;
    }
    
    div.stButton > button.active {
        background-color: #64B5F6;
        color: #1E1E2E;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #64B5F6;
        font-weight: 500;
    }
    
    /* Content cards */
    .content-card {
        background-color: #2A2A40;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    /* Feature buttons */
    .feature-button {
        background-color: #4285F4;
        color: white;
        font-weight: 500;
        text-align: center;
        padding: 0.75rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    
    .feature-button:hover {
        background-color: #5C9EFF;
    }
    
    /* Team member */
    .team-member {
        padding: 0.75rem;
        margin-bottom: 0.5rem;
        background-color: #2A2A40;
        border-radius: 5px;
    }
    
    /* Override Streamlit's default header styling */
    .main-header {
        font-size: 2rem;
        color: #64B5F6;
        font-weight: 500;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #64B5F6;
        font-weight: 500;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Custom horizontal line */
    .custom-divider {
        border-top: 1px solid #3A3A5A;
        margin: 1.5rem 0;
    }
    
    /* Footer */
    .footer {
        color: #9E9E9E;
        text-align: center;
        padding: 1rem 0;
        font-size: 0.85rem;
    }
    
    /* Fix active navigation highlight */
    .active-nav {
        background-color: rgba(100, 181, 246, 0.2);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# College header with logo
st.markdown("""
    <div style="background-color: #AED6F1; padding: 10px; text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/en/6/65/B.M.S._Institute_of_Technology_and_Management_logo.png" style="height: 80px; margin-right: 20px; vertical-align: middle;">
        <span style="display: inline-block; vertical-align: middle;">
            <h1 style="margin: 0; color: #000; font-size: 24px;">BMS INSTITUTE OF TECHNOLOGY AND MANAGEMENT</h1>
            <h2 style="margin: 5px 0 0 0; color: #000; font-size: 18px;">FINAL YEAR PROJECT - DEPT OF ECE</h2>
        </span>
    </div>
""", unsafe_allow_html=True)

# Function to create navigation links
def nav_page(page_name, icon="", active=False):
    active_class = "active-nav" if active else ""
    return f"""
    <a href="/{page_name}" target="_self" style="text-decoration: none; color: inherit;">
        <div class="nav-link {active_class}" style="padding: 0.75rem 1rem; margin-bottom: 0.25rem; border-radius: 8px;">
            {icon} {page_name.replace('_', ' ').title()}
        </div>
    </a>
    """

# Sidebar navigation
with st.sidebar:
    current_page = "Home"
    
    # Navigation links
    st.markdown(nav_page("Home", icon="🏠", active=(current_page=="Home")), unsafe_allow_html=True)
    st.markdown(nav_page("patientInfo", icon="👤", active=(current_page=="patientInfo")), unsafe_allow_html=True)
    st.markdown(nav_page("spiral", icon="🌀", active=(current_page=="spiral")), unsafe_allow_html=True)
    st.markdown(nav_page("wave", icon="〰️", active=(current_page=="wave")), unsafe_allow_html=True)
    st.markdown(nav_page("voice", icon="🎙️", active=(current_page=="voice")), unsafe_allow_html=True)
    st.markdown(nav_page("ecg", icon="💓", active=(current_page=="ecg")), unsafe_allow_html=True)
    st.markdown(nav_page("gait", icon="🚶", active=(current_page=="gait")), unsafe_allow_html=True)
    st.markdown(nav_page("report", icon="📊", active=(current_page=="report")), unsafe_allow_html=True)
    st.markdown(nav_page("game", icon="🎮", active=(current_page=="game")), unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Team guide section
    st.markdown("### Team Guide")
    st.markdown("""
    <div class="team-member">
        <b>Dr. Anil Kumar D</b><br>
        <small>Professor, Dept. of ECE</small>
    </div>
    """, unsafe_allow_html=True)

    
    # Team members section
    st.markdown("### Team Members")
    team_members = [
        {"name": "Adithya Hiremath", "usn": "1BY21EC004"},
        {"name": "Aditya Maheshwari", "usn": "1BY21EC006"},
        {"name": "Amrithavarshini M", "usn": "1BY21EC011"},
    ]
    
    for member in team_members:
        st.markdown(f"""
        <div class="team-member">
            <b>{member['name']}</b><br>
            <small>{member['usn']}</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">© 2025 BMS Institute of Technology</div>', unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">Parkinson\'s Disease Detection Portal</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #9E9E9E; text-align: center;">Final Year Project - Department of ECE<br>BMS Institute of Technology and Management</p>', unsafe_allow_html=True)

# Project introduction
st.markdown('<h2 class="sub-header">About the Project</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
    <p>This project aims to develop a comprehensive system for early detection and monitoring of Parkinson's disease using multiple biomarkers and AI-based analysis. Our system incorporates five different modalities:</p>
    <ul>
        <li><b>Spiral Drawing Test</b>: Analysis of hand tremors through spiral drawing tasks</li>
        <li><b>Wave Drawing Test</b>: Assessment of motor control through wave pattern drawings</li>
        <li><b>Voice Analysis</b>: Detection of vocal biomarkers associated with Parkinson's</li>
        <li><b>ECG Analysis</b>: Monitoring cardiac patterns that may indicate neurological disorders</li>
        <li><b>Gait Analysis</b>: Evaluation of walking patterns for signs of Parkinson's disease</li>
    </ul>
    <p>The system uses machine learning algorithms to analyze the data collected from these tests and provides a comprehensive report that can assist medical professionals in diagnosis.</p>
</div>
""", unsafe_allow_html=True)

# Feature buttons
st.markdown('<h2 class="sub-header">Detection Features</h2>', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <a href="/spiral" target="_self" style="text-decoration: none;">
        <div class="feature-button">
            Spiral Test
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/wave" target="_self" style="text-decoration: none;">
        <div class="feature-button">
            Wave Test
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/voice" target="_self" style="text-decoration: none;">
        <div class="feature-button">
            Voice Test
        </div>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="/ecg" target="_self" style="text-decoration: none;">
        <div class="feature-button">
            ECG Analysis
        </div>
    </a>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <a href="/gait" target="_self" style="text-decoration: none;">
        <div class="feature-button">
            Gait Analysis
        </div>
    </a>
    """, unsafe_allow_html=True)

# How to use the website
st.markdown('<h2 class="sub-header">How to Use This Platform</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
    <h4 style="color: #64B5F6;">Step-by-Step Guide:</h4>
    <ol>
        <li><b>Enter Patient Information</b>: Start by entering the patient's details in the Patient Info section.</li>
        <li><b>Perform Tests</b>: Navigate through each test (Spiral, Wave, Voice, ECG, Gait) and follow the instructions to collect data.</li>
        <li><b>View Analysis</b>: After completing the tests, the system will analyze the results using machine learning models.</li>
        <li><b>Generate Report</b>: Visit the Report section to view a comprehensive analysis and download the results.</li>
        <li><b>Consult Doctor</b>: Share the report with a healthcare professional for proper diagnosis and consultation.</li>
    </ol>
    <p><i>Note: This system is designed as a screening tool and should not replace professional medical diagnosis.</i></p>
</div>
""", unsafe_allow_html=True)

# Data Collection Game
st.markdown('<h2 class="sub-header">Typing Game for Data Collection</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="content-card">
        <h4 style="color: #64B5F6;">Help Advance Research by Playing Our Game</h4>
        <p>We've developed a simple typing game that helps us collect valuable data for improving our Parkinson's detection algorithms. By participating, you contribute to medical research while having fun!</p>
        <h5 style="color: #64B5F6;">How to Play:</h5>
        <ul>
            <li>Type the words that appear on the screen as quickly and accurately as possible</li>
            <li>The game measures your typing patterns and speed</li>
            <li>Complete as many rounds as you'd like</li>
            <li>All data is anonymized and used only for research purposes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <a href="/game" target="_self" style="text-decoration: none;">
            <div style="background-color: #4CAF50; color: white; font-size: 1.1rem; font-weight: 500; padding: 15px 30px; border-radius: 8px; text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); transition: all 0.3s;">
                Play Game Now
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Doctor contact info
st.markdown('<h2 class="sub-header">Patient Assistance</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="content-card">
    <h4 style="color: #64B5F6;">Consult with Specialists</h4>
    <p>Our system connects you with neurologists specialized in movement disorders. Feel free to contact them for consultations with your report.</p>
</div>
""", unsafe_allow_html=True)

# Creating doctor cards using columns to ensure visibility
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6; height: 100%;">
        <h5 style="color: #64B5F6;">Dr. Rajesh Kumar</h5>
        <p>Neurologist, Movement Disorders Specialist<br>
        📞 +91 9876543210<br>
        📧 dr.rajesh@example.com<br>
        🏥 City Neurology Center, 2nd Floor</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: rgba(100, 181, 246, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #64B5F6; height: 100%;">
        <h5 style="color: #64B5F6;">Dr. Priya Sharma</h5>
        <p>Parkinson's Disease Specialist<br>
        📞 +91 9876543211<br>
        📧 dr.priya@example.com<br>
        🏥 Movement Disorders Clinic, Main Street</p>
    </div>
    """, unsafe_allow_html=True)

# Quick links
st.markdown('<h2 class="sub-header">Quick Links</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="/patientInfo" target="_self" style="text-decoration: none;">
        <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
            <h4 style="color: #64B5F6;">Begin Assessment</h4>
            <p>Start by entering patient information</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="/report" target="_self" style="text-decoration: none;">
        <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
            <h4 style="color: #64B5F6;">View Report</h4>
            <p>See comprehensive analysis results</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="/game" target="_self" style="text-decoration: none;">
        <div class="content-card" style="text-align: center; cursor: pointer; transition: transform 0.2s;">
            <h4 style="color: #64B5F6;">Play Data Collection Game</h4>
            <p>Contribute to research while having fun</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

# JavaScript for navigation
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('a[href^="/"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const page = this.getAttribute('href').replace('/', '');
            if (page === '') {
                window.location.href = '/';
            } else {
                window.location.href = page;
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)

# Initialize session state if needed
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
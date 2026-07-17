import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Advanced CSS injection for Glassmorphism, subtle glowing shadows, and micro-interactions
st.markdown("""
    <style>
    /* Overall Background Pattern */
    .stApp {
        background: radial-gradient(circle at 90% 10%, rgba(79, 70, 229, 0.06) 0%, transparent 40%),
                    radial-gradient(circle at 10% 80%, rgba(16, 185, 129, 0.04) 0%, transparent 40%),
                    #f8fafc;
    }
    
    /* Input Card Layer Styling - Soft shadows and crisp borders */
    .input-section [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(226, 232, 240, 0.8) !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 20px -2px rgba(148, 163, 184, 0.12), 
                    0 2px 8px -1px rgba(148, 163, 184, 0.08) !important;
        padding: 28px !important;
        margin-bottom: 24px !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    /* Interactive Hover Effect for the Input Card */
    .input-section [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 24px -4px rgba(148, 163, 184, 0.18), 
                    0 4px 12px -2px rgba(148, 163, 184, 0.1) !important;
    }

    /* Output Section Layer Styling - Darker border-left accent with neon glow */
    .results-section [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 6px solid #4F46E5 !important;
        border-radius: 16px !important;
        box-shadow: 0 20px 25px -5px rgba(79, 70, 229, 0.08), 
                    0 8px 10px -6px rgba(79, 70, 229, 0.08) !important;
        padding: 28px !important;
    }
    
    /* Streamlit Widget Metric Component Overrides */
    [data-testid="stMetricValue"] {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: #4F46E5 !important;
        letter-spacing: -0.05em;
    }
    
    [data-testid="stMetricLabel"] {
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.78rem !important;
        color: #64748b !important;
        font-weight: 600;
    }

    /* Custom Title Typography styling */
    .main-title {
        background: linear-gradient(135deg, #1e293b 0%, #4F46E5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.03em;
    }
    
    .subtext {
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 2.5rem;
        line-height: 1.5;
    }
    
    h3 {
        color: #334155 !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model safely
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model.pkl: {e}")
    st.stop()

# Typography Banner Area
st.markdown('<h1 class="main-title">🎓 Student Performance Intelligence</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtext">An advanced analytics layer mapping core behaviors directly to expected performance margins. Refine the baseline metrics below to generate insight projections.</p>', 
    unsafe_allow_html=True
)

# Vertical Layout Block 1: Inputs embedded into our Glassmorphism block
st.markdown('<div class="input-section">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3>📊 Academic Habit Matrix</h3>', unsafe_allow_html=True)
    
    hours_studied = st.slider(
        "Hours Studied (per week)", 
        min_value=0.0, max_value=100.0, value=10.0, step=0.5
    )

    sleep_hours = st.slider(
        "Sleep Hours (per night)", 
        min_value=0.0, max_value=24.0, value=7.0, step=0.5
    )

    attendance_percent = st.slider(
        "Attendance Percentage (%)", 
        min_value=0.0, max_value=100.0, value=85.0, step=1.0
    )

    previous_scores = st.number_input(
        "Previous Exam Score Target", 
        min_value=0.0, max_value=100.0, value=75.0, step=1.0
    )
st.markdown('</div>', unsafe_allow_html=True)

# Grid separation layout for processing activation button
_, col_btn, _ = st.columns([1, 2, 1])
with col_btn:
    predict_clicked = st.button("Generate Performance Insight", type="primary", use_container_width=True)

st.write("") # Design spacing buffer

# Vertical Layout Block 2: Results Panel Output Matrix
st.markdown('<div class="results-section">', unsafe_allow_html=True)

if predict_clicked:
    input_data = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    with st.spinner("Processing behaviors through regression layers..."):
        try:
            prediction = model.predict(input_data)[0]
            display_score = min(max(prediction, 0.0), 100.0)
            
            with st.container(border=True):
                st.markdown('<h3>🎯 Analytical Projections</h3>', unsafe_allow_html=True)
                
                st.metric(
                    label="Predicted Achievement Quotient", 
                    value=f"{display_score:.2f}%"
                )
                
                # Semantic output feedback tiers
                if display_score >= 85:
                    st.balloons()
                    st.success("🌟 **Optimal Velocity Profile:** Data tracks firmly within high-tier outcomes. Current pacing supports top-bracket positioning.")
                elif display_score >= 50:
                    st.info("👍 **Passing Variance Stable:** Behaviors safely satisfy benchmark standards. Incrementing weekly study velocity will yield immediate value compounding.")
                else:
                    st.warning("⚠️ **Risk Threshold Breached:** Performance projections slip below target floors. Operational modifications in attendance or sleep allocation recommended.")
                    
        except Exception as e:
            st.error(f"Execution Exception encountered: {e}")
else:
    # Rest state resting visual container 
    with st.container(border=True):
        st.markdown('<p style="color: #94a3b8; margin: 0; text-align: center; font-size: 0.95rem;">System resting. Calibrate inputs above and trigger processing to display analytics.</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

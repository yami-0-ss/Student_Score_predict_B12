import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & STRUCTURAL THEMING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Academic Intelligence Dashboard",
    page_icon="⚡",
    layout="centered"
)

# Premium UI Styling Engine (Deep Slate Canvas + High-Contrast Typography)
st.markdown("""
    <style>
    /* Global Canvas Styling */
    .stApp {
        background: radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.12) 0%, transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(16, 185, 129, 0.08) 0%, transparent 50%),
                    #0f172a; /* Futuristic Deep Slate Dark Mode */
    }
    
    /* Clean Label & Typography Tuning */
    h1, h2, h3, p, label, .stSlider {
        color: #f8fafc !important;
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 600 !important;
        letter-spacing: 0.06em;
        color: #94a3b8 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase;
    }

    /* Behavioral Feature Matrix Glass Container */
    .feature-matrix-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5) !important;
        padding: 32px !important;
    }

    /* Analytics Hub Glass Container (Glow Effect) */
    .analytics-hub-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%) !important;
        border: 1px solid rgba(99, 102, 241, 0.25) !important;
        border-radius: 24px !important;
        box-shadow: 0 0 30px rgba(99, 102, 241, 0.15), inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Value Metric Tuning (Vibrant Gradient Text) */
    [data-testid="stMetricValue"] {
        font-size: 3.6rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.06em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.85rem !important;
    }

    /* Title Styling Architecture */
    .dashboard-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        margin-bottom: 2px;
    }
    
    .dashboard-subtitle {
        color: #64748b !important;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MODEL INGESTION ENGINE
# -----------------------------------------------------------------------------
@st.cache_resource
def load_predictive_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    predictive_model = load_predictive_model()
except Exception as error:
    st.error(f"Error initializing predictive engine: {error}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. DASHBOARD HEADER & SYSTEM INFRASTRUCTURE KPI BAR
# -----------------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">⚡ EduAnalytics Intelligence Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Predictive student monitoring environment driven by machine learning.</p>', unsafe_allow_html=True)

# System Architecture Insight Badges
kpi_1, kpi_2, kpi_3 = st.columns(3)
with kpi_1:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:16px; border-radius:14px; border-left:4px solid #6366f1;"><span style="color:#94a3b8; font-size:0.75rem; text-transform:uppercase; font-weight:600; letter-spacing:0.05em;">Model Architecture</span><br><b style="font-size:1.1rem; color:#fff;">K-Nearest Neighbors</b></div>', unsafe_allow_html=True)
with kpi_2:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:16px; border-radius:14px; border-left:4px solid #10b981;"><span style="color:#94a3b8; font-size:0.75rem; text-transform:uppercase; font-weight:600; letter-spacing:0.05em;">Feature Vectors</span><br><b style="font-size:1.1rem; color:#fff;">4 Dimensions</b></div>', unsafe_allow_html=True)
with kpi_3:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:16px; border-radius:14px; border-left:4px solid #f59e0b;"><span style="color:#94a3b8; font-size:0.75rem; text-transform:uppercase; font-weight:600; letter-spacing:0.05em;">Target Variable</span><br><b style="font-size:1.1rem; color:#fff;">Final Grade %</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. DATA MATRIX INPUT LAYER (2x2 GRID STRUCTURE)
# -----------------------------------------------------------------------------
st.markdown('<div class="feature-matrix-card">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 24px; font-size:1.2rem; font-weight:700; color:#f1f5f9; letter-spacing:-0.02em;">📊 Student Behavior Matrix</h3>', unsafe_allow_html=True)
    
    grid_left, grid_right = st.columns(2)
    with grid_left:
        hours_studied = st.slider("Weekly Study Hours", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("Attendance Rate (%)", 0.0, 100.0, 90.0, 1.0)
    with grid_right:
        sleep_hours = st.slider("Nightly Sleep Hours", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("Last Assessment Score", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Centered Action Trigger Button
_, alignment_col, _ = st.columns([1, 2, 1])
with alignment_col:
    compute_analytics = st.button("RUN PREDICTIVE ENGINE", type="primary", use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. DIAGNOSTIC ANALYTICS HUB LAYER
# -----------------------------------------------------------------------------
st.markdown('<div class="analytics-hub-card">', unsafe_allow_html=True)
with st.container(border=True):
    if compute_analytics:
        # Vectorize variables into exact model footprint shape
        features_vector = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = predictive_model.predict(features_vector)[0]
            final_index = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#818cf8; font-weight:700; font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase;">Analysis Concluded</span>', unsafe_allow_html=True)
            st.metric(label="Calculated Performance Index", value=f"{final_index:.1f}%")
            
            # Semantic Outcome Badges based on Grading Tiers
            if final_index >= 85:
                st.balloons()
                st.markdown('<div style="background:rgba(16,185,129,0.12); border:1px solid #10b981; color:#34d399; padding:14px; border-radius:12px; font-weight:600; font-size:0.92rem; letter-spacing:0.02em;">👑 EXCELLENCE MARGIN EXPECTED: TOP TIER TRACKING</div>', unsafe_allow_html=True)
            elif final_index >= 50:
                st.markdown('<div style="background:rgba(59,130,246,0.12); border:1px solid #3b82f6; color:#60a5fa; padding:14px; border-radius:12px; font-weight:600; font-size:0.92rem; letter-spacing:0.02em;">📈 STABLE PROJECTION: STABILIZED PASS METRIC MET</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:rgba(239,68,68,0.12); border:1px solid #ef4444; color:#f87171; padding:14px; border-radius:12px; font-weight:600; font-size:0.92rem; letter-spacing:0.02em;">⚠️ CRITICAL DIAGNOSTIC: INTERVENTION THRESHOLD BREACHED</div>', unsafe_allow_html=True)
                
        except Exception as prediction_error:
            st.error(f"Execution Discrepancy: {prediction_error}")
    else:
        st.markdown('<p style="color: #475569; margin: 0; font-weight:600; font-size:0.85rem; letter-spacing:0.12em;">AWAITING COMMAND INGESTION • TARGET CORE STANDING BY</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

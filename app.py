import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & MINIMALIST PURPLE THEMING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="EduMetrics Analytics Hub",
    page_icon="🔮",
    layout="centered"
)

# Premium Light Mode Custom Styling Engine (Crisp White + Royal Purple Accents)
st.markdown("""
    <style>
    /* Global Background (Soft Light Gray) */
    .stApp {
        background: radial-gradient(circle at 90% 10%, rgba(109, 40, 217, 0.05) 0%, transparent 40%),
                    #f8fafc; 
    }
    
    /* Clean Typography & Header Tuning */
    h1, h2, h3, p, label, .stSlider {
        color: #1e293b !important; /* Deep Charcoal for readability */
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 700 !important;
        letter-spacing: 0.06em;
        color: #6d28d9 !important; /* Royal Purple Labels */
        font-size: 0.82rem !important;
        text-transform: uppercase;
    }

    /* Behavioral Feature Matrix - Pure White Card with Amethyst Shadow */
    .feature-matrix-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 25px -5px rgba(109, 40, 217, 0.04), 
                    0 8px 10px -6px rgba(109, 40, 217, 0.04) !important;
        padding: 32px !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-matrix-card [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 30px -10px rgba(109, 40, 217, 0.08) !important;
    }

    /* Analytics Hub Container (Elegant Purple Gradient Boundary) */
    .analytics-hub-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-top: 5px solid #6d28d9 !important; /* Thick Purple Accent Top Border */
        border-radius: 16px !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Target Metric Display (Deep Amethyst Gradient Text) */
    [data-testid="stMetricValue"] {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 50%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.85rem !important;
        font-weight: 600;
    }

    /* Premium Purple Dashboard Title Architecture */
    .dashboard-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #1e293b 30%, #6d28d9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        margin-bottom: 2px;
    }
    
    .dashboard-subtitle {
        color: #64748b !important;
        font-size: 1.05rem;
        margin-bottom: 2.5rem;
    }
    
    /* Override primary button styling to match brand colors */
    .stButton>button {
        background-color: #6d28d9 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 12px rgba(109, 40, 217, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        background-color: #5b21b6 !important;
        box-shadow: 0 6px 16px rgba(109, 40, 217, 0.3) !important;
        transform: translateY(-1px);
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
# 3. INFRASTRUCTURE KPI BAR
# -----------------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">🔮 EduMetrics Intelligence Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Predictive analytics environment driven by machine learning.</p>', unsafe_allow_html=True)

# System Performance Insight Badges with clean purple highlights
kpi_1, kpi_2, kpi_3 = st.columns(3)
with kpi_1:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:12px; border: 1px solid #e2e8f0; border-left:4px solid #6d28d9;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Engine Core</span><br><b style="font-size:1.1rem; color:#1e293b;">K-Nearest Neighbors</b></div>', unsafe_allow_html=True)
with kpi_2:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:12px; border: 1px solid #e2e8f0; border-left:4px solid #8b5cf6;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Input Layers</span><br><b style="font-size:1.1rem; color:#1e293b;">4 Dimensions</b></div>', unsafe_allow_html=True)
with kpi_3:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:12px; border: 1px solid #e2e8f0; border-left:4px solid #c084fc;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Target Variable</span><br><b style="font-size:1.1rem; color:#1e293b;">Final Grade %</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. DATA MATRIX INPUT LAYER (2x2 CARD LAYOUT)
# -----------------------------------------------------------------------------
st.markdown('<div class="feature-matrix-card">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 24px; font-size:1.2rem; font-weight:700; color:#1e293b; letter-spacing:-0.01em;">📊 Student Performance Metrics</h3>', unsafe_allow_html=True)
    
    grid_left, grid_right = st.columns(2)
    with grid_left:
        hours_studied = st.slider("Weekly Study Hours", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("Attendance Rate (%)", 0.0, 100.0, 90.0, 1.0)
    with grid_right:
        sleep_hours = st.slider("Nightly Sleep Hours", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("Last Assessment Score", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Action Trigger Button
_, alignment_col, _ = st.columns([1, 2, 1])
with alignment_col:
    compute_analytics = st.button("RUN PREDICTIVE CORE", type="primary", use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. DIAGNOSTIC RESULTS HUB LAYER
# -----------------------------------------------------------------------------
st.markdown('<div class="analytics-hub-card">', unsafe_allow_html=True)
with st.container(border=True):
    if compute_analytics:
        features_vector = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = predictive_model.predict(features_vector)[0]
            final_index = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#6d28d9; font-weight:700; font-size:0.78rem; letter-spacing:0.2em; text-transform:uppercase;">Analysis Concluded</span>', unsafe_allow_html=True)
            st.metric(label="Calculated Performance Index", value=f"{final_index:.1f}%")
            
            # Semantic Clean Light Alert Panels
            if final_index >= 85:
                st.balloons()
                st.markdown('<div style="background:#f0fdf4; border:1px solid #bbf7d0; color:#15803d; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem;">👑 STATUS: EXCELLENCE MARGIN ENCOUNTERED</div>', unsafe_allow_html=True)
            elif final_index >= 50:
                st.markdown('<div style="background:#eff6ff; border:1px solid #bfdbfe; color:#1d4ed8; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem;">🔵 STATUS: METRIC PROJECTIONS STABLE</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:#fef2f2; border:1px solid #fecaca; color:#b91c1c; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem;">⚠️ WARNING: RISK CRITERIA THRESHOLD BREACHED</div>', unsafe_allow_html=True)
                
        except Exception as prediction_error:
            st.error(f"Execution Discrepancy: {prediction_error}")
    else:
        st.markdown('<p style="color: #94a3b8; margin: 0; font-weight:700; font-size:0.85rem; letter-spacing:0.15em;">CORE IDLE • AWAITING VARIABLE INPUTS</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

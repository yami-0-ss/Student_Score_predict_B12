import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & CYBERPUNK NEON THEMING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Cyber-Edu Analytics Hub",
    page_icon="🔮",
    layout="centered"
)

# High-Contrast Cyberpunk UI Styling Engine (Neon Glows & Dark Glassmorphism)
st.markdown("""
    <style>
    /* Global Cyber Canvas Background */
    .stApp {
        background: radial-gradient(circle at 80% 20%, rgba(236, 72, 153, 0.15) 0%, transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 50%),
                    #05050a; /* True Deep Cyber Black */
    }
    
    /* Neon Text & Label Typography */
    h1, h2, h3, p, label, .stSlider {
        color: #f8fafc !important;
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 700 !important;
        letter-spacing: 0.08em;
        color: #06b6d4 !important; /* Electric Cyan Labels */
        font-size: 0.82rem !important;
        text-transform: uppercase;
    }

    /* Behavioral Feature Matrix - Cyber Glass Panel */
    .feature-matrix-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(10, 10, 20, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(6, 182, 212, 0.2) !important; /* Cyan Tint Border */
        border-radius: 16px !important;
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.05), inset 0 0 15px rgba(6, 182, 212, 0.05) !important;
        padding: 32px !important;
    }

    /* Analytics Hub Glass Container (Neon Pulse Glow) */
    .analytics-hub-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(15, 10, 25, 0.95) 0%, rgba(5, 5, 10, 0.98) 100%) !important;
        border: 1px solid rgba(236, 72, 153, 0.3) !important; /* Magenta Tint Border */
        border-radius: 20px !important;
        box-shadow: 0 0 35px rgba(236, 72, 153, 0.2), inset 0 0 20px rgba(236, 72, 153, 0.1) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Cyber Value Metric Tuning (Electric Pink-to-Purple Gradient) */
    [data-testid="stMetricValue"] {
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #ec4899 0%, #8b5cf6 50%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        filter: drop-shadow(0 2px 10px rgba(236, 72, 153, 0.3));
    }
    
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        font-size: 0.85rem !important;
    }

    /* Futuristic Dashboard Header Architecture */
    .dashboard-title {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 30%, #ec4899 100%);
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
# 3. NEO-KPI INFRASTRUCTURE BAR
# -----------------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">🔮 Cyber-Edu Intelligence Grid</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Real-time student matrix projection environment.</p>', unsafe_allow_html=True)

# System Architecture Insight Badges with colored accent bars
kpi_1, kpi_2, kpi_3 = st.columns(3)
with kpi_1:
    st.markdown('<div style="background: rgba(6, 182, 212, 0.03); padding:16px; border-radius:12px; border: 1px solid rgba(6, 182, 212, 0.15); border-left:4px solid #06b6d4;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Engine Core</span><br><b style="font-size:1.1rem; color:#fff;">K-Nearest Neighbors</b></div>', unsafe_allow_html=True)
with kpi_2:
    st.markdown('<div style="background: rgba(16, 185, 129, 0.03); padding:16px; border-radius:12px; border: 1px solid rgba(16, 185, 129, 0.15); border-left:4px solid #10b981;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Data Inputs</span><br><b style="font-size:1.1rem; color:#fff;">4 Vectors</b></div>', unsafe_allow_html=True)
with kpi_3:
    st.markdown('<div style="background: rgba(236, 72, 153, 0.03); padding:16px; border-radius:12px; border: 1px solid rgba(236, 72, 153, 0.15); border-left:4px solid #ec4899;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">Target Index</span><br><b style="font-size:1.1rem; color:#fff;">Final Grade %</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. FEATURE GRID INPUT LAYER (CYAN ELEMENTS)
# -----------------------------------------------------------------------------
st.markdown('<div class="feature-matrix-card">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 24px; font-size:1.2rem; font-weight:700; color:#f8fafc; letter-spacing:0.02em;">📊 Ingest Behavioral Variables</h3>', unsafe_allow_html=True)
    
    grid_left, grid_right = st.columns(2)
    with grid_left:
        hours_studied = st.slider("Weekly Study Hours", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("Attendance Rate (%)", 0.0, 100.0, 90.0, 1.0)
    with grid_right:
        sleep_hours = st.slider("Nightly Sleep Hours", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("Last Assessment Score", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Action Trigger Button with Custom Theme Styling
_, alignment_col, _ = st.columns([1, 2, 1])
with alignment_col:
    compute_analytics = st.button("RUN PREDICTIVE CORE", type="primary", use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. DIAGNOSTIC HUB LAYER (MAGENTA NEON GLOW EFFECTS)
# -----------------------------------------------------------------------------
st.markdown('<div class="analytics-hub-card">', unsafe_allow_html=True)
with st.container(border=True):
    if compute_analytics:
        features_vector = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = predictive_model.predict(features_vector)[0]
            final_index = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#ec4899; font-weight:700; font-size:0.78rem; letter-spacing:0.2em; text-transform:uppercase;">Projection Complete</span>', unsafe_allow_html=True)
            st.metric(label="Calculated Performance Index", value=f"{final_index:.1f}%")
            
            # Semantic Neon Alert Badges
            if final_index >= 85:
                st.balloons()
                st.markdown('<div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; color:#34d399; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem; box-shadow: 0 0 15px rgba(16,185,129,0.2);">🟢 STATUS: OPTIMAL PERFORMANCES ANTICIPATED</div>', unsafe_allow_html=True)
            elif final_index >= 50:
                st.markdown('<div style="background:rgba(6,182,212,0.1); border:1px solid #06b6d4; color:#22d3ee; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem; box-shadow: 0 0 15px rgba(6,182,212,0.2);">🔵 STATUS: OPERATIONAL TARGETS NOMINAL</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:rgba(239,68,68,0.1); border:1px solid #ef4444; color:#f87171; padding:14px; border-radius:10px; font-weight:700; font-size:0.9rem; box-shadow: 0 0 15px rgba(239,68,68,0.2);">🔴 CRITICAL WARNING: RISK MATRIX THRESHOLD EXCEEDED</div>', unsafe_allow_html=True)
                
        except Exception as prediction_error:
            st.error(f"Execution Discrepancy: {prediction_error}")
    else:
        st.markdown('<p style="color: #64748b; margin: 0; font-weight:700; font-size:0.85rem; letter-spacing:0.15em;">GRID OFFLINE • AWAITING INPUT COMPILATION</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------------------------------
# 1. APPLICATION CONSTANTS & STRUCTURAL THEME ENGINE
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="EduSphere AI Pro Dashboard",
    page_icon="🔮",
    layout="centered"
)

# Advanced CSS injection for multi-color gradients, frosted glass layers, and neon shadows
st.markdown("""
    <style>
    /* Premium Colorful Radial Light/Dark Mashup Canvas */
    .stApp {
        background: radial-gradient(circle at 80% 15%, rgba(139, 92, 246, 0.15) 0%, transparent 45%),
                    radial-gradient(circle at 15% 75%, rgba(16, 185, 129, 0.12) 0%, transparent 40%),
                    #fafafa; /* Clean, ultra-bright backdrop matrix */
    }
    
    /* Typography & Core Label Enhancement */
    h1, h2, h3, p, label, .stSlider {
        color: #1e1b4b !important; /* Deep Indigo-Black for sharp contrast */
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 800 !important;
        letter-spacing: 0.08em;
        color: #8b5cf6 !important; /* Royal Violet Labels */
        font-size: 0.85rem !important;
        text-transform: uppercase;
    }

    /* Input Grid Container - Amethyst Glow Framework */
    .input-matrix-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid rgba(139, 92, 246, 0.15) !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px -5px rgba(139, 92, 246, 0.08), 
                    0 5px 15px -2px rgba(16, 185, 129, 0.04) !important;
        padding: 32px !important;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
    }
    
    /* Micro-lift Hover Dynamics */
    .input-matrix-card [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 25px 45px -10px rgba(139, 92, 246, 0.15) !important;
    }

    /* Diagnostics Output Hub - Emerald-to-Violet Color Accent Frame */
    .diagnostics-hub-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 6px solid #8b5cf6 !important; /* Primary Violet Indicator */
        border-right: 6px solid #10b981 !important; /* Secondary Mint Indicator */
        border-radius: 20px !important;
        box-shadow: 0 20px 30px -5px rgba(0, 0, 0, 0.04) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Performance Value Typography (Multi-Color Chroma Text Gradient) */
    [data-testid="stMetricValue"] {
        font-size: 4rem !important;
        font-weight: 950 !important;
        background: linear-gradient(135deg, #8b5cf6 0%, #d946ef 45%, #10b981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.05em;
        filter: drop-shadow(0 2px 4px rgba(139, 92, 246, 0.1));
    }
    
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        font-size: 0.85rem !important;
        font-weight: 700;
    }

    /* Vibrant Multi-Color Header Layout */
    .dashboard-title {
        font-size: 3.2rem;
        font-weight: 950;
        background: linear-gradient(135deg, #1e1b4b 20%, #8b5cf6 60%, #10b981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        margin-bottom: 2px;
    }
    
    .dashboard-subtitle {
        color: #64748b !important;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
    }
    
    /* Interactive Colorful Custom Button Theme */
    .stButton>button {
        background: linear-gradient(135deg, #8b5cf6 0%, #10b981 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        box-shadow: 0 12px 28px rgba(16, 185, 129, 0.4) !important;
        transform: translateY(-2px) scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MACHINE LEARNING ENGINE INGESTION
# -----------------------------------------------------------------------------
@st.cache_resource
def load_predictive_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    predictive_model = load_predictive_model()
except Exception as error:
    st.error(f"❌ Error initializing analytical core: {error}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. INTERACTIVE TITLE & CHROMATIC KPI BADGE SECTION
# -----------------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">✨ EduSphere™ Intelligence Grid</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">🔮 Predictive performance node tracking behavioral variables in real-time.</p>', unsafe_allow_html=True)

# Dynamic Architecture Status Badges
kpi_left, kpi_mid, kpi_right = st.columns(3)
with kpi_left:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:14px; border: 1px solid rgba(139, 92, 246, 0.12); border-left:4px solid #8b5cf6;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">🧠 Core Core</span><br><b style="font-size:1.05rem; color:#1e1b4b;">KNN Regressor</b></div>', unsafe_allow_html=True)
with kpi_mid:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:14px; border: 1px solid rgba(16, 185, 129, 0.12); border-left:4px solid #10b981;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">🧬 Footprint</span><br><b style="font-size:1.05rem; color:#1e1b4b;">4 Dimensions</b></div>', unsafe_allow_html=True)
with kpi_right:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:14px; border: 1px solid rgba(217, 70, 239, 0.12); border-left:4px solid #d946ef;"><span style="color:#64748b; font-size:0.75rem; text-transform:uppercase; font-weight:700; letter-spacing:0.05em;">🎯 Target Index</span><br><b style="font-size:1.05rem; color:#1e1b4b;">Final Grade %</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. DATA COMPILATION PANEL (2x2 CARD WITH INTEGRATED EMOJIS)
# -----------------------------------------------------------------------------
st.markdown('<div class="input-matrix-card">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 24px; font-size:1.25rem; font-weight:800; color:#1e1b4b; letter-spacing:-0.01em;">📊 Calibrate Student Input Vectors</h3>', unsafe_allow_html=True)
    
    column_left, column_right = st.columns(2)
    with column_left:
        hours_studied = st.slider("📚 Weekly Study Duration", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("🏫 Institutional Attendance (%)", 0.0, 100.0, 90.0, 1.0)
    with column_right:
        sleep_hours = st.slider("🌙 Nightly Sleep Recovery", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("📝 Historical Assessment Grade", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Trigger Engine Button
_, alignment_block, _ = st.columns([1, 2, 1])
with alignment_block:
    process_calculation = st.button("🚀 EXECUTE PREDICTIVE CORE", type="primary", use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. DIAGNOSTIC RESULTS HUB PANEL
# -----------------------------------------------------------------------------
st.markdown('<div class="diagnostics-hub-card">', unsafe_allow_html=True)
with st.container(border=True):
    if process_calculation:
        data_vector = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = predictive_model.predict(data_vector)[0]
            grade_quotient = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#8b5cf6; font-weight:800; font-size:0.8rem; letter-spacing:0.22em; text-transform:uppercase;">⚡ Analytics Run Success</span>', unsafe_allow_html=True)
            st.metric(label="Projected Academic Score Quotient", value=f"{grade_quotient:.1f}%")
            
            # Semantic Context Alerts with Custom Chromatic Layout Borders
            if grade_quotient >= 85:
                st.balloons()
                st.markdown('<div style="background:#f0fdf4; border:1px solid #bbf7d0; color:#166534; padding:14px; border-radius:12px; font-weight:800; font-size:0.92rem;">🏆 TIER-ONE EXCELLENCE MARGIN ANTICIPATED • KEEP PACE</div>', unsafe_allow_html=True)
            elif grade_quotient >= 50:
                st.markdown('<div style="background:#eff6ff; border:1px solid #bfdbfe; color:#1e40af; padding:14px; border-radius:12px; font-weight:800; font-size:0.92rem;">📈 SYSTEM METRIC RUN STABLE • PASS STATUS SECURED</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:#fef2f2; border:1px solid #fecaca; color:#991b1b; padding:14px; border-radius:12px; font-weight:800; font-size:0.92rem;">🚨 CRITICAL METRIC ALERT: RISK INTERVENTION GAP DETECTED</div>', unsafe_allow_html=True)
                
        except Exception as prediction_error:
            st.error(f"❌ Execution Fault Interception: {prediction_error}")
    else:
        st.markdown('<p style="color: #94a3b8; margin: 0; font-weight:800; font-size:0.85rem; letter-spacing:0.18em; text-transform:uppercase;">💤 Matrix Idle • Awaiting Target Command Input</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

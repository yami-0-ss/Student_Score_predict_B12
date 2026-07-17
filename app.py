import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="EduAnalytics Pro Dashboard",
    page_icon="⚡",
    layout="centered"
)

# Advanced UI Custom Dashboard Styling
st.markdown("""
    <style>
    /* Global Dashboard Theme */
    .stApp {
        background: radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(16, 185, 129, 0.1) 0%, transparent 50%),
                    #0f172a; /* Sleek Dark Slate Slate */
    }
    
    /* Typography Overrides */
    h1, h2, h3, p, label, .stSlider {
        color: #f8fafc !important;
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 600 !important;
        letter-spacing: 0.05em;
        color: #94a3b8 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase;
    }

    /* Input Matrix Glass Card */
    .input-matrix [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5) !important;
        padding: 32px !important;
    }

    /* Dynamic Output Panel with custom soft glow */
    .dashboard-hub [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 24px !important;
        box-shadow: 0 0 30px rgba(99, 102, 241, 0.15), inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Metric Values Tuning */
    [data-testid="stMetricValue"] {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.06em;
    }
    
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-size: 0.85rem !important;
    }

    /* Custom Title Styling */
    .dashboard-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.04em;
        margin-bottom: 0px;
    }
    
    .dashboard-subtitle {
        color: #64748b !important;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }

    /* Modernizing Streamlit Sliders */
    div[data-testid="stSlider"]  {
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Cache model load
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

# Header Division
st.markdown('<h1 class="dashboard-title">⚡ EduAnalytics Intelligence Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Predictive student monitoring environment driven by machine learning.</p>', unsafe_allow_html=True)

# Grid columns to layout indicators beautifully before user inputs
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:15px; border-radius:12px; border-left:4px solid #6366f1;"><span style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Model Core</span><br><b style="font-size:1.1rem; color:#fff;">K-Nearest Neighbors</b></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:15px; border-radius:12px; border-left:4px solid #10b981;"><span style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Feature Count</span><br><b style="font-size:1.1rem; color:#fff;">4 Dimensions</b></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background: rgba(255,255,255,0.03); padding:15px; border-radius:12px; border-left:4px solid #f59e0b;"><span style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Target Metric</span><br><b style="font-size:1.1rem; color:#fff;">Final Grade %</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ----------------- MAIN INPUT PANEL -----------------
st.markdown('<div class="input-matrix">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 20px; font-size:1.2rem; color:#f1f5f9;">📊 Student Behavior Vector</h3>', unsafe_allow_html=True)
    
    # Using 2x2 layout system within the container for cleaner look
    slot1, slot2 = st.columns(2)
    with slot1:
        hours_studied = st.slider("Weekly Study Hours", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("Attendance Rate (%)", 0.0, 100.0, 90.0, 1.0)
    with slot2:
        sleep_hours = st.slider("Nightly Sleep Hours", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("Last Assessment Score", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Action Execution Layer
_, center_col, _ = st.columns([1, 2, 1])
with center_col:
    predict_clicked = st.button("RUN PREDICTIVE ENGINE", type="primary", use_container_width=True)

st.write("")

# ----------------- ANALYTICS HUB OUTPUT -----------------
st.markdown('<div class="dashboard-hub">', unsafe_allow_html=True)
with st.container(border=True):
    if predict_clicked:
        input_data = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            # Predict
            prediction = model.predict(input_data)[0]
            display_score = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#818cf8; font-weight:700; font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase;">Analysis Concluded</span>', unsafe_allow_html=True)
            
            st.metric(label="Calculated Performance Index", value=f"{display_score:.1f}%")
            
            # Dynamic grading badge styling based on prediction outcome
            if display_score >= 85:
                st.balloons()
                st.markdown('<div style="background:rgba(16,185,129,0.15); border:1px solid #10b981; color:#34d399; padding:12px; border-radius:10px; font-weight:600;">👑 OUTSTANDING OUTCOME TIERS EXPECTED</div>', unsafe_allow_html=True)
            elif display_score >= 50:
                st.markdown('<div style="background:rgba(59,130,246,0.15); border:1px solid #3b82f6; color:#60a5fa; padding:12px; border-radius:10px; font-weight:600;">📈 NOMINAL PASS PERFORMANCE ASSURED</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:rgba(239,68,68,0.15); border:1px solid #ef4444; color:#f87171; padding:12px; border-radius:10px; font-weight:600;">⚠️ ATTENTION REQUIRED: CRITICAL FAILURE RISK</div>', unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Processing Fault: {e}")
    else:
        st.markdown('<p style="color: #475569; margin: 0; font-weight:500; letter-spacing:0.05em;">AWAITING COMMAND INGESTION • TARGET MATRIX STANDING BY</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import pickle
import numpy as np

# -----------------------------------------------------------------------------
# 1. APPLICATION CONSTANTS & CUTE PASTEL THEME ENGINE
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Magic Grade Garden",
    page_icon="🌸",
    layout="centered"
)

# Adorable CSS injection for pastel pinks, mints, cartoon text, and soft cloud shadows
st.markdown("""
    <style>
    /* Magical Garden Soft Pastel Background Grid */
    .stApp {
        background: radial-gradient(circle at 90% 15%, rgba(255, 182, 193, 0.4) 0%, transparent 50%),
                    radial-gradient(circle at 15% 75%, rgba(192, 250, 220, 0.4) 0%, transparent 50%),
                    #fffdf9; /* Creamy warm background vanilla */
    }
    
    /* Cute Cartoon Style Typography & Labels */
    h1, h2, h3, p, label, .stSlider {
        color: #4A3E3D !important; /* Sweet chocolate brown for clean contrast */
        font-family: 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif !important;
    }
    
    .stSlider label, .stNumberInput label {
        font-weight: 800 !important;
        letter-spacing: 0.02em;
        color: #D4A5B8 !important; /* Sweet Strawberry Pink Labels */
        font-size: 0.9rem !important;
    }

    /* Input Grid Container - Soft Fluffy Cloud Panel */
    .input-matrix-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 3px dashed #FBCFE8 !important; /* Pastel Pink Dashed Border */
        border-radius: 24px !important;
        box-shadow: 0 12px 24px rgba(255, 182, 193, 0.2) !important;
        padding: 30px !important;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    /* Fun Bounce Hover Effect */
    .input-matrix-card [data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px) scale(1.01);
    }

    /* Diagnostics Output Hub - Sweet Blossom Border Panel */
    .diagnostics-hub-card [data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff !important;
        border: 4px solid #D8B4FE !important; /* Pastel Purple border */
        border-radius: 24px !important;
        box-shadow: 0 15px 30px rgba(216, 180, 254, 0.25) !important;
        padding: 35px !important;
        text-align: center;
    }

    /* Magical Value Typography (Dreamy Pastel Rainbow Gradient) */
    [data-testid="stMetricValue"] {
        font-size: 4.2rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #FF80AB 0%, #BA68C8 50%, #4DB6AC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
        filter: drop-shadow(2px 2px 0px rgba(255,255,255,1));
    }
    
    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        letter-spacing: 0.05em;
        font-size: 0.95rem !important;
        font-weight: 700;
    }

    /* Adorable Header Layout Styles */
    .dashboard-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #FF6B8B 0%, #B970FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
    }
    
    .dashboard-subtitle {
        color: #8A7E7C !important;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
    }
    
    /* Super Cute Pastel Sparkle Button Theme */
    .stButton>button {
        background: linear-gradient(135deg, #FF8A9F 0%, #A78BFA 100%) !important;
        color: white !important;
        border: 2px solid #ffffff !important;
        border-radius: 50px !important; /* Pill shape */
        padding: 12px 30px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 8px 20px rgba(255, 138, 159, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        box-shadow: 0 12px 25px rgba(167, 139, 250, 0.5) !important;
        transform: translateY(-3px) scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MODEL ENGINE INGESTION
# -----------------------------------------------------------------------------
@st.cache_resource
def load_predictive_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

try:
    predictive_model = load_predictive_model()
except Exception as error:
    st.error(f"🔮 Oh no! The magic engine got tangled in vines: {error}")
    st.stop()

# -----------------------------------------------------------------------------
# 3. INTERACTIVE CUTE TITLE & PASTEL KPI MINI CARDS
# -----------------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">🌸 Magic Grade Garden ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Grow your habits, water your schedule, and let your predictions bloom beautifully! 🦄🌷</p>', unsafe_allow_html=True)

# Cute Floral Status Badges
kpi_left, kpi_mid, kpi_right = st.columns(3)
with kpi_left:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:18px; border: 2px solid #FDE68A; text-align:center;"><span style="font-size:1.6rem;">🧚‍♀️</span><br><b style="font-size:0.9rem; color:#4A3E3D;">Garden Pixie</b><br><small style="color:#8A7E7C;">KNN Core</small></div>', unsafe_allow_html=True)
with kpi_mid:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:18px; border: 2px solid #A7F3D0; text-align:center;"><span style="font-size:1.6rem;">🧪</span><br><b style="font-size:0.9rem; color:#4A3E3D;">4 Spells</b><br><small style="color:#8A7E7C;">Features</small></div>', unsafe_allow_html=True)
with kpi_right:
    st.markdown('<div style="background: #ffffff; padding:16px; border-radius:18px; border: 2px solid #FBCFE8; text-align:center;"><span style="font-size:1.6rem;">🎯</span><br><b style="font-size:0.9rem; color:#4A3E3D;">Final Goal</b><br><small style="color:#8A7E7C;">Grade Outcome</small></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# -----------------------------------------------------------------------------
# 4. DATA COMPILATION PANEL (CUTE SLIDERS & CARTOON DECORATIONS)
# -----------------------------------------------------------------------------
st.markdown('<div class="input-matrix-card">', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<h3 style="margin-top:0; margin-bottom: 24px; font-size:1.3rem; font-weight:900; text-align:center; color:#4A3E3D;">🌱 Water Your Habit Seeds 🌾</h3>', unsafe_allow_html=True)
    
    column_left, column_right = st.columns(2)
    with column_left:
        hours_studied = st.slider("📚 Weekly Study Journey", 0.0, 100.0, 15.0, 0.5)
        attendance_percent = st.slider("🏫 Happy School Days (%)", 0.0, 100.0, 90.0, 1.0)
    with column_right:
        sleep_hours = st.slider("🌙 Sweet Dream Hours", 0.0, 24.0, 7.5, 0.5)
        previous_scores = st.number_input("📝 Last Magical Quiz Score", 0.0, 100.0, 78.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Adorable Trigger Button
_, alignment_block, _ = st.columns([1, 2, 1])
with alignment_block:
    process_calculation = st.button("✨ CAST FLOWER SPELL! ✨", type="primary", use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. DIAGNOSTIC RESULTS HUB PANEL (BLOOMING EFFECTS)
# -----------------------------------------------------------------------------
st.markdown('<div class="diagnostics-hub-card">', unsafe_allow_html=True)
with st.container(border=True):
    if process_calculation:
        data_vector = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
        
        try:
            prediction = predictive_model.predict(data_vector)[0]
            grade_quotient = min(max(prediction, 0.0), 100.0)
            
            st.markdown('<span style="color:#BA68C8; font-weight:800; font-size:0.9rem; letter-spacing:0.05em;">🌸 Your Flower Has Bloomed! 🌸</span>', unsafe_allow_html=True)
            st.metric(label="Expected Score Power!", value=f"{grade_quotient:.1f}%")
            
            # Semantic Adorable Alerts based on Grades
            if grade_quotient >= 85:
                st.balloons()
                st.markdown('<div style="background:#FDF2F8; border:2px dashed #F472B6; color:#9D174D; padding:16px; border-radius:16px; font-weight:800; font-size:1rem;">👑🌟 WOO-HOO! You are an Absolute Superstar Flower! Standing proud in the top tier! 🎉</div>', unsafe_allow_html=True)
            elif grade_quotient >= 50:
                st.markdown('<div style="background:#ECFDF5; border:2px dashed #34D399; color:#065F46; padding:16px; border-radius:16px; font-weight:800; font-size:1rem;">🍀🧸 Yay! Doing great! Your little garden sprout is passing and growing smoothly! Keep going!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="background:#FFF5F5; border:2px dashed #F87171; color:#9B1C1C; padding:16px; border-radius:16px; font-weight:800; font-size:1rem;">🧸⚠️ Oh no, sleepy seeds! The garden needs a little extra water and attention. Let\'s try reviewing habits! 💕</div>', unsafe_allow_html=True)
                
        except Exception as prediction_error:
            st.error(f"💔 Pixie Dust Misplaced: {prediction_error}")
    else:
        st.markdown('<p style="color: #A1A1AA; margin: 0; font-weight:800; font-size:0.9rem; letter-spacing:0.05em;">💤 The Pixies are napping... adjust your sliders and cast the spell! 🧚‍♀️🍄</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

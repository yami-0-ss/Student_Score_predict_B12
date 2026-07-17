import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for modern vertical card layout, color theme, and shadows
# NOTE: changed parameter to unsafe_allow_html=True to fix the TypeError
st.markdown("""
    <style>
    /* Main container background setup */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Custom style block for the vertical input card */
    .input-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1);
        border: 1px solid #e9ecef;
        margin-bottom: 24px;
    }
    
    /* Custom style block for the results display card */
    .result-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #4F46E5; /* Indigo accent indicator */
        margin-top: 12px;
    }
    
    /* Header typography color tuning */
    h1, h2, h3 {
        color: #1e293b !important;
        font-weight: 700;
    }
    
    /* Subtext and captions */
    .subtext {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load the trained model
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

# Title Section
st.title("🎓 Student Performance Predictor")
st.markdown(
    '<p class="subtext">Predict final academic scores cleanly using data-driven insights. Fill out the characteristics below inside our structured layout panel.</p>', 
    unsafe_allow_html=True
)

# Vertical Layout Section 1: Inputs grouped within a distinct visual card block
st.markdown('<h3>📊 Academic Metrics Input</h3>', unsafe_allow_html=True)

# Opening the custom container div via markdown
st.markdown('<div class="input-card">', unsafe_allow_html=True)

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
    "Previous Exam Score", 
    min_value=0.0, max_value=100.0, value=75.0, step=1.0
)

# Closing the custom container div
st.markdown('</div>', unsafe_allow_html=True)

# Center alignment utility for the primary interaction button
_, col_btn, _ = st.columns([1, 2, 1])
with col_btn:
    predict_clicked = st.button("Calculate Predicted Score", type="primary", use_container_width=True)

st.write("") # Spacer

# Vertical Layout Section 2: Results Panel
if predict_clicked:
    input_data = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    with st.spinner("Processing metrics through the model..."):
        try:
            prediction = model.predict(input_data)[0]
            display_score = min(max(prediction, 0.0), 100.0)
            
            # Opening the custom output container block with an accent layout border
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<h3>🎯 Analysis Outcome</h3>', unsafe_allow_html=True)
            
            st.metric(
                label="Predicted Final Score Metric", 
                value=f"{display_score:.2f} / 100"
            )
            
            # Performance Tiers Context Output
            if display_score >= 85:
                st.balloons()
                st.success("🌟 **Outstanding Projection!** Current baseline habits align with tier-one outcomes.")
            elif display_score >= 50:
                st.info("👍 **Steady Track.** Parameters point to a passing tier. Incrementing attendance or focus hours will elevate target limits.")
            else:
                st.warning("⚠️ **Performance Risk Detected.** Predicted targets fall beneath criteria baselines. Review scheduling shifts.")
                
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"An unexpected tracking discrepancy surfaced during execution: {e}")
else:
    # Shadow box template placeholder when state is resting
    st.markdown('<div class="result-card" style="border-left: 5px solid #cbd5e1;"><p style="color: #94a3b8; margin: 0; text-align: center;">Awaiting processing inputs. Modify values above and trigger calculation to populate.</p></div>', unsafe_allow_html=True)

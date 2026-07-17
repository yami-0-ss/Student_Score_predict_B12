import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS targeting Streamlit's native container structures cleanly
st.markdown("""
    <style>
    /* Application overall light background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Injecting drop-shadow, border-radius, and modern colors onto the native st.container blocks */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #e9ecef !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        padding: 20px !important;
        margin-bottom: 20px !important;
    }

    /* Target the first container inside the results area to give it an accent-colored left indicator */
    .results-section [data-testid="stVerticalBlockBorderWrapper"] {
        border-left: 5px solid #4F46E5 !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Global layout adjustments for crisp headers */
    h1, h2, h3 {
        color: #1e293b !important;
        font-weight: 700 !important;
    }
    
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

# Title Header Section
st.title("🎓 Student Performance Predictor")
st.markdown(
    '<p class="subtext">Predict final academic scores cleanly using data-driven insights. Fill out the characteristics below inside our structured layout panel.</p>', 
    unsafe_allow_html=True
)

st.markdown('<h3>📊 Academic Metrics Input</h3>', unsafe_allow_html=True)

# Vertical Layout Section 1: The Input Card Component
with st.container(border=True):
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

# Center alignment layout setup for the execution button
_, col_btn, _ = st.columns([1, 2, 1])
with col_btn:
    predict_clicked = st.button("Calculate Predicted Score", type="primary", use_container_width=True)

st.write("") # Layout Spacer

# Vertical Layout Section 2: Results Display Panel
# Wrapping results inside a dedicated HTML structural div so custom CSS applies only here
st.markdown('<div class="results-section">', unsafe_allow_html=True)

if predict_clicked:
    input_data = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])
    
    with st.spinner("Processing metrics through the model..."):
        try:
            prediction = model.predict(input_data)[0]
            display_score = min(max(prediction, 0.0), 100.0)
            
            with st.container(border=True):
                st.markdown('<h3>🎯 Analysis Outcome</h3>', unsafe_allow_html=True)
                
                st.metric(
                    label="Predicted Final Score Metric", 
                    value=f"{display_score:.2f} / 100"
                )
                
                # Context messaging depending on results
                if display_score >= 85:
                    st.balloons()
                    st.success("🌟 **Outstanding Projection!** Current baseline habits align with tier-one outcomes.")
                elif display_score >= 50:
                    st.info("👍 **Steady Track.** Parameters point to a passing tier. Incrementing attendance or focus hours will elevate target limits.")
                else:
                    st.warning("⚠️ **Performance Risk Detected.** Predicted targets fall beneath criteria baselines. Review scheduling shifts.")
                    
        except Exception as e:
            st.error(f"An unexpected tracking discrepancy surfaced during execution: {e}")
else:
    # A resting state card placeholder
    with st.container(border=True):
        st.markdown('<p style="color: #94a3b8; margin: 0; text-align: center;">Awaiting processing inputs. Modify values above and trigger calculation to populate.</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

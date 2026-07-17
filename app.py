import streamlit as st
import pickle
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🔮",
    layout="centered"
)

# 2. Custom CSS for Dark Theme, Gradients, and Glow Shadows
st.markdown("""
<style>
    /* Dark background for the entire app */
    .stApp {
        background-color: #0f172a;
    }
    
    /* Main title styling */
    h1 {
        color: #f8fafc !important; 
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 0 2px 10px rgba(255, 255, 255, 0.1);
    }

    /* Subtitle styling */
    .subtitle {
        color: #94a3b8;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Target the form container to create a dark 'Card' with a glowing shadow */
    div[data-testid="stForm"] {
        background-color: #1e293b;
        border-radius: 20px;
        padding: 30px;
        border: 1px solid #334155;
        box-shadow: 0 10px 40px rgba(99, 102, 241, 0.15); /* Soft indigo glow */
    }

    /* Style the input labels to ensure they are readable on dark backgrounds */
    label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
    }

    /* Gradient Submit Button with strong shadow */
    button[kind="primary"] {
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4) !important; /* Pink/Purple glow */
    }
    
    button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.6) !important;
    }

    /* Neon Result Card */
    .result-card {
        background-color: #1e293b;
        border-radius: 16px;
        padding: 30px;
        border: 1px solid #06b6d4; /* Cyan border */
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.3); /* Cyan neon glow */
        text-align: center;
        margin-top: 30px;
    }
    
    .result-title {
        color: #94a3b8;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }
    
    .result-value {
        background: linear-gradient(to right, #22d3ee, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
        text-shadow: 0 0 20px rgba(34, 211, 238, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. Load the Model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# 4. Header Section
st.title("🔮 AI Score Predictor")
st.markdown('<div class="subtitle">Input student metrics to generate a predictive analysis.</div>', unsafe_allow_html=True)

# 5. Vertical Layout inside the Dark Styled Form
with st.form("prediction_form"):
    
    # Inputs stacked purely vertically
    hours_studied = st.number_input(
        "Hours Studied (per day/week)", 
        min_value=0.0, max_value=24.0, value=5.0, step=0.5
    )
    
    sleep_hours = st.number_input(
        "Sleep Hours (per day)", 
        min_value=0.0, max_value=24.0, value=8.0, step=0.5
    )
    
    attendance_percent = st.number_input(
        "Attendance (%)", 
        min_value=0.0, max_value=100.0, value=85.0, step=1.0
    )
    
    previous_scores = st.number_input(
        "Previous Scores", 
        min_value=0.0, max_value=100.0, value=75.0, step=1.0
    )
    
    st.write("") # Spacer
    
    # Submit button
    submitted = st.form_submit_button("Run Prediction Engine", type="primary", use_container_width=True)

# 6. Prediction Logic & Neon Output
if submitted:
    input_data = pd.DataFrame([[
        hours_studied, 
        sleep_hours, 
        attendance_percent, 
        previous_scores
    ]], columns=['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores'])
    
    try:
        prediction = model.predict(input_data)
        
        # Display the custom HTML result card with cyan neon glow and gradient text
        st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Projected Final Score</div>
                <div class="result-value">{prediction[0]:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Prediction Error: {e}")

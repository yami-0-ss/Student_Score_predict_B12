import streamlit as st
import pickle
import numpy as np

# Set up page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

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

# Application Title & Description
st.title("🎓 Student Performance Predictor")
st.markdown("""
Predict a student's final score based on their daily habits and historical performance. 
Adjust the inputs in the sidebar to recalculate.
""")

st.divider()

# Layout: Inputs on the Sidebar, Results on the Main Panel
st.sidebar.header("📋 Input Features")

hours_studied = st.sidebar.slider(
    "Hours Studied (per week)", 
    min_value=0.0, max_value=100.0, value=10.0, step=0.5
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours (per night)", 
    min_value=0.0, max_value=24.0, value=7.0, step=0.5
)

attendance_percent = st.sidebar.slider(
    "Attendance Percentage (%)", 
    min_value=0.0, max_value=100.0, value=85.0, step=1.0
)

previous_scores = st.sidebar.number_input(
    "Previous Exam Score", 
    min_value=0.0, max_value=100.0, value=75.0, step=1.0
)

# Main panel formatting
st.subheader("Prediction Results")

# Prepare input array for the model
input_data = np.array([[hours_studied, sleep_hours, attendance_percent, previous_scores]])

# Predict button
if st.button("Predict Score", type="primary"):
    with st.spinner("Calculating performance metric..."):
        try:
            prediction = model.predict(input_data)[0]
            
            # Bound prediction reasonably if the model extrapolates out of a 0-100 range
            display_score = min(max(prediction, 0.0), 100.0)
            
            # Display result inside a metric block
            st.success("Calculation complete!")
            st.metric(
                label="Predicted Final Score", 
                value=f"{display_score:.2f} / 100"
            )
            
            # Add context based on the score tier
            if display_score >= 85:
                st.balloons()
                st.info("🌟 Outstanding projection! The current habits indicate excellent performance.")
            elif display_score >= 50:
                st.info("👍 On track to pass. Consider increasing study hours or attendance to boost results further.")
            else:
                st.warning("⚠️ Warning: The predicted score falls below average. Review study habits or attendance.")
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
else:
    st.info("Click the 'Predict Score' button above to see the results.")

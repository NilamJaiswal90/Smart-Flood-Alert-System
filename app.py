# app.py
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model_nasa.pkl", "rb"))

# --- Page Config ---
st.set_page_config(
    page_title="Smart Flood Alert System",
    page_icon="🌧️",
    layout="centered"
)

# --- Custom Styling ---
def local_css():
    st.markdown("""
        <style>
        .main {
            background-color: #f1f8ff;
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #005f99;
        }
        .stTextInput>div>input {
            border-radius: 8px;
            height: 3em;
        }
        .output-box {
            background-color: #e3f2fd;
            border-left: 5px solid #0288d1;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 500;
        }
        .danger {
            background-color: #ffebee;
            border-left: 5px solid #c62828;
            color: #b71c1c;
        }
        .safe {
            background-color: #e8f5e9;
            border-left: 5px solid #2e7d32;
            color: #1b5e20;
        }
        footer {
            visibility: hidden;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3222/3222800.png", width=100)
st.sidebar.title("ℹ️ How to Use")
st.sidebar.markdown("""
1. Enter rainfall data for the past 1 and 2 days.
2. Click **Check Flood Risk**.
3. Get real-time flood prediction result.  
""")
st.sidebar.markdown("---")
st.sidebar.markdown("🔍 Data collected by NASA API.")

# --- Main App ---
st.title("🌧️ Smart Flood Alert System")
st.markdown("**Protect your area with early flood prediction.**")
st.markdown("Enter rainfall measurements below:")

# --- Input Form ---
with st.form("flood_form"):
    col1, col2 = st.columns(2)
    with col1:
        rainfall_1d = st.number_input("1-Day Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")
    with col2:
        rainfall_2d = st.number_input("2-Day Cumulative Rainfall (mm)", min_value=0.0, step=0.1, format="%.1f")

    submitted = st.form_submit_button("💧 Check Flood Risk")

# --- Prediction ---
if submitted:
    features = np.array([[rainfall_1d, rainfall_2d]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.markdown('<div class="output-box danger">🚨 <strong>Flood risk detected!</strong><br>Please take precautions and stay informed.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="output-box safe">✅ <strong>No flood risk today.</strong><br>Stay safe and monitor regularly.</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<br><br>
<hr>
<div style="text-align:center; color: grey;">
    Smart Flood Alert System © 2025 | Built By Vaibhavi And Team
</div>
""", unsafe_allow_html=True)

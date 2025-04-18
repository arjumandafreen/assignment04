import streamlit as st

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="wide")

# Custom styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 3em;
        color: #4CAF50;
        margin-bottom: 0.2em;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        margin-bottom: 2em;
    }
    .stButton button {
        background-color: black;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .result-box {
        background-color: black;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.2em;
        border: 2px solid #4CAF50;
        margin-top: 20px;
        color: white; /* Fix: make text visible */
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<h1 style="color:#4CAF50;">💪 BMI Calculator</h1>', unsafe_allow_html=True)
st.sidebar.image("bmi.png", use_container_width=True)

# Title and Description
st.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">📏 Enter your weight (kg) and height (feet) to check your Body Mass Index.</p>', unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Input fields
    weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, step=0.1)
    height_feet = st.number_input("📐 Enter your height (feet)", min_value=0.0, step=0.1)

    # BMI Calculation Function
    def calculate_bmi(weight, height_feet):
        height_meters = height_feet * 0.3048
        bmi = weight / (height_meters ** 2)
        return bmi

    if st.button("✨ Calculate BMI"):
        if weight > 0 and height_feet > 0:
            bmi = calculate_bmi(weight, height_feet)

            # Determine category
            if bmi < 18.5:
                category = "🟡 <strong>Category:</strong> Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "🟢 <strong>Category:</strong> Normal weight"
            elif 25 <= bmi < 29.9:
                category = "🟠 <strong>Category:</strong> Overweight"
            else:
                category = "🔴 <strong>Category:</strong> Obese"

            # Display result in one go
            st.markdown(
                f"<div class='result-box'>"
                f"📊 <strong>Your BMI is:</strong> {bmi:.2f}<br>{category}"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.error("🚫 Please enter valid weight and height values.")

import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="House of Mobile", page_icon="📱", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    .main {
        background-color: #1a1a1a;
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.05);
        margin: 1rem auto;
        max-width: 1000px;
    }
    .big-title {
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        color: #00ffcc;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        color: #dddddd;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .footer {
        text-align: center;
        font-size: 1rem;
        color: #aaa;
        padding: 2rem 0;
        border-top: 1px solid #333;
        margin-top: 3rem;
    }
    .footer span {
        color: #00ffcc;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📱 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🛒 Shop", "📞 Contact"])

# Home Page
if page == "🏠 Home":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Welcome to House of Mobile</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Your One-Stop Mobile Phone Online Shop</p>", unsafe_allow_html=True)
    
    # ✅ Updated line to avoid warning
    st.image("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9", use_container_width=True, caption="Explore Latest Mobiles")
    
    st.write("""
        Looking for the latest mobile phones at the best prices? You've come to the right place!
        Navigate through our online store to discover top brands and great deals.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Shop Page
elif page == "🛒 Shop":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Available Mobiles</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Best deals just for you!</p>", unsafe_allow_html=True)

    # Product listing
    phones = [
        {"name": "iPhone 14 Pro Max", "price": "Rs. 389,999"},
        {"name": "Samsung Galaxy S23 Ultra", "price": "Rs. 359,999"},
        {"name": "Xiaomi 13 Pro", "price": "Rs. 234,999"},
        {"name": "Infinix Zero 30", "price": "Rs. 74,999"},
        {"name": "Tecno Camon 20", "price": "Rs. 59,999"},
        {"name": "Vivo Y22", "price": "Rs. 48,000"},
    ]

    for phone in phones:
        st.markdown(f"**{phone['name']}** — 📱 Price: `{phone['price']}`")

    st.markdown("</div>", unsafe_allow_html=True)

# Contact Page
elif page == "📞 Contact":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>We'd love to assist you!</p>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you! We'll respond as soon as possible.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 class='subtitle'>Quick Price Reference 📋</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Realme C55**")
        st.markdown("**Oppo F21 Pro**")
        st.markdown("**iPhone 11**")
    with col2:
        st.markdown("Rs. 45,999")
        st.markdown("Rs. 88,999")
        st.markdown("Rs. 189,999")

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        Made with <span>💚</span> by <span>Arjumand</span> — Powered by <strong>Streamlit</strong>
    </div>
""", unsafe_allow_html=True)

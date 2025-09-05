import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

# Custom CSS with cartoon rain/river background
st.markdown("""
    <style>
        .main {
            background: url('https://i.ibb.co/7j1tJ6h/cartoon-rain-river.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        .stButton>button {
            border-radius: 12px;
            background-color: #0077b6;
            color: white;
            font-size: 16px;
            padding: 0.6em 1.2em;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #023e8a;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            border-radius: 8px;
        }
        h1, h2, h3 {
            color: #03045e;
            text-shadow: 1px 1px 2px #90e0ef;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Converter Options")
choice = st.sidebar.radio("Select a Converter", ["🌡 Temperature", "⚖️ Weight", "💰 Currency (Live)"])

st.title("🔁 Stylish Unit Converter 🚀")

# ---- Temperature Converter ----
if choice == "🌡 Temperature":
    st.subheader("🌡 Temperature Converter")
    temp = st.number_input("Enter Temperature", value=0.0)
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])

    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = temp * 9/5 + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (temp - 32) * 5/9
    else:
        result = temp

    st.success(f"✅ {temp} {from_unit} = {round(result,2)} {to_unit}")

# ---- Weight Converter ----
elif choice == "⚖️ Weight":
    st.subheader("⚖️ Weight Converter")
    weight = st.number_input("Enter Weight", value=0.0)
    from_unit = st.selectbox("From", ["Kilogram", "Gram", "Pound"])
    to_unit = st.selectbox("To", ["Kilogram", "Gram", "Pound"])

    factors = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462}
    result = weight * factors[to_unit] / factors[from_unit]
    st.success(f"✅ {weight} {from_unit} = {round(result,2)} {to_unit}")

# ---- Currency Converter ----
elif choice == "💰 Currency (Live)":
    st.subheader("💰 Currency Converter (Live Rates)")
    amount = st.number_input("Enter Amount", value=1.0)
    from_curr = st.selectbox("From", ["INR", "USD", "EUR"])
    to_curr = st.selectbox("To", ["INR", "USD", "EUR"])

    if st.button("🔄 Convert"):
        try:
            url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}"
            res = requests.get(url).json()
            result = res["result"]
            st.success(f"✅ {amount} {from_curr} = {round(result, 2)} {to_curr}")
        except Exception:
            st.error("❌ Could not fetch live rates. Check internet connection.")

import streamlit as st
import requests

st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Data Source")
mode = st.sidebar.radio("Choose Mode:", ["Live API", "Manual Entry (Backup)"])
AV_KEY = "0SYM2E4LAG7AHT2K"

def get_live_data():
    # ... (Keep your existing get_macro_data code here) ...
    return None, "Daily Limit Reached"

# --- LOGIC ---
if mode == "Manual Entry (Backup)":
    st.info("Manual Mode: Enter prices from Google/Yahoo to calculate ratio.")
    m_btc = st.number_input("Current Bitcoin Price ($)", value=65000.0)
    m_gold = st.number_input("Current Gold Price ($)", value=5100.0)
    btc_p, gold_p = m_btc, m_gold
    err = None
else:
    # Use the live function we built earlier
    data_bundle, err = get_macro_data()
    if data_bundle:
        btc_p, gold_p = data_bundle
    else:
        btc_p, gold_p = None, None

# --- DISPLAY ---
if btc_p and gold_p:
    ratio = btc_p / gold_p
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL!")
    else:
        st.info(f"HOLD: Target 11.0. (Currently {ratio:.2f})")
else:
    st.warning(f"⚠️ API Limit Reached. Switch to 'Manual Entry' in the sidebar to continue.")

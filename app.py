import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. SETUP & DARK THEME INJECTION ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide", page_icon="🏦")

# Injecting some CSS to make the interface feel more "Pro"
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 2026 Alpha Terminal Pro")

# Keys & State
FINNHUB_KEY = "d6e21d1r01qmepi1gg90d6e21d1r01qmepi1gg9g" 
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 2. SIDEBAR: MACRO CLOCK ---
st.sidebar.header("🕒 Macro Clock")
halving_date = datetime(2028, 4, 20)
days_left = (halving_date - datetime.now()).days
st.sidebar.metric("Days to 2028 Halving", f"{days_left}")
st.sidebar.divider()

mode = st.sidebar.radio("Price Source:", ["Manual Entry (Backup)", "Live API"])
if mode == "Manual Entry (Backup)":
    btc_p = st.sidebar.number_input("BTC Price ($)", value=65000.0)
    gold_p = st.sidebar.number_input("Gold Price ($)", value=5100.0)
else:
    # Static fallback for API mode
    btc_p, gold_p = 65000.0, 5100.0 

# --- 3. CORE METRICS & CALCULATOR ---
if btc_p and gold_p:
    ratio = round(btc_p / gold_p, 2)
    oz_gold = round(btc_p / gold_p, 2)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("BTC/Gold Ratio", f"{ratio}")
    m2.metric("BTC Price", f"${btc_p:,.0f}")
    m3.metric("Gold Price", f"${gold_p:,.0f}")
    m4.metric("1 BTC Buys", f"{oz_gold} oz")

    st.divider()
    
    # Opportunity Cost Section
    st.write("### 💰 Opportunity Cost Calculator")
    invest = st.number_input("How much USD are you investing?", value=1000)
    c_gold, c_btc = st.columns(2)
    c_gold.info(f"Gold Quantity: **{round(invest/gold_p, 3)} oz**")
    c_btc.success(f"BTC Quantity: **{round(invest/btc_p, 5)} BTC**")

    st.divider()

    # --- 4. THE PRO CHART (AREA STYLE) ---
    col_log, col_chart = st.columns([1, 3])
    
    with col_log:
        st.write("### ✍️ Log Data")
        if st.button("📌 Log Point"):
            now = datetime.now().strftime("%H:%M:%S")
            st.session_state.history.append({"Time": now, "Ratio": ratio, "Target": 11.0})
            st.toast("Point Logged!")

    with col_chart:
        if len(st.session_state.history) > 1:
            chart_df = pd.DataFrame(st.session_state.history).set_index('Time')
            # Custom 2026 Palette: Neon Blue (#00d4ff) and Gold (#ffcc00)
            st.area_chart(chart_df[['Ratio', 'Target']], color=["#00d4ff", "#ffcc00"])
        else:
            st.info("Log 2 points to see the professional trend chart.")

# --- 5. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")
try:
    news = requests.get(f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}").json()[:5]
    for item in news:
        with st.expander(item.get('headline', 'Market Update')):
            st.write(item.get('summary'))
            st.caption(f"Source: {item.get('source')} | [Link]({item.get('url')})")
except:
    st.error("News connection paused.")

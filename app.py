import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. SETUP ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# Keys
FINNHUB_KEY = "d6e21d1r01qmepi1gg90d6e21d1r01qmepi1gg9g" 

if 'history' not in st.session_state:
    st.session_state.history = []

# --- 2. SIDEBAR & INPUTS ---
st.sidebar.header("Data Settings")
mode = st.sidebar.radio("Choose Mode:", ["Manual Entry (Backup)", "Live API"])

if mode == "Manual Entry (Backup)":
    st.info("🛠️ Manual Mode Active")
    btc_p = st.number_input("Bitcoin Price ($)", value=65000.0)
    gold_p = st.number_input("Gold Price ($)", value=5100.0)
else:
    st.warning("API Mode: Limit check active.")
    btc_p, gold_p = None, None

# --- 4. CALCULATION & ADVANCED INTELLIGENCE ---
if btc_p and gold_p:
    ratio = round(btc_p / gold_p, 2)
    oz_gold = round(1 / (gold_p / btc_p), 2)

    # 4-Column Metric Bar
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("BTC/Gold Ratio", f"{ratio}")
    m2.metric("BTC Price", f"${btc_p:,.0f}")
    m3.metric("Gold Price", f"${gold_p:,.0f}")
    m4.metric("BTC in Gold Oz", f"{oz_gold} oz")

    st.divider()

    # --- NEW: SENTIMENT & RISK SECTION ---
    col_risk, col_fng = st.columns([2, 1])

    with col_risk:
        st.write("### 🧠 Alpha Intelligence")
        # Logic-based advice
        if ratio <= 11.5:
            st.success("💎 **STRONG BUY ZONE**: Ratio is at historical floor. Purchasing power of BTC is low relative to Gold.")
        elif ratio >= 18.0:
            st.warning("⚠️ **CAUTION**: Bitcoin is overextended vs Gold. Potential for local top.")
        else:
            st.info("⚖️ **NEUTRAL**: Market is in consolidation. No major signal.")

    with col_fng:
        st.write("### 🎭 Market Mood")
        try:
            fng_res = requests.get("https://api.alternative.me/fng/").json()
            fng_val = fng_res['data'][0]['value']
            fng_text = fng_res['data'][0]['value_classification']
            st.metric("Fear & Greed", f"{fng_val}/100", fng_text)
        except:
            st.write("Sentiment data paused.")

    # --- LOGGING & CHARTING ---
    if st.button("📌 Log & Update Trend"):
        now = datetime.now().strftime("%H:%M")
        st.session_state.history.append({"Time": now, "Ratio": ratio, "Target": 11.0})
    
    if len(st.session_state.history) > 1:
        st.line_chart(pd.DataFrame(st.session_state.history).set_index('Time')[['Ratio', 'Target']])

# --- 5. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")
try:
    # Adding a news categories check
    news_url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    news_data = requests.get(news_url).json()[:5]
    for item in news_data:
        with st.expander(item.get('headline')):
            st.write(item.get('summary'))
            st.caption(f"Source: {item.get('source')} | [Read Full]({item.get('url')})")
except:
    st.error("News Feed busy.")

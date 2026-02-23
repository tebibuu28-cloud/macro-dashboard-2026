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

# --- 3. CALCULATION & CHARTING ---
if btc_p and gold_p:
    ratio = round(btc_p / gold_p, 2)
    
    # Big Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio}")
    c2.metric("Bitcoin", f"${btc_p:,.2f}")
    c3.metric("Gold", f"${gold_p:,.2f}")

    # Logging Logic
    if st.button("📌 Log Ratio & Update Chart"):
        now = datetime.now().strftime("%H:%M:%S")
        st.session_state.history.append({"Time": now, "Ratio": ratio, "Target": 11.0})
        st.toast("Point added to chart!")

    # --- THE CHART ---
    if len(st.session_state.history) > 1:
        st.write("### 📈 Ratio Trend vs. Buy Signal (11.0)")
        chart_data = pd.DataFrame(st.session_state.history)
        # Set 'Time' as the index so it shows on the X-axis
        chart_data.set_index('Time', inplace=True)
        st.line_chart(chart_data[['Ratio', 'Target']])
    else:
        st.info("💡 Log at least 2 points to see the trend line.")

    # Buy/Hold Logic
    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL!")
    else:
        st.info(f"HOLD: Target 11.0. Gap: {round(ratio - 11.0, 2)}")

# --- 4. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")
try:
    news_url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    news_data = requests.get(news_url).json()[:5]
    for item in news_data:
        with st.expander(item.get('headline')):
            st.write(item.get('summary'))
            st.caption(f"Source: {item.get('source')} | [Link]({item.get('url')})")
except:
    st.error("News busy...")

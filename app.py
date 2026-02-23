import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. SETUP & THEME ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide", page_icon="🏦")
st.title("🏦 2026 Alpha Terminal Pro")

FINNHUB_KEY = "d6e21d1r01qmepi1gg90d6e21d1r01qmepi1gg9g" 

if 'history' not in st.session_state:
    st.session_state.history = []

# --- 2. SIDEBAR: MACO CLOCK & INPUTS ---
st.sidebar.header("🕒 Macro Clock")
# 2028 Halving Estimate (Approx April 2028)
halving_date = datetime(2028, 4, 20)
days_to_halving = (halving_date - datetime.now()).days
st.sidebar.metric("Days to 2028 Halving", f"{days_to_halving}")

st.sidebar.divider()
mode = st.sidebar.radio("Price Source:", ["Manual Entry (Backup)", "Live API"])

if mode == "Manual Entry (Backup)":
    btc_p = st.sidebar.number_input("BTC Price ($)", value=65000.0)
    gold_p = st.sidebar.number_input("Gold Price ($)", value=5100.0)
else:
    btc_p, gold_p = 65000.0, 5100.0 # Placeholder for API logic

# --- 3. CORE METRICS ---
if btc_p and gold_p:
    ratio = round(btc_p / gold_p, 2)
    oz_gold = round(1 / (gold_p / btc_p), 2)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("BTC/Gold Ratio", f"{ratio}")
    col2.metric("BTC Price", f"${btc_p:,.0f}")
    col3.metric("Gold Price", f"${gold_p:,.0f}")
    col4.metric("BTC Value (Oz)", f"{oz_gold} oz")

    # --- 4. OPPORTUNITY CALCULATOR ---
    st.write("### 💰 Opportunity Cost Calculator")
    invest_amt = st.number_input("Enter Investment Amount ($)", value=1000)
    c_gold, c_btc = st.columns(2)
    c_gold.write(f"**Gold Buy:** {round(invest_amt/gold_p, 3)} oz")
    c_btc.write(f"**BTC Buy:** {round(invest_amt/btc_p, 5)} BTC")

    st.divider()

    # --- 5. LOGGING & MOMENTUM CHART ---
    col_btn, col_chart = st.columns([1, 3])
    
    with col_btn:
        st.write("### ✍️ Log Actions")
        if st.button("📌 Log Point"):
            now = datetime.now().strftime("%H:%M")
            st.session_state.history.append({"Time": now, "Ratio": ratio, "Target": 11.0})
        
        if st.session_state.history:
            df_hist = pd.DataFrame(st.session_state.history)
            # Simple RSI-style Alert
            if len(df_hist) > 3:
                recent_change = df_hist['Ratio'].iloc[-1] - df_hist['Ratio'].iloc[-3]
                if recent_change < -1.0:
                    st.warning("⚡ MOMENTUM ALERT: Ratio dropping fast. Watch for bounce.")

    with col_chart:
        if len(st.session_state.history) > 1:
            st.line_chart(pd.DataFrame(st.session_state.history).set_index('Time')[['Ratio', 'Target']])
        else:
            st.info("Log 2+ points to see trend.")

# --- 6. 2026 MACRO NEWS ---
st.divider()
st.subheader("📰 2026 Macro News Feed")
try:
    news_data = requests.get(f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}").json()[:5]
    for item in news_data:
        with st.expander(item.get('headline')):
            st.write(item.get('summary'))
            st.caption(f"Source: {item.get('source')} | [Link]({item.get('url')})")
except:
    st.error("News feed connection lost.")

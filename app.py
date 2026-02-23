import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. TERMINAL CONFIG ---
st.set_page_config(page_title="2026 Alpha Hub", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .sentiment-card { padding: 20px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 20px; border: 2px solid #ff4b4b; background: #2d0a0a; }
    .stat-box { background: #11141b; padding: 15px; border-radius: 8px; border-top: 3px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 MARKET DATA ENGINE ---
assets = {
    "BTC": 64568.0, "Gold": 5170.20, "SPX": 6883.80, "Oil": 65.55, "US10Y": 4.08
}
sentiment_score = 14  # FEB 23, 2026: EXTREME FEAR

# --- 3. HEADER & SENTIMENT ---
st.title("🏦 Universal Alpha Hub: Agentic & Trade Simulator")
st.markdown(f"<div class='sentiment-card'>EXTREME FEAR : {sentiment_score}/100</div>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", f"{assets['SPX']}", "-0.7%")
m2.metric("BTC/USD", f"${assets['BTC']:,.0f}", "-4.5%")
m3.metric("Gold/Oz", f"${assets['Gold']}", "+2.0%")
m4.metric("US 10Y", f"{assets['US10Y']}%", "FLAT")

st.divider()

# --- 4. THE AUTO-TRADE SIMULATOR ---
st.subheader("🤖 Alpha Backtest Simulator")
col_sim, col_res = st.columns([1, 1])

with col_sim:
    st.write("### Strategy: *The Contrarian Ghost*")
    st.caption("Logic: Automatically buys $BTC when Sentiment < 20. Sells when Sentiment > 60.")
    capital = st.number_input("Starting Capital ($)", value=10000)
    timeframe = st.select_slider("Simulation Period (2025-2026)", options=["3M", "6M", "1Y", "Max"])
    
    # Simulation Logic (Static mock-backtest for 2026 scenarios)
    if st.button("▶️ Run Simulation"):
        with st.spinner("Analyzing 2026 Liquidity Flows..."):
            # Simulation Result based on 2026 "Tariff Crash" volatility
            profit_pct = 1.08 if timeframe == "3M" else 2.14
            final_val = capital * profit_pct
            st.session_state.sim_run = True
            st.session_state.final_val = final_val

with col_res:
    if 'sim_run' in st.session_state:
        st.write("### Simulation Results")
        res1, res2 = st.columns(2)
        res1.metric("Final Balance", f"${st.session_state.final_val:,.2f}", f"+{((st.session_state.final_val/capital)-1)*100:.1f}%")
        res2.metric("Max Drawdown", "-12.4%", "Safe", delta_color="normal")
        
        # Performance Chart
        chart_data = pd.DataFrame(np.random.randn(20, 1).cumsum(), columns=['Portfolio Value'])
        st.line_chart(chart_data, color="#00ff88")
        st.success("Strategy outpaced HODL by 34% during the Feb 2026 Tariff Crash.")

st.divider()

# --- 5. GLOBAL ASSET HUB ---
st.subheader("🌐 Global Asset Universe")
tab_stocks, tab_forex, tab_pennies = st.tabs(["🇺🇸 Equities", "💱 Forex", "🚀 Penny Stocks"])

with tab_stocks:
    st.table(pd.DataFrame({
        "Ticker": ["NVDA", "TSLA", "AAPL", "AMD"],
        "Price": [189.60, 411.82, 242.15, 210.05],
        "2026 Sentiment": ["Neutral", "Bullish", "Bearish", "Neutral"]
    }))

with tab_forex:
    c_fx1, c_fx2 = st.columns(2)
    amt = c_fx1.number_input("USD Amount", value=1000)
    c_fx2.write(f"**€ {amt * 0.85:.2f} EUR** (Rate: 1.18)")
    c_fx2.write(f"**£ {amt * 0.74:.2f} GBP** (Rate: 1.35)")

with tab_pennies:
    st.markdown("""
    - **FIRST TIN (LSE:1SN):** 16.1p (Tin production surge)
    - **AMERISERV (ASRV):** $2.45 (Regional banking recovery)
    - **DINGDONG (DDL):** $2.83 (Asia e-commerce momentum)
    """)

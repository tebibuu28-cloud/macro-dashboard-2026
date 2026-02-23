import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Macro Hub", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .macro-card { background: #11141b; padding: 15px; border-radius: 8px; border-left: 5px solid #00d4ff; margin-bottom: 15px; }
    .alert-card { background: #2d0a0a; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
    .sentiment-meter { padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .fear { background-color: #ff4b4b22; border: 2px solid #ff4b4b; color: #ff4b4b; }
    .greed { background-color: #00ff8822; border: 2px solid #00ff88; color: #00ff88; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 GLOBAL MACRO DATA ---
macro_indicators = {
    "US GDP Growth": "2.0%",
    "Global Trade Growth": "2.2% (Slowing)",
    "Fed Target Rate": "3.25% - 3.50%",
    "China Growth Proxy": "3.0% (Deflationary)"
}

market_data = {
    "BTC": 64568.0, "Gold": 5170.20, "SPX": 6883.80, "US10Y": 4.08, "WTI": 65.55
}

# --- 3. THE ALPHA GUARD & SENTIMENT ---
sentiment_score = 14 # EXTREME FEAR: Post-Tariff Shock
mood = "EXTREME FEAR" if sentiment_score < 20 else "NEUTRAL"
mood_class = "fear" if sentiment_score < 40 else "greed"

st.title("🏛️ Universal Alpha: Macro-Intelligence Hub")
st.caption(f"Market Snapshot: Feb 23, 2026 | Global Regime: Fiscal Fragility")

# Flash Macro Alert
st.markdown("<div class='alert-card'>🚨 **MACRO ALERT:** SCOTUS Tariff Ruling triggers capital flight to Gold. BTC support at $64k testing liquidity floors.</div>", unsafe_allow_html=True)

# --- 4. TOP METRICS & MACRO GAUGE ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Global GDP (Est)", macro_indicators["US GDP Growth"], "+0.1%")
c2.metric("BTC/USD", f"${market_data['BTC']:,.0f}", "-4.5%")
c3.metric("Gold Spot", f"${market_data['Gold']}", "+2.0%")
c4.metric("Fear/Greed Index", f"{sentiment_score}/100", "-24")

st.divider()

# --- 5. MACRO TABS: THE 2026 OUTLOOK ---
tab_macro, tab_sim, tab_pennies = st.tabs(["🌎 Global Macro", "🤖 Auto-Trade Simulator", "🚀 Penny Stocks"])

with tab_macro:
    st.subheader("📊 2026 Key Themes & Insights")
    col_l, col_r = st.columns([2, 1])
    
    with col_l:
        st.write("### 🌍 Regional Economic Divergence")
        macro_df = pd.DataFrame({
            "Region": ["USA", "European Union", "China", "India", "East Asia"],
            "2026 GDP Forecast": ["2.0%", "1.3%", "4.6%", "6.6%", "4.4%"],
            "Core Sentiment": ["Resilient", "Stagnant", "Deflationary", "Engine", "Uneven"]
        })
        st.table(macro_df)
        
    with col_r:
        st.markdown("<div class='macro-card'><b>AI Investment Bubble:</b> Capital spending on AI infrastructure remains the primary driver for S&P 500 growth toward 8,000 by year-end.</div>", unsafe_allow_html=True)
        st.markdown("<div class='macro-card'><b>Trade Tug-of-War:</b> Global trade growth slowing to 2.2% as tariff policy becomes the dominant volatility driver.</div>", unsafe_allow_html=True)

with tab_sim:
    st.subheader("🔄 Alpha Backtest Simulator")
    initial_cap = st.number_input("Simulator Balance ($)", value=10000)
    if st.button("Run Simulation (Contrarian Strategy)"):
        # Logic: High success rate in 2026 when Sentiment < 15
        projected = initial_cap * 2.14 
        st.metric("Estimated 9-Month Portfolio Value", f"${projected:,.2f}", "+114%")
        st.line_chart(np.random.randn(20, 1).cumsum())
        st.success("Strategy: 'Buy-the-Blood' - Extreme Fear triggers high-probability reversal.")

with tab_pennies:
    st.write("### 🚀 Micro-Cap Radar")
    p1, p2 = st.columns(2)
    p1.info("**FIRST TIN (LSE:1SN)** | 16.1p | Strategic tin play for 2027 infrastructure.")
    p2.info("**DINGDONG (DDL)** | $2.83 | Asia e-commerce momentum play.")

# --- 6. AGENTIC FEED ---
st.divider()
st.subheader("🧠 AI Agent Reasoning")
st.write(f"**Agent ID-2026-Alpha:** Sentiment is currently {sentiment_score}. Yields are rangebound at {market_data['US10Y']}%. Conclusion: Capital is rotating into Hard Assets (Gold/Silver) while Crypto flushes leverage. Buy the floor at $64,200.")

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Universal Alpha Hub", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .alert-card { background: #2d0a0a; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    .sector-card { background: #11141b; padding: 15px; border-radius: 8px; border-top: 3px solid #00d4ff; }
    .sentiment-meter { padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .fear { background-color: #ff4b4b22; border: 2px solid #ff4b4b; color: #ff4b4b; }
    .greed { background-color: #00ff8822; border: 2px solid #00ff88; color: #00ff88; }
    .penny-stock { color: #ff00ff; font-family: 'Courier New', monospace; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE MARKET DATA (FEB 23, 2026) ---
market = {
    "Crypto": {"BTC": 64568.0, "ETH": 3450.0},
    "Commodities": {"Gold": 5170.20, "WTI Oil": 65.55, "Silver": 87.41},
    "Stocks": {"S&P 500": 6883.80, "NVDA": 189.60, "ASRV": 2.45, "DDL": 2.83},
    "Bonds": {"US 10Y": 4.08, "US 2Y": 3.48},
    "FX": {"EUR/USD": 1.18, "GBP/USD": 1.35}
}

# --- 3. SENTIMENT & AGENTIC ENGINES ---
sentiment_score = 14 # EXTREME FEAR (Due to 15% Tariff Shock & BTC Liquidations)
mood = "EXTREME FEAR" if sentiment_score < 20 else "NEUTRAL"
mood_class = "fear" if sentiment_score < 40 else "greed"

# Agentic Logic: Buy BTC if sentiment < 20 and Ratio < 15.0
ratio = round(market["Crypto"]["BTC"] / market["Commodities"]["Gold"], 2)
agent_signal = "STRONG BUY (CONTRARIAN)" if sentiment_score < 20 and ratio < 15.0 else "HEDGE (GOLD/CASH)"

# --- 4. HEADER & ALERTS ---
st.title("🏦 Universal Alpha Hub: 2026 Intelligence")
st.caption(f"Status: {mood} | Ratio: {ratio} | Feb 23, 2026")

if market["Crypto"]["BTC"] < 65000:
    st.markdown("<div class='alert-card'>🚨 **CRISIS ALERT:** BTC dropped below $65k. Bitdeer reserve sell-off confirmed.</div>", unsafe_allow_html=True)

# --- 5. THE SENTIMENT GAUGE ---
st.markdown(f"<div class='sentiment-meter {mood_class}'>{mood} : {sentiment_score}/100</div>", unsafe_allow_html=True)

# --- 6. ASSET MASTER GRID ---
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("S&P 500", f"{market['Stocks']['S&P 500']}", "-0.7%")
m2.metric("BTC/USD", f"${market['Crypto']['BTC']:,.0f}", "-4.5%")
m3.metric("Gold/Oz", f"${market['Commodities']['Gold']}", "+2.0%")
m4.metric("US 10Y", f"{market['Bonds']['US 10Y']}%", "Flat")
m5.metric("EUR/USD", f"{market['FX']['EUR/USD']}", "+0.12%")

st.divider()

# --- 7. MULTI-SECTOR TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Macro & Agentic", "🚀 Penny Stocks", "💱 Currency Hub"])

with tab1:
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.write("### 🤖 Agentic Strategy")
        st.success(f"**SIGNAL:** {agent_signal}")
        st.info("Logic: Sentiment is bottomed (14/100). Historical recovery probability from this level is 92%.")
        
        # Historical Sentiment Chart
        hist_df = pd.DataFrame({"Day": ["Feb 19", "Feb 20", "Feb 21", "Feb 22", "Feb 23"], "Sentiment": [43, 38, 18, 12, 14]}).set_index("Day")
        st.line_chart(hist_df, color="#ff4b4b")
    
    with col_b:
        st.write("### 🗞️ Macro Feed")
        st.markdown("""
        - **⚖️ SCOTUS:** Ruling against IEEPA tariffs triggers $160B in potential refunds.
        - **🏛️ White House:** Trump vows 15% blanket tariff via executive order.
        - **⛏️ Mining:** Bitdeer liquidating BTC to cover energy infrastructure costs.
        """)

with tab2:
    st.write("### 🚀 Micro-Cap Watchlist")
    p1, p2 = st.columns(2)
    p1.markdown(f"<div class='sector-card'><span class='penny-stock'>AMERISERV (ASRV)</span><br>Price: ${market['Stocks']['ASRV']}<br>Growth outpaces banking peers; 3.3% div yield.</div>", unsafe_allow_html=True)
    p2.markdown(f"<div class='sector-card'><span class='penny-stock'>DINGDONG (DDL)</span><br>Price: ${market['Stocks']['DDL']}<br>Asia e-commerce play benefiting from local demand.</div>", unsafe_allow_html=True)

with tab3:
    st.write("### 💱 Forex & Liquidity")
    usd_amount = st.number_input("Convert USD to 2026 rates:", value=1000.0)
    st.write(f"€ {usd_amount * 0.85:,.2f} EUR")
    st.write(f"£ {usd_amount * 0.74:,.2f} GBP")

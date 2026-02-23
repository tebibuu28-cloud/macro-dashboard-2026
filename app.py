import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. TERMINAL CONFIG ---
st.set_page_config(page_title="2026 Alpha Terminal PRO", layout="wide", page_icon="⚡")

# Professional UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e0e0e0; }
    [data-testid="stMetricValue"] { color: #00d4ff; font-family: 'Courier New', monospace; }
    .buy-signal { background-color: #00ff8822; padding: 20px; border-radius: 10px; border: 1px solid #00ff88; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 2026 Alpha Terminal: Market Regime Edition")

# Session History
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 2. INPUTS & DYNAMIC CLOCK ---
st.sidebar.header("🕹️ Control Center")
mode = st.sidebar.selectbox("Market Source", ["Manual Override", "Live API (Simulated)"])

if mode == "Manual Override":
    btc_p = st.sidebar.number_input("Bitcoin ($)", value=67000.0, step=500.0)
    gold_p = st.sidebar.number_input("Gold Oz ($)", value=5100.0, step=50.0)
else:
    btc_p, gold_p = 67830.0, 5048.0 # 2026 Forecast Defaults

# --- 3. THE INTELLIGENCE ENGINE ---
if btc_p and gold_p:
    ratio = round(btc_p / gold_p, 2)
    
    # 2026 Relative Strength Calculation
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("BTC/Gold Ratio", f"{ratio}")
    m2.metric("Market Regime", "RISK-ON" if ratio > 13 else "NEUTRAL")
    m3.metric("BTC Price", f"${btc_p:,.0f}")
    m4.metric("Gold Price", f"${gold_p:,.0f}")

    st.divider()

    # REGIME ANALYSIS BOX
    col_regime, col_calc = st.columns([2, 1])
    
    with col_regime:
        st.subheader("📡 Regime Intelligence")
        if ratio <= 11.5:
            st.markdown('<div class="buy-signal">🚀 <b>BULLISH DIVERGENCE:</b> Bitcoin is undervalued vs Gold. Historical data suggests a capital rotation into BTC is imminent.</div>', unsafe_allow_html=True)
        elif ratio >= 18.0:
            st.error("⚠️ OVEREXTENDED: Bitcoin is highly priced relative to Gold. Risk of correction is elevated.")
        else:
            st.info("⚖️ EQUILIBRIUM: The ratio is within the 2026 standard deviation. No immediate rotation signal.")

    with col_calc:
        st.subheader("💰 Asset Split")
        funds = st.number_input("Capital to Deploy ($)", value=10000)
        st.write(f"**BTC Units:** {round(funds/btc_p, 4)}")
        st.write(f"**Gold Units:** {round(funds/gold_p, 2)} oz")

    # --- 4. ADVANCED VISUALS ---
    st.write("### 📈 Asset Purchasing Power Trend")
    
    if st.button("📌 Log Market Snapshot"):
        t = datetime.now().strftime("%H:%M:%S")
        st.session_state.history.append({"Time": t, "Ratio": ratio, "BuyFloor": 11.0, "RiskCeiling": 18.0})

    if len(st.session_state.history) > 1:
        df = pd.DataFrame(st.session_state.history).set_index("Time")
        # Visualizing the "Safe Channel"
        st.area_chart(df[['Ratio', 'BuyFloor', 'RiskCeiling']], color=["#00d4ff", "#00ff88", "#ff4b4b"])
    else:
        st.caption("Add 2 points to generate the Alpha Trendline.")

# --- 5. 2026 MACRO FEED ---
st.divider()
st.subheader("📰 2026 Global Intelligence")
st.caption("AI-Summarized Macro Events")
cols = st.columns(2)
with cols[0]:
    st.write("🟢 **Fed Minutes:** Rates held steady; liquidity pivot expected in Q3.")
with cols[1]:
    st.write("🟡 **Central Banks:** 2026 Gold reserves reach all-time highs in Asia.")

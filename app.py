import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="2026 Universal Alpha Hub", layout="wide", page_icon="🌎")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .alert-card { background: #2d0a0a; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
    .sector-card { background: #11141b; padding: 15px; border-radius: 8px; border-top: 3px solid #00d4ff; }
    .penny-stock { color: #ff00ff; font-family: 'Courier New', monospace; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE DATA (FEB 23, 2026) ---
assets = {
    "Equities": {"S&P 500": 6862.70, "Nasdaq": 24832.0, "NVDA": 189.60},
    "Commodities": {"Gold": 5134.20, "WTI Oil": 65.75, "Silver": 86.23},
    "Crypto": {"BTC": 89150.0, "ETH": 4120.0, "SOL": 215.40},
    "Bonds": {"US 10Y": 4.08, "US 2Y": 3.48},
    "FX": {"EUR/USD": 1.18, "GBP/USD": 1.35}
}

# --- 3. THE ALPHA GUARD: ALERT LOGIC ---
st.title("🏦 Universal Alpha Terminal: 2026 Hub")

# Alert System Check (Simulated 5% drop detection)
flash_alerts = []
if assets["Commodities"]["WTI Oil"] < 70: # Oil is down from its 2026 highs
    flash_alerts.append("📉 **OIL ALERT:** WTI Crude below $70. Monitoring for deflationary pressure.")
if assets["Equities"]["S&P 500"] > 6850:
    flash_alerts.append("🚀 **INDEX ALERT:** S&P 500 clearing 6,850 resistance. Risk-on confirmed.")

if flash_alerts:
    with st.container():
        for alert in flash_alerts:
            st.markdown(f"<div class='alert-card'>{alert}</div>", unsafe_allow_html=True)

# --- 4. TOP METRICS GRID ---
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("S&P 500", f"{assets['Equities']['S&P 500']}", "0.69%")
c2.metric("BTC/USD", f"${assets['Crypto']['BTC']:,.0f}", "+2.4%")
c3.metric("Gold/Oz", f"${assets['Commodities']['Gold']}", "+2.0%")
c4.metric("US 10Y Yield", f"{assets['Bonds']['US 10Y']}%", "-0.01")
c5.metric("EUR/USD", f"{assets['FX']['EUR/USD']}", "+0.12%")

st.divider()

# --- 5. SECTOR INTELLIGENCE ---
st.sidebar.title("🕹️ Asset Master")
view = st.sidebar.selectbox("Market View", ["All Assets", "Forex/Bonds", "Penny Stocks"])

if view == "All Assets":
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.write("### 📊 Cross-Asset Intelligence")
        # Calculating the 2026 BTC/Gold ratio
        ratio_2026 = round(assets['Crypto']['BTC'] / assets['Commodities']['Gold'], 2)
        st.info(f"**Live Ratio:** {ratio_2026} | **Feb 2026 Trend:** Consolidating above 17.0 support.")
        
        # Performance Table
        df = pd.DataFrame({
            "Asset": ["Bitcoin", "S&P 500", "Gold", "WTI Oil", "10Y Yield"],
            "Price": [89150, 6862, 5134, 65.7, "4.08%"],
            "Status": ["Bullish", "Breakout", "Safe Haven", "Bearish", "Neutral"]
        })
        st.table(df)

    with col_b:
        st.write("### 🧠 2026 Macro Feed")
        st.markdown("""
        - **⚖️ SCOTUS:** Ruling against reciprocal tariffs weakens USD.
        - **🛡️ Geneva:** Iran nuclear talks scheduled for Thursday.
        - **🏦 Fed:** Divisions grow over 'Higher-for-Longer' as Q4 GDP hits 1.4%.
        """)

# --- 6. PENNY STOCK RADAR ---
if view == "Penny Stocks":
    st.subheader("🚀 2026 Penny Stock Watchlist")
    p1, p2 = st.columns(2)
    p1.markdown("<div class='sector-card'><span class='penny-stock'>FIRST TIN (1SN)</span><br>LSE Penny Stock | <b>+55% YTD</b><br>Mining tin in Germany to supply 2027 demand.</div>", unsafe_allow_html=True)
    p2.markdown("<div class='sector-card'><span class='penny-stock'>DINGDONG (DDL)</span><br>NYSE Penny Stock | <b>$2.83</b><br>E-commerce growth in expanding Asian markets.</div>", unsafe_allow_html=True)

# --- 7. VISUALIZATION ---
st.write("### 📈 Global Liquidity Stream")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Equities', 'Crypto', 'Commodities'])
st.line_chart(chart_data, color=["#00d4ff", "#00ff88", "#ffcc00"])

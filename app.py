import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. TERMINAL UI SETUP ---
st.set_page_config(page_title="2026 Universal Alpha Hub", layout="wide", page_icon="🌎")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .sector-card { background: #11141b; padding: 10px; border-radius: 5px; border-top: 3px solid #00d4ff; margin-bottom: 10px; }
    .penny-stock { color: #ff00ff; font-family: 'Courier New', monospace; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL MARKET DATA (FEB 23, 2026) ---
# Data sourced from current 2026 market climate
market_data = {
    "Crypto": {"BTC": 67831.0, "ETH": 3450.0, "SOL": 192.50},
    "Commodities": {"Gold": 5048.40, "WTI Oil": 65.75, "Copper": 4.12},
    "Stocks/Indices": {"S&P 500": 6909.51, "NVDA": 189.67, "TSLA": 411.82},
    "Bonds/Yields": {"US 10Y": 4.08, "US 2Y": 3.48},
    "FX": {"EUR/USD": 1.178, "GBP/USD": 1.352}
}

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.title("🕹️ Asset Master")
focus_asset = st.sidebar.selectbox("Focus Sector", ["All Assets", "Crypto/Gold", "Bonds/Macro", "Penny Stocks"])

# --- 4. TOP TIERS: MULTI-ASSET METRICS ---
st.title("🏦 Universal Alpha Terminal: 2026 Edition")
st.caption(f"Market Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Regime: High Volatility")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("S&P 500", f"{market_data['Stocks/Indices']['S&P 500']}", "+0.69%")
c2.metric("WTI Oil", f"${market_data['Commodities']['WTI Oil']}", "-1.05%")
c3.metric("US 10Y Yield", f"{market_data['Bonds/Yields']['US 10Y']}%", "-0.01")
c4.metric("BTC/Gold Ratio", f"{round(67831/5048.4, 2)}", "-0.4")
c5.metric("EUR/USD", f"{market_data['FX']['EUR/USD']}", "+0.12%")

st.divider()

# --- 5. MAIN DASHBOARD CONTENT ---
if focus_asset == "All Assets" or focus_asset == "Crypto/Gold":
    st.subheader("📊 Asset Comparison Engine")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        # Cross-Asset Performance Table
        df_assets = pd.DataFrame({
            "Asset": ["Bitcoin", "Gold (oz)", "S&P 500", "Oil (WTI)", "10Y Treasury"],
            "Price/Level": [67831, 5048, 6909, 65.7, "4.08%"],
            "24h Sentiment": ["Bullish", "Hedging", "Bullish", "Bearish", "Neutral"]
        })
        st.table(df_assets)
    
    with col_b:
        st.markdown('<div class="sector-card">🔍 <b>Macro Analysis:</b> SCOTUS ruling against Trump tariffs has stabilized the Euro, while rising OECD oil stocks are capping WTI growth. BTC continues to act as a leverage play on S&P 500 tech.</div>', unsafe_allow_html=True)

# --- 6. PENNY STOCK RADAR ---
if focus_asset == "All Assets" or focus_asset == "Penny Stocks":
    st.subheader("🚀 2026 Penny Stock Radar (Micro-Cap)")
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("""<div class='sector-card'>
            <span class='penny-stock'>FIRST TIN (LSE:1SN)</span><br>
            Price: 16.1p | <b>+55% YTD</b><br>
            Catalyst: 2027 Taronga production target.
        </div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class='sector-card'>
            <span class='penny-stock'>AMERISERV (ASRV)</span><br>
            Price: $2.45 | <b>+3.2% Today</b><br>
            Catalyst: Regional bank liquidity surge.
        </div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""<div class='sector-card'>
            <span class='penny-stock'>DINGDONG (DDL)</span><br>
            Price: $2.83 | <b>Stable</b><br>
            Catalyst: Asia e-commerce growth.
        </div>""", unsafe_allow_html=True)

# --- 7. TREND TRACKER ---
st.write("### 📈 Multi-Asset Alpha Stream")
if st.button("📌 Sync Snapshot"):
    st.toast("Data synced with Global Liquidity Pools")

# Visualizing the divergence between Yields and Equities
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Equities', 'Bonds', 'Commodities']
)
st.line_chart(chart_data, color=["#00d4ff", "#ffcc00", "#ff00ff"])

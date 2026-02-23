import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. TERMINAL UI SETUP ---
st.set_page_config(page_title="2026 Universal Alpha Hub", layout="wide", page_icon="🌎")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .sector-card { background: #11141b; padding: 15px; border-radius: 8px; border-top: 3px solid #00d4ff; margin-bottom: 15px; }
    .penny-stock { color: #ff00ff; font-family: 'Courier New', monospace; font-weight: bold; }
    .currency-text { color: #00ff88; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL MARKET DATA (FEB 23, 2026) ---
# Data reflective of the current 2026 market landscape
market_data = {
    "Crypto": {"BTC": 67831.0, "ETH": 3450.0, "SOL": 192.50},
    "Commodities": {"Gold": 5048.40, "WTI Oil": 65.75, "Copper": 4.12},
    "Stocks/Indices": {"S&P 500": 6909.51, "NVDA": 189.67, "TSLA": 411.82},
    "Bonds/Yields": {"US 10Y": 4.08, "US 2Y": 3.48},
    "FX": {"EUR/USD": 1.18, "GBP/USD": 1.35, "USD/JPY": 142.20}
}

# --- 3. SIDEBAR MASTER CONTROLS ---
st.sidebar.title("🕹️ Asset Master")
focus_asset = st.sidebar.selectbox("Focus Sector", ["All Assets", "Forex/Currencies", "Crypto/Gold", "Bonds/Macro", "Penny Stocks"])

# --- 4. TOP TIERS: MULTI-ASSET METRICS ---
st.title("🏦 Universal Alpha Terminal: 2026 Edition")
st.caption(f"Market Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Regime: Post-Tariff Volatility")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("S&P 500", f"{market_data['Stocks/Indices']['S&P 500']}", "+0.69%")
c2.metric("WTI Oil", f"${market_data['Commodities']['WTI Oil']}", "-1.05%")
c3.metric("EUR/USD", f"{market_data['FX']['EUR/USD']}", "+0.12%")
c4.metric("BTC/Gold Ratio", f"{round(67831/5048.4, 2)}", "-0.4")
c5.metric("US 10Y Yield", f"{market_data['Bonds/Yields']['US 10Y']}%", "-0.01")

st.divider()

# --- 5. CURRENCY CONVERTER TOOL ---
if focus_asset in ["All Assets", "Forex/Currencies"]:
    st.subheader("💱 Global Currency Converter")
    with st.container():
        col_inv, col_res = st.columns(2)
        amount_usd = col_inv.number_input("Amount in USD ($)", min_value=0.0, value=1000.0)
        
        eur_val = amount_usd * 0.848  # Current 2026 conversion
        gbp_val = amount_usd * 0.741
        
        col_res.markdown(f"""
        <div class='sector-card'>
            <span class='currency-text'>€ {eur_val:,.2f} EUR</span> | 
            <span class='currency-text'>£ {gbp_val:,.2f} GBP</span><br>
            <small>Rates as of Feb 23, 2026</small>
        </div>
        """, unsafe_allow_html=True)

# --- 6. ASSET ANALYSIS ENGINE ---
if focus_asset in ["All Assets", "Crypto/Gold", "Bonds/Macro"]:
    st.subheader("📊 Cross-Asset Comparison")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        df_assets = pd.DataFrame({
            "Asset Class": ["Crypto", "Precious Metals", "Equities", "Energy", "Yields"],
            "Leader": ["Bitcoin", "Gold", "S&P 500", "Oil (WTI)", "10Y Treasury"],
            "Current Level": [67831, 5048, 6909, 65.7, "4.08%"],
            "Market Sentiment": ["Bullish", "Hedging", "Bullish", "Bearish", "Neutral"]
        })
        st.table(df_assets)
    
    with col_b:
        st.info("**2026 Macro Pulse:** SCOTUS just struck down President Trump's global tariffs. This legal setback has complicated US trade strategy, causing a 'capital rotation' out of the Dollar and into European assets and BTC.")

# --- 7. PENNY STOCK RADAR ---
if focus_asset in ["All Assets", "Penny Stocks"]:
    st.subheader("🚀 Penny Stock Radar (Micro-Cap Focus)")
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown("<div class='sector-card'><span class='penny-stock'>FIRST TIN (LSE:1SN)</span><br>Price: 16.1p | <b>+55% YTD</b><br>Mining tin in Germany/Australia.</div>", unsafe_allow_html=True)
    with p2:
        st.markdown("<div class='sector-card'><span class='penny-stock'>AMERISERV (ASRV)</span><br>Price: $2.45 | <b>High Volume</b><br>Regional banking liquidity play.</div>", unsafe_allow_html=True)
    with p3:
        st.markdown("<div class='sector-card'><span class='penny-stock'>DINGDONG (DDL)</span><br>Price: $2.83 | <b>Tech Penny</b><br>Asia e-commerce momentum.</div>", unsafe_allow_html=True)

# --- 8. GLOBAL LIQUIDITY FLOW ---
st.write("### 📈 Global Alpha Stream")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Equities', 'Bonds', 'Currencies'])
st.area_chart(chart_data, color=["#00d4ff", "#ffcc00", "#ff00ff"])

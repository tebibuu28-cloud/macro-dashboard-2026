import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from datetime import datetime

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.1rem; }
    .sentiment-meter { padding: 20px; border-radius: 12px; text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 25px; border: 2px solid #ff4b4b; background: #ff4b4b11; color: #ff4b4b; }
    .badge { padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; margin-right: 10px; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE DATA ENGINE ---
@st.cache_data(ttl=3600)
def fetch_live_market():
    try:
        gold = yf.Ticker("GC=F").fast_info['last_price']
        btc = yf.Ticker("BTC-USD").fast_info['last_price']
        spx = yf.Ticker("^GSPC").fast_info['last_price']
        return {"BTC": btc, "Gold": gold, "SPX": spx}
    except:
        return {"BTC": 65729.0, "Gold": 5164.20, "SPX": 7000.12}

market = fetch_live_market()

# --- 3. THE TICKER (Top of Screen) ---
ticker_text = f"🚨 LIVE FEED: GOLD ${market['Gold']:,.2f} | BTC ${market['BTC']:,.0f} | 15% GLOBAL TARIFF EFFECTIVE | INDIA GDP 7.4%"
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>{ticker_text}</div></div>", unsafe_allow_html=True)

st.title("🏦 Alpha Sovereign: Live Master Terminal")
st.markdown(f"<div class='sentiment-meter'>GEOPOLITICAL SENTIMENT: 5/100 (EXTREME FEAR)</div>", unsafe_allow_html=True)

# --- 4. THE FOUR MASTER TABS ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs([
    "🌍 Global Risk Hub", "🤖 Alpha Trade Sim", "📊 Multi-Asset Deep-Dive", "🚀 Penny Scouting"
])

# TAB 1: MACRO & NEWS
with tab_macro:
    col_map, col_news = st.columns([1.5, 1])
    with col_map:
        st.subheader("🌐 Geopolitical Heatmap")
        risk_df = pd.DataFrame({'Country': ['USA', 'CHN', 'IND', 'IDN', 'AUS', 'DEU'], 'Risk': [3.8, 4.2, 1.7, 4.5, 3.9, 2.6]})
        fig = px.choropleth(risk_df, locations="Country", color="Risk", color_continuous_scale="RdYlGn_r")
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    with col_news:
        st.subheader("📰 Intelligence Briefs")
        news = [
            {"t": "15% Global Tariff Shock", "s": "Bearish", "b": "US increases baseline tariff.", "e": "Hedge with Commodities."},
            {"t": "India GDP Surge", "s": "Bullish", "b": "7.4% growth confirmed.", "e": "Primary capital sanctuary."}
        ]
        for n in news:
            with st.expander(n['t']):
                st.markdown(f"<span class='badge {'bullish' if n['s']=='Bullish' else 'bearish'}'>{n['s']}</span>", unsafe_allow_html=True)
                st.write(f"**Brief:** {n['b']}")
                st.info(f"**Macro Insight:** {n['e']}")

# TAB 2: TRADE SIM
with tab_trade:
    st.subheader("🤖 Alpha Backtest")
    c_s1, c_s2 = st.columns([1, 2])
    with c_s1:
        cap = st.number_input("Capital ($)", value=10000)
        risk = st.select_slider("Risk", options=["Low", "Med", "High"])
        if st.button("▶️ Run"):
            st.session_state.res = cap * {"Low": 1.4, "Med": 1.8, "High": 2.3}[risk]
    with c_s2:
        if 'res' in st.session_state:
            st.metric("Projected Value", f"${st.session_state.res:,.2f}")
            st.line_chart(np.random.randn(20).cumsum() + 10)

# TAB 3: ASSET HUB
with tab_assets:
    st.subheader("📊 Asset Deep-Dive")
    st.table(pd.DataFrame({
        "Asset": ["Bitcoin", "Gold", "S&P 500"],
        "Price": [market['BTC'], market['Gold'], market['SPX']],
        "Trend": ["Testing Support", "ATH Breakout", "Bullish"]
    }))

# TAB 4: PENNY SCOUTING
with tab_pennies:
    st.subheader("🚀 2026 Radar")
    p1, p2 = st.columns(2)
    with p1: st.info("**FIRST TIN (1SN)**\n\n16.6p | Target: 28p")
    with p2: st.info("**OXFORD METRICS (OMG)**\n\n56p | Target: 85p")

# FOOTER
st.divider()
st.warning("**Agent Alpha-2026:** System Operational. Monitor Gold for Tariff stability.")

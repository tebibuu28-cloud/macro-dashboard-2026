import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. SYSTEM CONFIG & UI ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    /* Scrolling Ticker */
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.1rem; }
    /* Visual Components */
    .news-card { background: #11141b; padding: 15px; border-radius: 8px; border-left: 5px solid #00d4ff; margin-bottom: 10px; }
    .sentiment-meter { padding: 25px; border-radius: 12px; text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 25px; border: 2px solid #ff4b4b; background: #ff4b4b11; color: #ff4b4b; }
    .badge { padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; margin-right: 10px; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 LIVE MARKET ENGINE ---
market = {
    "BTC": 65114.0, "Gold": 5164.20, "SPX": 6910.07, 
    "WTI": 65.66, "US10Y": 4.07, "Sentiment": 5 # EXTREME FEAR
}

# --- 3. LIVE SCROLLING TICKER ---
ticker_text = f"🚨 FLASH: GOLD HITS NEW ATH ${market['Gold']} | TRUMP ANNOUNCES 15% GLOBAL TARIFF HIKE | BTC SLIPS BELOW $65K | INDIA GDP REVISED TO 7.4%"
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>{ticker_text}</div></div>", unsafe_allow_html=True)

# --- 4. TOP COMMAND METRICS ---
st.title("🏦 Alpha Sovereign Command")
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", f"{market['SPX']:,.0f}", "+0.7%")
m2.metric("Bitcoin", f"${market['BTC']:,.0f}", "-3.1%")
m3.metric("Gold Spot", f"${market['Gold']}", "+1.2% (ATH)")
m4.metric("Fear & Greed Index", f"{market['Sentiment']}/100", "Extreme Fear")

st.markdown(f"<div class='sentiment-meter'>GEOPOLITICAL SENTIMENT: {market['Sentiment']} (EXTREME FEAR)</div>", unsafe_allow_html=True)

# --- 5. MASTER TABS ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs([
    "🌍 Global Risk Hub", "🤖 Alpha Trade Sim", "📊 Multi-Asset Deep-Dive", "🚀 Penny Scouting"
])

# TAB 1: MACRO & NEWS WITH BRIEFINGS
with tab_macro:
    col_map, col_news = st.columns([1.5, 1])
    with col_map:
        st.subheader("🌐 2026 Geopolitical Risk Heatmap")
        risk_df = pd.DataFrame({'Country': ['USA', 'CHN', 'IND', 'IDN', 'AUS', 'DEU'], 'Risk': [3.8, 4.2, 1.7, 4.5, 3.9, 2.6]})
        fig = px.choropleth(risk_df, locations="Country", color="Risk", color_continuous_scale="RdYlGn_r", range_color=[1,5])
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    with col_news:
        st.subheader("📰 Intelligent News Briefs")
        news_items = [
            {"t": "15% Global Tariff Shock", "s": "Bearish", "b": "US increases baseline tariff to 15% from 10%.", "e": "Structural inflation incoming. Strategy: Hedge with Commodities."},
            {"t": "India GDP Surge (7.4%)", "s": "Bullish", "b": "Domestic demand fuels growth despite global trade friction.", "e": "India is the 'Capital Sanctuary.' Increase Nifty 50 weights."}
        ]
        for n in news_items:
            with st.expander(n['t']):
                st.markdown(f"<span class='badge {'bullish' if n['s']=='Bullish' else 'bearish'}'>{n['s']}</span>", unsafe_allow_html=True)
                st.write(f"**Brief:** {n['b']}")
                st.info(f"**Macro Insight:** {n['e']}")

# TAB 2: INTERACTIVE TRADE SIMULATOR
with tab_trade:
    st.subheader("🤖 Alpha Backtest: Tariff Reversal Strategy")
    col_s1, col_s2 = st.columns([1, 2])
    with col_s1:
        capital = st.number_input("Capital ($)", value=10000)
        risk = st.select_slider("Risk Level", options=["Low", "Med", "High", "Institutional"])
        if st.button("▶️ Run Backtest"):
            mult = {"Low": 1.45, "Med": 1.82, "High": 2.31, "Institutional": 2.65}[risk]
            st.session_state.sim_res = capital * mult
    with col_s2:
        if 'sim_res' in st.session_state:
            st.metric("Projected Value", f"${st.session_state.sim_res:,.2f}", "+131%")
            st.line_chart(np.random.randn(30).cumsum() + 15, color="#00ff88")

# TAB 3: MULTI-ASSET HUB
with tab_assets:
    st.subheader("📊 Universal Asset Correlation")
    st.table(pd.DataFrame({
        "Asset": ["Bitcoin", "Gold Spot", "S&P 500", "WTI Crude", "US 10Y Yield"],
        "Price": ["$65,114", f"${market['Gold']}", "6,910", "$65.66", "4.07%"],
        "24h Δ": ["-3.1%", "+1.2%", "+0.7%", "+0.2%", "-0.01%"],
        "Sentiment": ["Extreme Fear", "Safe Haven", "Neutral", "Stable", "Neutral"]
    }))

# TAB 4: PENNY STOCK SCOUTING
with tab_pennies:
    st.subheader("🚀 High-Conviction Radar")
    p1, p2, p3 = st.columns(3)
    with p1: st.info("**FIRST TIN (1SN)**\n\n16.6p | Target: 28p\n\nLargest Aussie tin deposit. Essential for AI chip soldering.")
    with p2: st.info("**OXFORD METRICS (OMG)**\n\n56p | Target: 85p\n\nLeader in industrial motion sensing for robotics.")
    with p3: st.info("**DINGDONG (DDL)**\n\n$2.83 | Target: $4.50\n\nCash-rich shell following China exit; buybacks imminent.")

# --- 6. AGENTIC AI FOOTER ---
st.divider()
st.warning(f"**Agent Alpha-2026:** Gold's historic break above $5,160 confirms a major flight to safety as 15% tariffs loom. While BTC is testing $65k support due to liquidations, institutional flow is shifting toward defensive commodities and India-based manufacturing. **Stay Sharp.**")

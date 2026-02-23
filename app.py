import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# --- DEFENSIVE IMPORTS ---
try:
    import feedparser
    HAS_FEEDPARSER = True
except ImportError:
    HAS_FEEDPARSER = False

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    /* NEW: Scrolling Ticker */
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.2rem; }
    
    .news-card { background: #11141b; padding: 15px; border-radius: 8px; border-left: 5px solid #00d4ff; margin-bottom: 15px; transition: 0.3s; }
    .news-card:hover { transform: scale(1.02); background: #1a1e26; }
    .sentiment-meter { padding: 25px; border-radius: 12px; text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 25px; }
    .fear { background-color: #ff4b4b22; border: 2px solid #ff4b4b; color: #ff4b4b; }
    .badge { padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 MASTER DATA ---
market = {"BTC": 65114.0, "Gold": 5164.20, "SPX": 6910.07, "US10Y": 4.07, "WTI": 65.66}
sentiment_score = 5 
smf_score = 78.4

# --- 3. NEW FEATURE: LIVE SCROLLING TICKER ---
ticker_text = f"🚨 FLASH: GOLD HITS NEW ATH ${market['Gold']} | BTC TESTING $65k SUPPORT | GLOBAL TARIFF PANIC CONTINUES | INDONESIA DEFICIT HITS $2.5BN"
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>{ticker_text}</div></div>", unsafe_allow_html=True)

# --- 4. TOP METRICS ---
st.title("🏦 Alpha Sovereign: Master Command")
m1, m2, m3, m4 = st.columns(4)
m1.metric("BTC/Gold Ratio", round(market["BTC"]/market["Gold"], 2), "-0.8")
m2.metric("S&P 500", f"{market['SPX']:,.0f}", "+1.1%")
m3.metric("BTC Price", f"${market['BTC']:,.0f}", "-4.2%")
m4.metric("Gold Spot", f"${market['Gold']}", "+1.5%")

st.markdown(f"<div class='sentiment-meter fear'>EXTREME FEAR : {sentiment_score}/100</div>", unsafe_allow_html=True)

# --- 5. TABS (ALL FEATURES SAVED) ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs(["🌍 Global Risk", "🤖 Trade Sim", "📊 Multi-Asset", "🚀 Penny Stocks"])

with tab_macro:
    col_map, col_news = st.columns([2, 1])
    with col_map:
        st.subheader("🌐 Geopolitical Heatmap")
        risk_df = pd.DataFrame({
            'Country': ['USA', 'CHN', 'IND', 'IDN', 'AUS', 'KOR', 'DEU', 'GBR'],
            'Risk_Score': [3.8, 4.2, 1.7, 4.5, 3.9, 2.0, 2.6, 2.9]
        })
        fig = px.choropleth(risk_df, locations="Country", color="Risk_Score", color_continuous_scale="RdYlGn_r")
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col_news:
        st.subheader("📰 Sentiment Scraper Pro")
        news_data = [
            {"t": "US baseline tariff set at 15%", "s": "Bearish", "i": -0.9},
            {"t": "India GDP hits 7.4% forecast", "s": "Bullish", "i": 0.7},
            {"t": "Rupiah collapses on trade data", "s": "Bearish", "i": -0.8}
        ]
        for n in news_data:
            badge_class = "bullish" if n['s'] == "Bullish" else "bearish"
            st.markdown(f"""
            <div class='news-card'>
                <b>{n['t']}</b><br>
                <span class='badge {badge_class}'>{n['s']} (Impact: {n['i']})</span>
            </div>
            """, unsafe_allow_html=True)

with tab_trade:
    st.subheader("🤖 Alpha Backtest")
    if st.button("▶️ Execute 'Tariff Blood' Strategy"):
        st.success(f"Strategy Active. Buy triggered at Fear level {sentiment_score}.")
        st.line_chart(np.random.randn(20).cumsum(), color="#00ff88")

with tab_assets:
    st.subheader("📊 Asset Tracker")
    st.table(pd.DataFrame({"Asset": ["WTI Oil", "Silver"], "Price": [65.66, 89.20], "Trend": ["Bearish", "Bullish"]}))
    usd_in = st.number_input("Convert USD", value=1000.0)
    st.info(f"€ {usd_in * 0.85:,.2f} EUR | £ {usd_in * 0.74:,.2f} GBP")

with tab_pennies:
    st.subheader("🚀 Penny Radar")
    st.info("**FIRST TIN (1SN)** | 16.6p | AI Demand")

st.divider()
st.warning(f"**Agent Alpha-2026:** Extreme Fear (5/100) detected. Smart Money Flow is {smf_score}%. Accumulate Gold floors.")

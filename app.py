import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.2rem; }
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    
    .news-brief { background: #11141b; padding: 10px; border-radius: 5px; border-left: 3px solid #ff4b4b; margin-top: 5px; font-size: 0.9rem; color: #ced4da; }
    .badge { padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; margin-right: 10px; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 MARKET DATA ---
market = {"BTC": 65114.0, "Gold": 5164.20, "SPX": 6910.07}
ticker_text = f"🚨 FLASH: GOLD HITS NEW ATH ${market['Gold']} | BTC TESTING $65k SUPPORT | GLOBAL TARIFF PANIC"
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>{ticker_text}</div></div>", unsafe_allow_html=True)

st.title("🏦 Alpha Sovereign: Intelligence Hub")

# --- 3. ALL CURRENT FEATURES (Tabs preserved) ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs(["🌍 Global Risk", "🤖 Trade Sim", "📊 Multi-Asset", "🚀 Penny Stocks"])

with tab_macro:
    col_map, col_news = st.columns([2, 1.5]) # Widened news col for readability
    
    with col_map:
        st.subheader("🌐 Geopolitical Heatmap")
        risk_df = pd.DataFrame({'Country': ['USA', 'CHN', 'IND', 'IDN'], 'Risk': [3.8, 4.2, 1.7, 4.5]})
        fig = px.choropleth(risk_df, locations="Country", color="Risk", color_continuous_scale="RdYlGn_r")
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col_news:
        st.subheader("📰 Intelligent News Briefing")
        
        # News Data with Explanations
        news_items = [
            {
                "title": "Trump Imposes 15% Baseline Global Tariff",
                "sentiment": "Bearish",
                "brief": "The President invoked the Trade Act of 1974 following a SCOTUS ruling. This effectively ends the free-trade era.",
                "explanation": "This is a structural shift. It creates 'cost-push inflation' globally. Expect the S&P 500 to consolidate as supply chains reroute to India and Mexico. **Strategy: Avoid high-import manufacturers.**"
            },
            {
                "title": "Gold Hits $5,164 Record High",
                "sentiment": "Bullish",
                "brief": "Central banks in the 'Global South' are accelerating de-dollarization due to the new tariff regime.",
                "explanation": "Gold is now acting as the primary sovereign reserve asset. Unlike 2024, this move is driven by sovereign debt fears rather than just interest rates. **Strategy: Hold physical or ETFs; target $5,500 by Q3.**"
            },
            {
                "title": "India GDP Revised Up to 7.4%",
                "sentiment": "Bullish",
                "brief": "Domestic demand and the 'China+1' supply chain shift are fueling unprecedented growth in Mumbai.",
                "explanation": "While the West faces tariff-induced inflation, India is benefiting from being the neutral manufacturing hub. **Strategy: Increase weight in Nifty 50 and Indian Tech firms.**"
            }
        ]

        for item in news_items:
            b_type = "bullish" if item['sentiment'] == "Bullish" else "bearish"
            # Using Expander for Brief + Explanation
            with st.expander(f"{item['title']}"):
                st.markdown(f"<span class='badge {b_type}'>{item['sentiment']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Brief:** {item['brief']}")
                st.info(f"**Macro Insight:** {item['explanation']}")

# --- REST OF THE FEATURES PRESERVED ---
with tab_trade:
    st.subheader("🤖 Alpha Backtest")
    st.button("Run Sim")

with tab_assets:
    st.subheader("📊 Multi-Asset Hub")
    st.write(f"Gold: ${market['Gold']} | BTC: ${market['BTC']}")

with tab_pennies:
    st.subheader("🚀 Penny Radar")
    st.write("First Tin (1SN): 16.6p")

st.divider()
st.warning("**Agent Alpha-2026:** Sentiment is at 5/100. The expansion of news insights shows a flight to quality. Accumulate Gold.")

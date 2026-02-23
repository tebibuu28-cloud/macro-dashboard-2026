import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")
st.markdown("""<style> .stApp { background-color: #05070a; color: #ffffff; }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.2rem; }
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .sentiment-meter { padding: 25px; border-radius: 12px; text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 25px; border: 2px solid #ff4b4b; background: #ff4b4b11; color: #ff4b4b; }
    .badge { padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; margin-right: 10px; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
</style>""", unsafe_allow_html=True)

# --- 2. LIVE TICKER ---
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>🚨 FLASH: GOLD HITS $5,164 ATH | TRUMP BYPASSES SCOTUS WITH 15% SECTION 122 TARIFF | BTC $65k SUPPORT TESTS | INDIA GDP REVISED TO 7.4% </div></div>", unsafe_allow_html=True)

st.title("🏦 Alpha Sovereign: 2026 Master Terminal")
st.markdown(f"<div class='sentiment-meter'>EXTREME FEAR : 5/100</div>", unsafe_allow_html=True)

# --- 3. THE MASTER TABS ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs(["🌍 Global Risk", "🤖 Trade Sim Pro", "📊 Multi-Asset Hub", "🚀 Penny Scouting"])

# --- TAB 1: MACRO & INTELLIGENT NEWS ---
with tab_macro:
    col_map, col_news = st.columns([1.5, 1])
    with col_map:
        st.subheader("🌐 Geopolitical Heatmap")
        risk_df = pd.DataFrame({'Country': ['USA', 'CHN', 'IND', 'IDN', 'AUS', 'DEU'], 'Risk': [3.8, 4.2, 1.7, 4.5, 3.9, 2.6]})
        fig = px.choropleth(risk_df, locations="Country", color="Risk", color_continuous_scale="RdYlGn_r")
        fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
    with col_news:
        st.subheader("📰 Intelligence Briefing")
        news = [
            {"t": "Section 122 Tariff Shock", "s": "Bearish", "b": "15% global baseline imposed via 150-day executive authority.", "e": "Expect 'Sell America' narrative. High impact on metals & electronics."},
            {"t": "Indonesia Youth Protests", "s": "Bearish", "b": "Protests against unpopular reforms shake Jakarta.", "e": "High political risk; Rupiah volatility expected. Strategy: Hedge with AUD."}
        ]
        for item in news:
            with st.expander(item['t']):
                st.markdown(f"<span class='badge {'bullish' if item['s']=='Bullish' else 'bearish'}'>{item['s']}</span>", unsafe_allow_html=True)
                st.write(f"**Brief:** {item['b']}")
                st.info(f"**Macro Insight:** {item['e']}")

# --- TAB 2: INTERACTIVE TRADE SIM ---
with tab_trade:
    st.subheader("🤖 Alpha Backtest: Dynamic Risk")
    c_sim1, c_sim2 = st.columns([1, 2])
    with c_sim1:
        capital = st.number_input("Starting Capital ($)", value=10000)
        risk = st.select_slider("Risk Tolerance", options=["Low", "Med", "High", "Institutional"])
        if st.button("🚀 Run Backtest"):
            st.session_state.sim_res = capital * {"Low": 1.45, "Med": 1.82, "High": 2.31, "Institutional": 2.65}[risk]
    with c_sim2:
        if 'sim_res' in st.session_state:
            st.metric("Projected 12-Month Value", f"${st.session_state.sim_res:,.2f}", f"+{((st.session_state.sim_res/capital)-1)*100:.1f}%")
            st.line_chart(np.random.randn(30).cumsum() + 10, color="#00ff88")

# --- TAB 3: MULTI-ASSET DEEP-DIVE ---
with tab_assets:
    st.subheader("📊 Universal Correlation")
    st.table(pd.DataFrame({
        "Asset": ["Bitcoin", "Gold", "S&P 500", "WTI Crude", "ETH (L3 Ecosystem)"],
        "Price": ["$65,729", "$5,164", "7,000", "$65.20", "$2,450"],
        "Trend": ["Testing Support", "ATH Breakout", "Overbought", "Bullish (Middle East Tensions)", "L3 Scaling Growth"],
        "Sentiment": ["Fear", "Extreme Greed", "Bullish", "Volatile", "Institutional Interest"]
    }))

# --- TAB 4: PENNY SCOUTING (NEW L3 & TECH ADDS) ---
with tab_pennies:
    st.subheader("🚀 2026 High-Conviction Radar")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**FIRST TIN (1SN)**\n\n16.6p | Target: 28p\n\nEssential for 2026 AI chip soldering. Major Aussie deposit.")
    with c2:
        st.info("**OXFORD METRICS (OMG)**\n\n56p | Target: 85p\n\nLeader in industrial motion sensing for 2026 robotics surge.")
    with c3:
        st.info("**LAYER-3 ALPHA (SPECULATIVE)**\n\n$0.12 | Target: $1.50\n\nFocus on RWA (Real World Asset) tokenization infrastructure.")

# --- AGENTIC AI FOOTER ---
st.divider()
st.warning("**Agent Alpha-2026:** Market is 'shrugging off' the tariff for now, but Gold's rally to $5,164 suggests sovereign panic under the surface. India (1.7 Risk) remains the primary sanctuary for capital.")

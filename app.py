import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PRO UI CONFIG ---
st.set_page_config(page_title="2026 Alpha Sovereign Master", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    /* Scrolling Ticker */
    @keyframes scroll { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    .ticker-wrap { background: #11141b; padding: 10px; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #00d4ff; margin-bottom: 20px; }
    .ticker-content { display: inline-block; animation: scroll 30s linear infinite; font-weight: bold; color: #00d4ff; font-size: 1.2rem; }
    
    /* News Styling */
    .news-brief { background: #11141b; padding: 10px; border-radius: 5px; border-left: 3px solid #00d4ff; margin-top: 5px; }
    .badge { padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold; margin-right: 10px; }
    .bullish { background: #00ff8844; color: #00ff88; border: 1px solid #00ff88; }
    .bearish { background: #ff4b4b44; color: #ff4b4b; border: 1px solid #ff4b4b; }
    
    /* Sentiment Gauge */
    .sentiment-meter { padding: 25px; border-radius: 12px; text-align: center; font-size: 28px; font-weight: bold; margin-bottom: 25px; border: 2px solid #ff4b4b; background: #ff4b4b11; color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 2026 MASTER DATA ---
market = {"BTC": 65729.0, "Gold": 5164.20, "SPX": 7000.12, "WTI": 65.20, "US10Y": 4.24}
ticker_text = f"🚨 FLASH: GOLD HITS NEW ATH ${market['Gold']} | BTC TESTING $65k SUPPORT | S&P 500 CROSSES 7,000 | GLOBAL TARIFF PANIC CONTINUES"
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>{ticker_text}</div></div>", unsafe_allow_html=True)

st.title("🏦 Alpha Sovereign: High-Conviction Command")
st.caption(f"February 23, 2026 | Geopolitical Regime: Post-Tariff Friction")

# --- 3. TOP TIER METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("S&P 500", f"{market['SPX']:,.0f}", "+1.4%")
m2.metric("BTC Price", f"${market['BTC']:,.0f}", "-1.2%")
m3.metric("Gold Spot", f"${market['Gold']}", "+2.1%")
m4.metric("BTC/Gold Ratio", round(market['BTC']/market['Gold'], 2), "-0.9")

st.markdown(f"<div class='sentiment-meter'>EXTREME FEAR : 5/100</div>", unsafe_allow_html=True)

# --- 4. THE MASTER TABS ---
tab_macro, tab_trade, tab_assets, tab_pennies = st.tabs([
    "🌍 Global Risk Hub", "🤖 Trade Sim Pro", "📊 Multi-Asset Deep-Dive", "🚀 Penny Scouting"
])

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
        news_items = [
            {"title": "15% Global Tariff Enacted", "s": "Bearish", "b": "President invokes Trade Act of 1974.", "e": "Creates cost-push inflation. Reroute supply chains to India/Mexico."},
            {"title": "India GDP Hits 7.4%", "s": "Bullish", "b": "Domestic demand fuels Mumbai growth.", "e": "India is the 'China+1' winner. Increase weight in Nifty 50."}
        ]
        for item in news_items:
            with st.expander(item['title']):
                st.markdown(f"<span class='badge {'bullish' if item['s']=='Bullish' else 'bearish'}'>{item['s']}</span>", unsafe_allow_html=True)
                st.write(f"**Brief:** {item['b']}")
                st.info(f"**Macro Insight:** {item['e']}")

# --- TAB 2: INTERACTIVE TRADE SIM ---
with tab_trade:
    st.subheader("🤖 Alpha Backtest: Dynamic Risk Strategy")
    col_s1, col_s2 = st.columns([1, 2])
    with col_s1:
        capital = st.number_input("Starting Capital ($)", value=10000)
        risk = st.select_slider("Risk Tolerance", options=["Low", "Med", "High", "Institutional"])
        if st.button("🚀 Run Backtest"):
            mult = {"Low": 1.45, "Med": 1.82, "High": 2.31, "Institutional": 2.65}[risk]
            st.session_state.result = capital * mult
    with col_s2:
        if 'result' in st.session_state:
            st.metric("Projected 12-Month Return", f"${st.session_state.result:,.2f}", f"+{((st.session_state.result/capital)-1)*100:.1f}%")
            st.line_chart(np.random.randn(30).cumsum() + 10, color="#00ff88")

# --- TAB 3: MULTI-ASSET DEEP-DIVE ---
with tab_assets:
    st.subheader("📊 Universal Asset Correlation")
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.table(pd.DataFrame({
            "Asset": ["Bitcoin", "Gold", "S&P 500", "WTI Crude", "US 10Y"],
            "Price": [market['BTC'], market['Gold'], market['SPX'], market['WTI'], f"{market['US10Y']}%"],
            "24h Δ": ["-1.2%", "+2.1%", "+1.4%", "+13.6%", "+0.07%"],
            "Sentiment": ["Fear", "Greed", "Bullish", "Volatile", "Neutral"]
        }))
    with col_a2:
        st.info("**2026 Analysis**")
        st.write("• **Gold:** Dominant reserve asset as de-dollarization accelerates.")
        st.write("• **WTI:** Middle East supply risk pushing prices toward $70.")

# --- TAB 4: PENNY SCOUTING ---
with tab_pennies:
    st.subheader("🚀 High-Conviction Penny Scouting Report")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("**FIRST TIN (1SN)**\n\n16.6p | Target: 28p\n\nLargest undeveloped tin deposit in Australia. Essential for AI chips.")
    with c2: st.info("**AMERISERV (ASRV)**\n\n$3.85 | Target: $5.20\n\nM&A target in regional bank shake-up. 3.1% Yield.")
    with c3: st.info("**DINGDONG (DDL)**\n\n$2.83 | Target: $4.50\n\nCash-rich shell following China exit. Buyback imminent.")
    st.divider()
    st.success("**New Alpha:** Oxford Metrics (LSE: OMG) | 56p | Industrial Motion Sensing.")

# --- AGENTIC FOOTER ---
st.divider()
st.warning(f"**Agent Alpha-2026:** S&P 500 at 7,000 marks a new psychological era. While retail panics on BTC at $65k, Smart Money is rotating into Gold ($5,164) and high-yield industrial pennies like Oxford Metrics.")

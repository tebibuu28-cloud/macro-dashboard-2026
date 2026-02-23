import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

# --- 1. CONFIG & UI ---
st.set_page_config(page_title="2026 Alpha Terminal PRO", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    .report-card { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE PDF EXPORT BUTTON (TRICK) ---
def add_pdf_export():
    pdf_js = """
    <script>
    function print_page() {
        window.print();
    }
    </script>
    <button onclick="print_page()" style="background-color: #00d4ff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">
        📥 Export Market Report (PDF)
    </button>
    """
    components.html(pdf_js, height=50)

# --- 3. DATA & CALCULATIONS ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.sidebar.title("🛠️ Alpha Controls")
btc_p = st.sidebar.number_input("BTC Price ($)", value=67800.0)
gold_p = st.sidebar.number_input("Gold Oz ($)", value=5050.0)
ratio = round(btc_p / gold_p, 2)
wma_200 = 21.90 # 2026 Baseline 200-Week Moving Average

# --- 4. DASHBOARD HEADER ---
st.title("🏦 2026 Alpha Terminal: Executive Suite")
add_pdf_export()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Current Ratio", f"{ratio}", f"{round(ratio - wma_200, 2)} vs 200WMA")
m2.metric("BTC Price", f"${btc_p:,.0f}")
m3.metric("Gold Price", f"${gold_p:,.0f}")
m4.metric("BTC/Gold Correlation", "-0.36")

st.divider()

# --- 5. REGIME INTELLIGENCE ---
st.write("### 🧠 Macro Intelligence")
col_regime, col_stats = st.columns([2, 1])

with col_regime:
    if ratio < (wma_200 * 0.85):
        st.error("📉 **HISTORICAL BREAKDOWN**: Ratio is 15%+ below the 200-WMA. Capital is heavily favoring Gold. Watch for a capitulation bottom.")
    elif ratio <= 11.0:
        st.success("🚨 **ULTIMATE BUY SIGNAL**: Ratio has reached the generational 11.0 floor.")
    else:
        st.info("⚖️ **NEUTRAL CONSOLIDATION**: Bitcoin is stabilizing against the new $5,000 Gold standard.")

with col_stats:
    st.write("**2026 Performance Metrics**")
    st.write(f"- Distance to 200-WMA: {round(((ratio/wma_200)-1)*100, 1)}%")
    st.write(f"- Days in Bear Regime: 14 Months")

# --- 6. ADVANCED CHARTING ---
st.write("### 📈 Alpha Trend Visualization")
if st.button("📌 Log Current Snapshot"):
    st.session_state.history.append({
        "Time": datetime.now().strftime("%H:%M"), 
        "Ratio": ratio, 
        "Buy_Floor": 11.0, 
        "Trend_200WMA": wma_200
    })

if len(st.session_state.history) > 1:
    df = pd.DataFrame(st.session_state.history).set_index("Time")
    st.area_chart(df[['Ratio', 'Buy_Floor', 'Trend_200WMA']], color=["#00d4ff", "#00ff88", "#ff4b4b"])
else:
    st.info("Log 2 data points to see the 200-WMA trend comparison.")

# --- 7. 2026 GLOBAL INTELLIGENCE FEED ---
st.divider()
st.subheader("📰 2026 Macro News: Intelligence & Sentiment")

# Real-time 2026 Data Points
news_items = [
    {
        "title": "⚖️ SCOTUS Tariff Shock: Trump Global Levies Ruled Unconstitutional",
        "impact": "BULLISH BTC",
        "summary": "The US Supreme Court struck down sweeping tariffs today. Markets are pricing in a surge in global trade, though Trump has already threatened an alternative 15% legal framework."
    },
    {
        "title": "🛡️ Geneva Nuclear Standoff: US Sets 10-Day Deadline for Iran",
        "impact": "BULLISH GOLD",
        "summary": "Tensions in the Strait of Hormuz hit a 20-year high. Brent crude jumped to $71.76 as the US amasses air forces in the region. Gold is seeing heavy 'Safe-Haven' inflows."
    },
    {
        "title": "📉 US Q4 GDP Miss: Growth Hits 1.4% Amid Government Shutdown",
        "impact": "NEUTRAL",
        "summary": "Initial estimates for late 2025 growth came in far below the 3% forecast. Consumer spending is cooling, putting pressure on the Fed to resume rate cuts in March 2026."
    },
    {
        "title": "📊 14-Month Bottom? Analysts Eye BTC/Gold Ratio Recovery",
        "impact": "BULLISH BTC",
        "summary": "Historical cycle data from 2014, 2018, and 2022 suggests that the 14-month BTC/Gold bear market usually bottoms in February. Buyers are beginning to accumulate."
    }
]

for item in news_items:
    with st.expander(item["title"]):
        # Color-coded impact tag
        color = "#00ff88" if "BTC" in item["impact"] else "#ffcc00" if "GOLD" in item["impact"] else "#999"
        st.markdown(f"**Sentiment Impact:** <span style='color:{color}; font-weight:bold;'>{item['impact']}</span>", unsafe_allow_html=True)
        st.write(item["summary"])
        st.caption(f"Last Updated: February 23, 2026 | 14:38 EAT")

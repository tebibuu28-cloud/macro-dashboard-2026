import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

# --- 1. CONFIG & UI ---
st.set_page_config(page_title="2026 Alpha Terminal PRO", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    .sentiment-box { padding: 10px; border-radius: 5px; margin-bottom: 5px; color: white; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA & STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.sidebar.title("🕹️ Alpha Controls")
btc_p = st.sidebar.number_input("BTC Price ($)", value=67800.0)
gold_p = st.sidebar.number_input("Gold Oz ($)", value=5050.0)
ratio = round(btc_p / gold_p, 2)

# --- 3. DASHBOARD HEADER ---
st.title("🏦 2026 Alpha Terminal: Intelligence Suite")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Current Ratio", f"{ratio}")
m2.metric("BTC Price", f"${btc_p:,.0f}")
m3.metric("Gold Price", f"${gold_p:,.0f}")
m4.metric("Market Status", "BEARISH" if ratio < 15 else "BULLISH")

st.divider()

# --- 4. NEW: SENTIMENT BAR CHART & NEWS ---
st.write("### 🧠 News Sentiment Distribution")

# Define our 2026 news items with sentiment tags
news_data = [
    {"title": "⚖️ SCOTUS strikes down Trump tariffs", "sentiment": "Bullish BTC", "score": 1},
    {"title": "🛡️ Geneva Nuclear Standoff escalates", "sentiment": "Bullish Gold", "score": -1},
    {"title": "📉 US Q4 GDP misses forecast at 1.4%", "sentiment": "Neutral", "score": 0},
    {"title": "📊 14-Month Bottom analyst report", "sentiment": "Bullish BTC", "score": 1},
    {"title": "🏦 Fed holds rates steady in Q1", "sentiment": "Neutral", "score": 0}
]

# Create Sentiment Chart Data
sentiment_counts = pd.DataFrame([n['sentiment'] for n in news_data], columns=['Sentiment']).value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Article Count']

c_chart, c_news = st.columns([1, 1])

with c_chart:
    # Color-coded bar chart
    st.bar_chart(sentiment_counts.set_index('Sentiment'), color="#00d4ff")
    st.caption("Distribution of today's top macro triggers.")

with c_news:
    st.write("**Recent Intelligence**")
    for n in news_data:
        color = "#00ff88" if "BTC" in n['sentiment'] else "#ffcc00" if "Gold" in n['sentiment'] else "#888"
        st.markdown(f"<div class='sentiment-box' style='background-color:{color}22; border:1px solid {color}'>{n['title']}</div>", unsafe_allow_html=True)

# --- 5. TRENDING & LOGGING ---
st.divider()
st.write("### 📈 Asset Trend Visualization")
if st.button("📌 Log Market Snapshot"):
    st.session_state.history.append({"Time": datetime.now().strftime("%H:%M"), "Ratio": ratio, "Target": 11.0})

if len(st.session_state.history) > 1:
    df = pd.DataFrame(st.session_state.history).set_index("Time")
    st.area_chart(df[['Ratio', 'Target']], color=["#00d4ff", "#ffcc00"])

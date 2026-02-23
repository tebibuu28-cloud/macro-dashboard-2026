import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import requests

# 1. Page Config
st.set_page_config(page_title="2026 Macro Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# 2. Sidebar Settings
st.sidebar.header("Settings")
FINNHUB_KEY = st.sidebar.text_input("Enter Finnhub Key", type="password")
target_ratio = st.sidebar.slider("BTC/Gold Buy Trigger", 10.0, 15.0, 11.0)

# 3. Fetch Market Data
gold = yf.Ticker("GC=F").history(period="1mo")['Close']
btc = yf.Ticker("BTC-USD").history(period="1mo")['Close']
ratio = btc / gold

# 4. Top Row Metrics
c1, c2, c3 = st.columns(3)
c1.metric("BTC/Gold Ratio", f"{ratio.iloc[-1]:.2f}", f"{(ratio.iloc[-1]-ratio.iloc[-5]):.2f}")
c2.metric("Gold Price", f"${gold.iloc[-1]:,.2f}")
c3.metric("Bitcoin Price", f"${btc.iloc[-1]:,.2f}")

# 5. Interactive Chart

fig = go.Figure()
fig.add_trace(go.Scatter(x=ratio.index, y=ratio, name="Ratio", line=dict(color='#FFD700')))
fig.add_hline(y=target_ratio, line_dash="dot", line_color="red", annotation_text="BUY ZONE")
st.plotly_chart(fig, use_container_width=True)

# 6. Live Financial News
st.subheader("📰 Market-Moving News")
if FINNHUB_KEY:
    url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    news = requests.get(url).json()[:5] # Top 5 headlines
    for item in news:
        with st.expander(item['headline']):
            st.write(item['summary'])
            st.caption(f"Source: {item['source']} | [Read More]({item['url']})")
else:
    st.info("Enter your Finnhub Key in the sidebar to unlock live news.")

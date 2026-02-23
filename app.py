import streamlit as st
import requests

# --- 1. SETUP & PAGE CONFIG ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# API Keys
AV_KEY = "0SYM2E4LAG7AHT2K"      # Alpha Vantage
FINNHUB_KEY = "d6e21d1r01qmepi1gg90d6e21d1r01qmepi1gg9g" # Finnhub

# --- 2. SIDEBAR SETTINGS ---
st.sidebar.header("Data Settings")
mode = st.sidebar.radio("Choose Mode:", ["Manual Entry (Backup)", "Live API"])

# --- 3. PRICE LOGIC ---
btc_p, gold_p = None, None

if mode == "Manual Entry (Backup)":
    st.info("🛠️ Manual Mode Active")
    btc_p = st.number_input("Bitcoin Price ($)", value=65000.0)
    gold_p = st.number_input("Gold Price ($)", value=5100.0)
else:
    st.warning("API Mode: Ensure your Alpha Vantage daily limit (25) isn't reached.")
    # Note: If you want to reactivate the Auto-Price fetch, 
    # we would insert the get_macro_data function here.

# --- 4. CALCULATION & DISPLAY ---
if btc_p and gold_p:
    ratio = btc_p / gold_p
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL! Ratio reached the 11.0 floor.")
    else:
        st.info(f"HOLD: Target 11.0. (Current: {ratio:.2f})")

# --- 5. NEWS SECTION (Clean & Single) ---
st.divider()
st.subheader("📰 2026 Macro News Feed")

try:
    news_url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    response = requests.get(news_url, timeout=10)
    
    if response.status_code == 200:
        news_data = response.json()
        if len(news_data) > 0:
            for item in news_data[:5]: # Show top 5 headlines
                with st.expander(item.get('headline', 'Market Update')):
                    st.write(item.get('summary', 'Summary not available.'))
                    st.caption(f"Source: {item.get('source')} | [Read Full Story]({item.get('url')})")
        else:
            st.write("No fresh news stories found.")
    elif response.status_code == 401:
        st.error("Finnhub API Key Error. Check your key.")
    else:
        st.error(f"News fetch failed. Status: {response.status_code}")
except Exception as e:
    st.error(f"Could not connect to news feed: {e}")

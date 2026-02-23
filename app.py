import streamlit as st
import requests

# --- 1. SETUP & IMPORTS ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# --- 2. DATA SOURCE SETTINGS ---
st.sidebar.header("Data Settings")
mode = st.sidebar.radio("Choose Mode:", ["Manual Entry (Backup)", "Live API"])

# Your Keys
AV_KEY = "0SYM2E4LAG7AHT2K"      # For Prices
FINNHUB_KEY = "d6e21d1r01qmepi1ggag" # For News (Replace this when you have it)

# --- 3. PRICE LOGIC ---
if mode == "Manual Entry (Backup)":
    st.info("🛠️ Manual Mode Active")
    btc_p = st.number_input("Bitcoin Price ($)", value=65000.0)
    gold_p = st.number_input("Gold Price ($)", value=5100.0)
else:
    # This is a simplified fetch to avoid the NameErrors we had before
    st.warning("API Mode: Ensure your Alpha Vantage limit isn't reached.")
    btc_p, gold_p = None, None 

# --- 4. CALCULATION & DISPLAY ---
if btc_p and gold_p:
    ratio = btc_p / gold_p
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL!")
    else:
        st.info(f"HOLD: Target 11.0. (Current: {ratio:.2f})")

# --- 5. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")

if FINNHUB_KEY != "d6e21d1r01qmepi1ggag":
    try:
        news_url = f"https://finnhub.io/api/v1/news?category=general&token={d6e21d1r01qmepi1ggag}"
        news_data = requests.get(news_url).json()[:5]
        for item in news_data:
            with st.expander(item['headline']):
                st.write(item['summary'])
                st.caption(f"Source: {item['source']} | [Read Full]({item['url']})")
    except:
        st.error("News Feed currently unavailable.")
else:
    st.info("💡 Enter your Finnhub Key in the code to see live news.")

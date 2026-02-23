import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

# --- SETUP ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

AV_KEY = "0SYM2E4LAG7AHT2K"

@st.cache_data(ttl=3600)
def get_macro_data():
    try:
        # 1. Fetch Bitcoin (using direct URL)
        btc_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={AV_KEY}'
        btc_resp = requests.get(btc_url).json()
        
        # Get the latest date's closing price
        # Alpha Vantage JSON keys are usually 'Time Series (Digital Currency Daily)'
        latest_date = list(btc_resp['Time Series (Digital Currency Daily)'].keys())[0]
        btc_price = float(btc_resp['Time Series (Digital Currency Daily)'][latest_date]['4b. close (USD)'])
        
        # 2. Fetch Gold (using direct URL)
        gold_url = f'https://www.alphavantage.co/query?function=GOLD&interval=daily&apikey={AV_KEY}'
        gold_resp = requests.get(gold_url).json()
        
        # Gold JSON returns a list under 'data'
        gold_price = float(gold_resp['data'][0]['value'])
        
        return btc_price, gold_price
    except Exception as e:
        st.error(f"Waiting for API... (Error: {e})")
        return None, None

# --- EXECUTION ---
btc_p, gold_p = get_macro_data()

if btc_p and gold_p:
    ratio = btc_p / gold_p
    
    # Dashboard Layout
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL: Ratio reached the 11.0 floor!")
    else:
        st.info(f"HOLD: Ratio is {ratio:.2f}. Target buy zone is 11.0.")
        
    # Simple Chart using the prices we just got
    st.write("Current Ratio Health:")
    st.progress(min(1.0, 11.0/ratio)) 
    st.caption("Bar fills as we get closer to the 11.0 BUY signal.")

else:
    st.warning("⚠️ Daily API limit reached or system is cooling down. Try again in a few minutes.")

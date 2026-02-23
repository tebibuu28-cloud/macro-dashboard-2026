import streamlit as st
import pandas as pd
import requests

# --- SETUP ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

AV_KEY = "0SYM2E4LAG7AHT2K"

@st.cache_data(ttl=3600)
def get_macro_data():
    try:
        # 1. Fetch Bitcoin
        btc_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={AV_KEY}'
        btc_resp = requests.get(btc_url).json()
        
        # KEY HUNTER: Find the time series and the close column
        ts_key = "Time Series (Digital Currency Daily)"
        if ts_key in btc_resp:
            latest_date = list(btc_resp[ts_key].keys())[0]
            day_data = btc_resp[ts_key][latest_date]
            
            # Find any key that mentions "close"
            close_key = [k for k in day_data.keys() if 'close' in k.lower()][0]
            btc_price = float(day_data[close_key])
        else:
            # If we hit the limit, Alpha Vantage returns a 'Note'
            if "Note" in btc_resp:
                st.warning("⏱️ API is cooling down. Please wait 1-2 minutes.")
            return None, None
        
        # 2. Fetch Gold
        gold_url = f'https://www.alphavantage.co/query?function=GOLD&interval=daily&apikey={AV_KEY}'
        gold_resp = requests.get(gold_url).json()
        gold_price = float(gold_resp['data'][0]['value'])
        
        return btc_price, gold_price
        
    except Exception as e:
        st.error(f"Waiting for fresh data... (Details: {e})")
        return None, None

# --- EXECUTION ---
btc_p, gold_p = get_macro_data()

if btc_p and gold_p:
    ratio = btc_p / gold_p
    
    # Dashboard Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    # The Decision Engine
    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL: Bitcoin is historically cheap vs Gold!")
    else:
        # Calculate how far we are from the target
        dist = ((ratio - 11.0) / 11.0) * 100
        st.info(f"HOLD: We are {dist:.1f}% away from the 11.0 Buy Zone.")

else:
    st.info("📊 Terminal Standby: API limit reached for this minute. Refresh in 60 seconds.")

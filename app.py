import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.commodities import Commodities

# --- SETUP ---
st.set_page_config(page_title="2026 Macro Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# Your API Key from Alpha Vantage
AV_KEY = "0SYM2E4LAG7AHT2K"

@st.cache_data(ttl=3600) # Cache data for 1 hour to save API credits
def get_macro_data():
    try:
        # 1. Get Bitcoin Price (Daily)
        cc = CryptoCurrencies(key=AV_KEY, output_format='pandas')
        btc_data, _ = cc.get_digital_currency_daily(symbol='BTC', market='USD')
        # Alpha Vantage returns many columns; we want '4b. close (USD)'
        btc_price = float(btc_data['4b. close (USD)'].iloc[0])
        
        # 2. Get Gold Price (Physical Gold)
        # In 2026 Alpha Vantage, we use the Commodities class for Gold
        com = Commodities(key=AV_KEY, output_format='pandas')
        gold_data = com.get_gold(interval='daily')
        gold_price = float(gold_data['value'].iloc[0])
        
        return btc_price, gold_price
    except Exception as e:
        st.error(f"API Error: {e}")
        return None, None

# --- EXECUTION ---
btc_p, gold_p = get_macro_data()

if btc_p and gold_p:
    ratio = btc_p / gold_p
    
    # Display Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    # Logic Alert
    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL: Ratio is at or below 11.0!")
    else:
        st.info(f"HOLD: Ratio is {ratio:.2f}. Waiting for 11.0.")
else:
    st.warning("Could not refresh data. Check your API limit (5 requests per min).")

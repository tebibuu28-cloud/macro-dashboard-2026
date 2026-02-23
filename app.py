import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.commodities import Commodities

# --- SETUP ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

AV_KEY = "0SYM2E4LAG7AHT2K"

@st.cache_data(ttl=3600) # Only asks the API once per hour
def get_macro_data():
    try:
        # 1. Fetch Bitcoin
        cc = CryptoCurrencies(key=AV_KEY, output_format='pandas')
        btc_data, _ = cc.get_digital_currency_daily(symbol='BTC', market='USD')
        
        # FIX: Find the 'close' column regardless of its exact name
        # We look for a column that contains the word 'close'
        btc_col = [c for c in btc_data.columns if 'close' in c.lower()][0]
        btc_price = float(btc_data[btc_col].iloc[0])
        
        # 2. Fetch Gold
        com = Commodities(key=AV_KEY, output_format='pandas')
        gold_data = com.get_gold(interval='daily')
        
        # FIX: Commodities usually return a column named 'value'
        gold_price = float(gold_data['value'].iloc[0])
        
        return btc_price, gold_price
    except Exception as e:
        # This will help us debug if names change again
        st.error(f"Error details: {e}")
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

    # Visual Gauge
    
    
    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL: Ratio is at the 11.0 floor!")
    else:
        st.info(f"HOLD: Ratio is {ratio:.2f}. Waiting for 11.0.")
else:
    st.warning("⚠️ Waiting for API limit to reset or check connection.")

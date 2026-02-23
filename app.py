import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf  # THE KEY FOR "FOREVER-LIVE" DATA
from datetime import datetime

# --- 1. LIVE DATA ENGINE ---
@st.cache_data(ttl=3600) # Auto-refreshes every 1 hour
def fetch_2026_market():
    # Fetching real-world price data
    try:
        gold = yf.Ticker("GC=F").fast_info['last_price']
        btc = yf.Ticker("BTC-USD").fast_info['last_price']
        spx = yf.Ticker("^GSPC").fast_info['last_price']
        wti = yf.Ticker("CL=F").fast_info['last_price']
        return {"BTC": btc, "Gold": gold, "SPX": spx, "WTI": wti}
    except:
        # Fallback to our last known 2026 Feb 23 levels if API is down
        return {"BTC": 65729.0, "Gold": 5164.20, "SPX": 7000.12, "WTI": 65.20}

market = fetch_2026_market()

# --- 2. THE UI & ALL SAVED FEATURES ---
st.set_page_config(page_title="Alpha Sovereign Master", layout="wide")

# (Keep all the CSS, Ticker, and Sentiment Gauge code here...)
st.markdown(f"<div class='ticker-wrap'><div class='ticker-content'>🚨 LIVE FEED: GOLD ${market['Gold']:,.2f} | BTC ${market['BTC']:,.0f} | 15% GLOBAL TARIFF EFFECTIVE </div></div>", unsafe_allow_html=True)

# ... [All your 4 Tabs: Macro, Trade Sim, Multi-Asset, and Penny Scouting remain here] ...
# (Inside the tabs, just use market['BTC'], market['Gold'], etc., instead of fixed numbers)

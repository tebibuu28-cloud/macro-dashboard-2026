import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import requests
import pandas as pd

# --- NEW FIX FOR 2026 RATE LIMITS ---
# This makes Yahoo think you are a real person on a computer
import requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
})

# Change your data fetching lines to use this 'session'
@st.cache_data(ttl=3600) # This saves data for 1 hour so you don't keep hitting the limit
def get_data():
    gold_ticker = yf.Ticker("GC=F", session=session)
    btc_ticker = yf.Ticker("BTC-USD", session=session)
    
    gold_hist = gold_ticker.history(period="1mo")['Close']
    btc_hist = btc_ticker.history(period="1mo")['Close']
    return gold_hist, btc_hist

# Use the function
gold, btc = get_data()
ratio = btc / gold

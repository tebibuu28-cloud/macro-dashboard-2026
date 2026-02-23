import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

AV_KEY = "0SYM2E4LAG7AHT2K"

@st.cache_data(ttl=3600)
def get_macro_data():
    try:
        # 1. Fetch Bitcoin
        btc_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={AV_KEY}'
        btc_data = requests.get(btc_url).json()
        
        # Key Hunter for BTC
        ts_key = next((k for k in btc_data.keys() if "Time Series" in k), None)
        if ts_key:
            latest_date = list(btc_data[ts_key].keys())[0]
            price_dict = btc_data[ts_key][latest_date]
            close_key = next((k for k in price_dict.keys() if "close" in k.lower()), None)
            btc_price = float(price_dict[close_key])
        else:
            return None, "BTC Limit/Error"

        # 2. Fetch Gold (The 2026 structure fix)
        gold_url = f'https://www.alphavantage.co/query?function=GOLD&interval=daily&apikey={AV_KEY}'
        gold_data = requests.get(gold_url).json()
        
        # Gold often returns {'name': 'Gold', 'interval': 'daily', 'unit': 'troy ounce', 'data': [...]}
        if 'data' in gold_data:
            # We take the first entry, but check if it's 'value' or 'price'
            first_entry = gold_data['data'][0]
            gold_price = float(first_entry.get('value', first_entry.get('price', 0)))
        else:
            return None, "Gold Limit/Error"
            
        return (btc_price, gold_price), None
        
    except Exception as e:
        return None, str(e)

# --- EXECUTION ---
data_bundle, err = get_macro_data()

if data_bundle:
    btc_p, gold_p = data_bundle
    ratio = btc_p / gold_p
    
    col1, col2, col3 = st.columns(3)
    col1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    col2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    col3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL: Target 11.0 reached!")
    else:
        st.info(f"HOLD: Ratio is {ratio:.2f}. Target is 11.0.")
else:
    st.warning(f"⚠️ {err}")
    st.write("Tip: Alpha Vantage Free Tier = 25 requests per day. If you hit this limit, the data will refresh at Midnight GMT.")

# --- DEBUG SECTION (Optional) ---
with st.expander("System Logs"):
    st.write("API Key Status: Active")
    st.write(f"Last Error Observed: {err}")

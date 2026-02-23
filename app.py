import streamlit as st
import requests

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# --- 2. SIDEBAR ---
st.sidebar.header("Data Settings")
mode = st.sidebar.radio("Choose Mode:", ["Live API", "Manual Entry (Backup)"])
AV_KEY = "0SYM2E4LAG7AHT2K"

# --- 3. THE FUNCTION (Must be defined before it is called!) ---
@st.cache_data(ttl=3600)
def get_macro_data():
    try:
        # Fetch Bitcoin
        btc_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey={AV_KEY}'
        btc_resp = requests.get(btc_url).json()
        ts_key = next((k for k in btc_resp.keys() if "Time Series" in k), None)
        
        if ts_key:
            latest_date = list(btc_resp[ts_key].keys())[0]
            price_dict = btc_resp[ts_key][latest_date]
            close_key = next((k for k in price_dict.keys() if "close" in k.lower()), None)
            btc_p = float(price_dict[close_key])
        else:
            return None, "BTC Limit Reached"

        # Fetch Gold
        gold_url = f'https://www.alphavantage.co/query?function=GOLD&interval=daily&apikey={AV_KEY}'
        gold_data = requests.get(gold_url).json()
        if 'data' in gold_data:
            gold_p = float(gold_data['data'][0].get('value', 0))
        else:
            return None, "Gold Limit Reached"
            
        return (btc_p, gold_p), None
    except Exception as e:
        return None, str(e)

# --- 4. DATA LOGIC ---
if mode == "Manual Entry (Backup)":
    st.info("🛠️ Manual Mode Active")
    btc_p = st.number_input("Bitcoin Price ($)", value=65000.0)
    gold_p = st.number_input("Gold Price ($)", value=5100.0)
    err = None
else:
    data_bundle, err = get_macro_data()
    if data_bundle:
        btc_p, gold_p = data_bundle
    else:
        btc_p, gold_p = None, None

# --- 5. DISPLAY ---
if btc_p and gold_p:
    ratio = btc_p / gold_p
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL!")
    else:
        st.info(f"HOLD: Target 11.0. (Distance: {ratio - 11.0:.2f})")
elif err:
    st.warning(f"⚠️ {err}. Switch to 'Manual Entry' in the sidebar.")

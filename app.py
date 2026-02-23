import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# --- 1. SETUP & PAGE CONFIG ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide")
st.title("🏦 2026 Alpha Terminal")

# API Keys
AV_KEY = "0SYM2E4LAG7AHT2K"      
FINNHUB_KEY = "d6e21d1r01qmepi1gg90d6e21d1r01qmepi1gg9g" 

# Initialize Memory
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 2. SIDEBAR SETTINGS ---
st.sidebar.header("Data Settings")
mode = st.sidebar.radio("Choose Mode:", ["Manual Entry (Backup)", "Live API"])

# --- 3. PRICE LOGIC ---
if mode == "Manual Entry (Backup)":
    st.info("🛠️ Manual Mode Active")
    btc_p = st.number_input("Bitcoin Price ($)", value=65000.0)
    gold_p = st.number_input("Gold Price ($)", value=5100.0)
else:
    st.warning("API Mode: Daily limit check...")
    btc_p, gold_p = None, None

# --- 4. CALCULATION & DISPLAY ---
if btc_p and gold_p:
    ratio = btc_p / gold_p
    c1, c2, c3 = st.columns(3)
    c1.metric("BTC/Gold Ratio", f"{ratio:.2f}")
    c2.metric("Bitcoin Price", f"${btc_p:,.2f}")
    c3.metric("Gold Price", f"${gold_p:,.2f}")

    # LOGGING BUTTONS
    col_a, col_b = st.columns(2)
    
    with col_a:
        if st.button("📌 Log Current Ratio"):
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.history.append({"Time": now, "Ratio": round(ratio, 2), "BTC": btc_p, "Gold": gold_p})
            st.toast("Data logged!")

    with col_b:
        if st.session_state.history:
            # Convert history list to a DataFrame for CSV export
            df = pd.DataFrame(st.session_state.history)
            csv = df.to_csv(index=False).encode('utf-8')
            
            st.download_button(
                label="📥 Download History (CSV)",
                data=csv,
                file_name=f"macro_history_{datetime.now().strftime('%Y%m%d')}.csv",
                mime='text/csv',
            )

    # SHOW HISTORY TABLE
    if st.session_state.history:
        st.write("### 📝 Logged Observations")
        st.dataframe(st.session_state.history, use_container_width=True)

    if ratio <= 11.0:
        st.success("🚨 BUY SIGNAL! Ratio reached the 11.0 floor.")
    else:
        st.info(f"HOLD: Target 11.0. (Current: {ratio:.2f})")

# --- 5. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")

try:
    news_url = f"https://finnhub.io/api/v1/news?category=general&token={FINNHUB_KEY}"
    response = requests.get(news_url, timeout=10)
    if response.status_code == 200:
        news_data = response.json()
        for item in news_data[:5]:
            with st.expander(item.get('headline', 'Market Update')):
                st.write(item.get('summary', 'Summary not provided.'))
                st.caption(f"Source: {item.get('source')} | [Read Full Story]({item.get('url')})")
except Exception as e:
    st.error(f"News error: {e}")

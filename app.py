import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. PRO UI THEMING ---
st.set_page_config(page_title="2026 Alpha Terminal", layout="wide", page_icon="🕵️")

# CSS Injection - Fixed Syntax
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #ffffff; }
    .metric-card { background: #11141b; padding: 15px; border-radius: 8px; border: 1px solid #1f2937; }
    .agent-status { font-weight: bold; padding: 5px 10px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIC & DATA ---
if 'history' not in st.session_state:
    st.session_state.history = []

st.sidebar.title("🕵️ Terminal Controls")
btc_p = st.sidebar.number_input("BTC/USD", value=68420.0)
gold_p = st.sidebar.number_input("Gold/Oz", value=5080.0)
ratio = round(btc_p / gold_p, 2)

# --- 3. THE AGENTIC ENGINE ---
st.title("🏦 Alpha Terminal: Agentic Intelligence")

# 2026 Metrics
smf_score = round(np.random.uniform(45, 85), 2) 
volatility = "HIGH" if abs(btc_p - 68000) > 2000 else "STABLE"

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("BTC/Gold Ratio", f"{ratio}")
with col2:
    st.metric("Smart Money Flow", f"{smf_score}%", "Institutional Buy" if smf_score > 60 else "Retail Lead")
with col3:
    st.metric("Market Volatility", volatility)
with col4:
    decision = "ACCUMULATE" if ratio < 13.5 and smf_score > 65 else "HEDGE (GOLD)"
    st.metric("Agentic Signal", decision)

st.divider()

# --- 4. SMART MONEY & CHARTING ---
st.write("### 🧠 AI Agent Reasoning")
c_logic, c_chart = st.columns([1, 2])

with c_logic:
    st.info(f"**Agent ID-2026-X:** Ratio is currently {ratio}. SMF is {smf_score}%.")
    if decision == "ACCUMULATE":
        st.success("✅ **ACTION:** Priority Accumulation.")
    else:
        st.warning("⚠️ **ACTION:** Asset Rotation Advised.")

with c_chart:
    if st.button("📌 Log Agent Snapshot"):
        t = datetime.now().strftime("%H:%M:%S")
        # CONSISTENT NAMES: 'Ratio' and 'Floor'
        st.session_state.history.append({"Time": t, "Ratio": ratio, "Floor": 11.0})
        st.toast("Snapshot Saved")
    
    if len(st.session_state.history) > 1:
        df = pd.DataFrame(st.session_state.history).set_index("Time")
        # Fixed: Checking columns explicitly to avoid KeyError
        cols_to_show = [c for c in ['Ratio', 'Floor'] if c in df.columns]
        st.area_chart(df[cols_to_show], color=["#00d4ff", "#00ff88"])
    else:
        st.caption("Log 2 snapshots to activate the Trend Engine.")

# --- 5. AGENTIC NEWS ---
st.divider()
st.subheader("🌐 Agentic Network & News")
st.markdown("""
- **🤖 Agent Network:** 412 Autonomous nodes are bidding at the 11.5 ratio level.
- **🏛️ Treasury News:** Fed announces 'Agentic Governance' for 2026 liquidity.
- **⛽ Energy Note:** BTC Hashrate spikes as Texas nuclear miners go online.
""")

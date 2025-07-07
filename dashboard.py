import streamlit as st
from angel_api import get_connection, fetch_pcr_data

st.set_page_config(page_title="FS Traders Official", layout="wide")
st.title("📊 FS Traders Official - Live PCR & OI Dashboard")

with st.spinner("Connecting to Angel One API..."):
    conn = get_connection()
    data = fetch_pcr_data(conn)

if "error" in data:
    st.error(f"❌ Failed to fetch data: {data['error']}")
else:
    st.metric("Put/Call Ratio (PCR)", data['pcr'])
    st.metric("Trend", data['trend'])
    st.metric("Total PE OI", data['pe_oi'])
    st.metric("Total CE OI", data['ce_oi'])

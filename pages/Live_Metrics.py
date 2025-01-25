import streamlit as st
import pandas as pd
import altair as alt
import requests
from utils import fetch_live_data, make_donut
from websocket import create_connection, WebSocketConnectionClosedException
import json, threading
# ---------------- Functions -----------------
API_URL = "http://192.168.8.227"

def fetch_live_data():
    ws = create_connection(f"{API_URL}/ws/device_data")
    try:
        while True:
            result = ws.recv()
            if result:
                live_data = json.loads(result)
                previous_data = st.session_state['live_data']
                st.session_state['live_data'] = live_data
                # Pop last item
                if len(st.session_state['recent_data']) > 5:
                    st.session_state['recent_data'].pop(0)
                # Add to front of list
                st.session_state['recent_data'].append(previous_data)

    except WebSocketConnectionClosedException:
        ws.close()
        st.error("WebSocket connection closed unexpectedly")

# Initialize live data in session state if not already there
if 'live_data' not in st.session_state:
    st.session_state['live_data'] = {}
    if 'recent_data' not in st.session_state:
        st.session_state['recent_data'] = []
    # Start the data fetching in a separate thread
    thread = threading.Thread(target=fetch_live_data)
    thread.start()
# ------------------------- UI -----------------------------
st.set_page_config(
    page_title="Live Metrics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navigation Bar
col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("Home.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/Historic_Data.py", label="**Historic Data**", icon="📊")

with col3:
   st.page_link("pages/Live_Metrics.py", label="**Live Metrics**", icon="📈")

with col4:
    st.page_link("pages/Manage_Device.py", label="**Manage Device**", icon="⚙️")

container1 = st.container()
container2 = st.container()

with container1:
    efficiency_col, data_table_col = st.columns(spec=[0.5, 0.5])

    with efficiency_col:
        st.subheader("Power Generation")
        live_efficiency = (st.session_state['live_data'].get("power", 0) / 100) * 100  # Adjust calculation based on actual efficiency logic
        chart = make_donut(input_response=live_efficiency, input_text='Efficiency', input_color='green')
        st.text("Efficiency")
        st.altair_chart(chart, use_container_width=True)
        st.write(f"Panel Angle: {st.session_state['live_data'].get('angle', 0)}°")
        st.write(f"Sun Angle: {st.session_state['live_data'].get('angle', 0) - 10}°")  # Example adjustment for sun angle

    with data_table_col:
        live_df = pd.DataFrame([st.session_state['recent_data'].reverse()])
        styled_df = live_df.style.format({
            "voltage": "{:.1f} V",
            "current": "{:.1f} mA",
            "power": "{:.1f} W",
            "angle": "{:.1f}°"
        }).set_table_styles([
            {'selector': 'th', 'props': [('font-size', '18px'), ('text-align', 'center'), ('font-family', 'Helvetica'), ('background-color', '#48C9B0'), ('color', 'white')]},
            {'selector': 'td', 'props': [('text-align', 'center'), ('font-family', 'Helvetica')]},
            {'selector': 'tr:hover', 'props': [('background-color', '#dddddd')]}
        ])
        st.write("### Solar Panel Data", styled_df)

with container2:
    st.subheader("Current Data")
    cur_data_col1, cur_data_col2, cur_data_col3 = st.columns(3)
    cur_data_col1.metric("Power", f"{st.session_state['live_data'].get('power', 0):.1f} W", "7 W")
    cur_data_col2.metric("Current", f"{st.session_state['live_data'].get('current', 0):.1f} mA", "-2 mA")
    cur_data_col3.metric("Voltage", f"{st.session_state['live_data'].get('voltage', 0):.1f} V", "2 V")

with st.container() as container2:
    st.subheader("Current Data")
    cur_data_col1, cur_data_col2, cur_data_col3 = st.columns(3)
    cur_data_col1.metric("Power", f"{st.session_state['live_data'].get('power', 0):.1f} W", "7 W")
    cur_data_col2.metric("Current", f"{st.session_state['live_data'].get('current', 0):.1f} mA", "-2 mA")
    cur_data_col3.metric("Voltage", f"{st.session_state['live_data'].get('voltage', 0):.1f} V", "2 V")

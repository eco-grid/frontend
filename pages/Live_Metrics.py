import streamlit as st
import pandas as pd
import threading
import time
import requests
from queue import Queue
from utils import make_donut, fetch_current_data



if 'live_data'not in st.session_state:
    st.session_state['live_data'] = fetch_current_data()

if 'current_data' not in st.session_state:
    st.session_state['current_data'] = pd.DataFrame()

st.set_page_config(page_title="Live Metrics", page_icon="📈", layout="wide", initial_sidebar_state="collapsed")

# Navigation Bar
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("Home")
with col2:
    st.button("Historic Data")
with col3:
    st.button("Live Metrics")
with col4:
    st.button("Manage Device")

# Main container for the dashboard
container1 = st.container()
container2 = st.container()

# Update data from the queue

with container1:
    efficiency_col, data_table_col = st.columns([0.5, 0.5])
with efficiency_col:
    st.subheader("Power Generation")
    if 'live_data' in st.session_state:
        power = st.session_state['live_data']['power']
        angle = st.session_state['live_data']['angle']
        live_efficiency = (power / 100) * 100
        chart = make_donut(input_response=live_efficiency, input_text='Efficiency', input_color='green')
        st.altair_chart(chart, use_container_width=True)
        st.write(f"Panel Angle: {angle}°")

with container2:
    st.subheader("Current Data")
    if st.session_state['live_data']:
        print(st.session_state['live_data'])
        cur_data_col1, cur_data_col2, cur_data_col3 = st.columns(3)
        power = st.session_state['live_data']['power']
        current = st.session_state['live_data']['current']
        voltage = st.session_state['live_data']['voltage']
        cur_data_col1.metric("Power", f"{power:.1f} W", "7 W")
        cur_data_col2.metric("Current", f"{current:.1f} mA", "-2 mA")
        cur_data_col3.metric("Voltage", f"{voltage:.1f} V", "2 V")




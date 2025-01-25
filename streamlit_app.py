import streamlit as st
import requests

# API base URL
BASE_URL = "http://localhost:5173"

st.title("Renewable Energy Control System")

# Fetch and display real-time data
st.header("Real-Time Data")
try:
    response = requests.get(f"{BASE_URL}/data")
    if response.status_code == 200:
        data = response.json()
        st.metric("Voltage (kV)", data["voltage"])
        st.metric("Current (A)", data["current"])
        st.metric("Sun Angle (°)", data["angle"])
except Exception as e:
    st.error(f"Error fetching data: {e}")

# Control actions
st.header("Control Panel")
action = st.selectbox("Select Action", ["None", "Adjust Panel", "Emergency Shutdown"])
if st.button("Execute Action"):
    try:
        response = requests.post(f"{BASE_URL}/control", json={"action": action})
        if response.status_code == 200:
            st.success(response.json()["status"])
        else:
            st.error("Failed to execute action")
    except Exception as e:
        st.error(f"Error sending control command: {e}")

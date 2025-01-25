import streamlit as st
import pandas as pd
import streamlit as st
import json
from utils import fetch_historic_data
st.set_page_config(
    page_title="Historic Data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed")
col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("Home.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/Historic_Data.py", label="**Historic Data**", icon="📊")

with col3:
   st.page_link("pages/Live_Metrics.py", label="**Live Metrics**", icon="📈")


with col4:
    st.page_link("pages/Manage_Device.py", label="**Manage Device**", icon="⚙️")

st.subheader("Power Generation")

df = pd.DataFrame({
    "time": ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
    "power": [100, 200, 300, 400, 500, 600, 700],
    "current": [10, 20, 30, 40, 50, 60, 70],
    "voltage": [15, 30, 11, 20, 20, 30, 40],
    
})
#json_data = fetch_historic_data()
#data = json.loads(json_data)  # Converts JSON string to a Python dictionary
#df = pd.DataFrame(data)
st.area_chart(df.set_index("time"))
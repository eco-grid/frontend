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

json_data = fetch_historic_data()
data = json.loads(json_data)  # Converts JSON string to a Python dictionary
df = pd.DataFrame(data)
st.line_chart(df.set_index("Time"))
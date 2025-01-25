import streamlit as st
import pandas as pd
import streamlit as st

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
    "Time": ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
    "Power": [100, 200, 300, 400, 500, 600, 700],
})
st.line_chart(df.set_index("Time"))
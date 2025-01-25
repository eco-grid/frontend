import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",)
col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("Home.py", label="**Home**", icon="🏠")

with col2:
   st.page_link("pages/Historic_Data.py", label="**Historic Data**", icon="📊")

with col3:
   st.page_link("pages/Live_Metrics.py", label="**Live Metrics**", icon="📈")


with col4:
    st.page_link("pages/Manage_Device.py", label="**Manage Device**", icon="⚙️")
st.markdown(
    """
    <style>
    .title-text {
        font-size: 48px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        position: absolute;
        top: 20%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }
    .image-container {
        position: relative;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="image-container">
        <img src="./wind-turbines-and-solar-panels-at-sunset.webp" style="width: 100%; border-radius: 15px;">
        <div class="title-text">Eco-Grid</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Competition Summary")
st.markdown(
    """
    The Eco-Grid application is designed to monitor and control renewable energy power plants, combining real-time 
    data monitoring, automated controls, and emergency safety mechanisms to enhance operational efficiency 
    and environmental sustainability.
    
    Key Features:
    - Real-time voltage, current, power, and sun angle monitoring.
    - Visual representation of metrics for analysis.
    - Emergency shutdown and manual/automatic control for solar panel angles.
    """
)
import streamlit as st
st.set_page_config(
    page_title="Manage Device",
    page_icon="⚙️",
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
# Set up the page
st.title('Solar Panel Angle Adjustment')
st.write("Use the toggle to switch between automatic and manual control of the solar panel angle.")

# Toggle for manual or automatic mode
is_manual = st.toggle("Manual Mode", False)

if is_manual:
    st.write('Adjust the angle of the solar panel manually using the slider below.')

    # Slider for angle input
    angle = st.slider('Adjust Angle', min_value=0, max_value=180, value=90)
    
    # Button to submit the angle
    if st.button('Submit Angle'):
        st.success(f'Angle set to {angle} degrees manually.')
else:
    st.write("The solar panel is adjusting automatically based on sensors and algorithms.")

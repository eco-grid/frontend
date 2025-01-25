import streamlit as st

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

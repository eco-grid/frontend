import streamlit as st

# Page Navigation
st.sidebar.title("Eco-Grid Navigation")
page = st.sidebar.radio("Go to", ["Info Page", "Real-Time Metrics", "Graphs"])

# Info Page
if page == "Info Page":
    # Display the title image
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
            <img src="frontend/wind-turbines-and-solar-panels-at-sunset.webp" style="width: 100%; border-radius: 15px;">
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

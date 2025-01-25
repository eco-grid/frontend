import streamlit as st
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Historic Data", page_icon="🌳")

graph_col = st.columns(1)


with graph_col:
    st.subheader("Power Generation")
    df = pd.DataFrame({
        "Time": ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
        "Power": [100, 200, 300, 400, 500, 600, 700],
    })
    st.line_chart(df.set_index("Time"))
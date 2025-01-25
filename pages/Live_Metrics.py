import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
st.set_page_config(page_title="Metrics", page_icon="🌳")

cur_data_col, efficiency_col = st.columns(spec=[0.3, 0.7])



#pcv_col1, pcv_col2, pcv_col3 = st.columns(3)
cur_data_col.metric("Power", "100 W", "7 W")
cur_data_col.metric("Current", "9 mph", "-8%")
cur_data_col.metric("Voltage", "12 V", "2 V")


def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text
with efficiency_col:
    st.subheader("Power Generation")
    # Generate the donut chart
    chart = make_donut(input_response=20, input_text='Efficiency', input_color='green')

    # Display the chart in Streamlit
    st.text("Efficiency")
    st.altair_chart(chart, use_container_width=True)
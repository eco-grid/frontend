import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#---------------- Functions -----------------
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
def generate_data():
    return pd.DataFrame({
        "Time": ['2:30', '3:30', '4:30', '5:30', '6:30'],
        "Power (kW)": [5.2, 5.3, 5.1, 5.0, 5.4],
        "Efficiency (%)": [92.5, 93.0, 91.8, 92.2, 93.5]
    })
# Format the 'Time' column to display nicer
#df['Time'] = df['Time'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Styling the DataFrame using Pandas' Styler
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: #53a567; color: white' if v else '' for v in is_max]


#---------------- UI -----------------
st.set_page_config(page_title="Metrics", page_icon="🌳")

cur_data_col, efficiency_col, data_table_col = st.columns(spec=[0.2, 0.3, 0.5])

cur_data_col.metric("Power", "100 W", "7 W")
cur_data_col.metric("Current", "9 mA", "-2 mA")
cur_data_col.metric("Voltage", "12 V", "2 V")


with efficiency_col:
    st.subheader("Power Generation")
    # Generate the donut chart
    chart = make_donut(input_response=20, input_text='Efficiency', input_color='green')

    # Display the chart in Streamlit
    st.text("Efficiency")
    st.altair_chart(chart, use_container_width=True)



# Display the DataFrame
with data_table_col:
    df = generate_data()
    styled_df = df.style.apply(highlight_max, subset=['Power (kW)', 'Efficiency (%)'])\
        .format({'Power (kW)': "{:.1f}", 'Efficiency (%)': "{:.1f}"})\
        .set_table_styles([
            {'selector': 'th', 'props': [('font-size', '18px'), ('text-align', 'center'), ('font-family', 'Helvetica'), ('background-color', '#48C9B0'), ('color', 'white')]},
            {'selector': 'td', 'props': [('text-align', 'center'), ('font-family', 'Helvetica')]},
            {'selector': 'tr:hover', 'props': [('background-color', '#dddddd')]}
        ])
    st.write("### Solar Panel Data", styled_df)
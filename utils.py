import requests
import json
import pandas as pd
import altair as alt
from websocket import create_connection

# Development aided by AI

API_URL = "http://192.168.8.227"
def fetch_live_data():
    ws = create_connection(f"{API_URL}/ws/device_data")
    while True:
        result = ws.recv()
        ws.close()
        return result
def fetch__data():
    try:
        response = requests.get(f"{API_URL}/api/current")
        if response.status_code == 200:
            json_data = response.json()
            if(json_data):
                data = json.loads(json_data)
                return pd.DataFrame(data)
            else:
                return pd.DataFrame()
        else:
            return pd.DataFrame({
                "timestamp": [],
                "voltage": [],
                "current": [],
                "power": [],
                "angle": []
                })
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {"timestamp": "", "voltage": 0, "current": 0, "power": 0, "angle": 0}

def fetch_historic_data():
    try:
        response = requests.get(f"{API_URL}/api/data/historical")
        if response.status_code == 200:
            json_data = response.json()
            if(json_data):
                data = json.loads(json_data)  # Converts JSON string to a Python dictionary
                return pd.DataFrame(data)
            else:
                return pd.DataFrame()
        else:
            return pd.DataFrame()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    
def stop_current_flow():
    try:
        response = requests.post(f"{API_URL}/api/stop")
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error stopping current flow: {e}")
        return False
    
def adjust_panel_angle(new_angle):
    try:
        response = requests.post(f"{API_URL}/api/angle", json={"angle": new_angle})
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error adjusting panel angle: {e}")
        return False
    
def make_donut(input_response, input_text, input_color):
    chart_color = {
        'blue': ['#29b5e8', '#155F7A'],
        'green': ['#27AE60', '#12783D'],
        'orange': ['#F39C12', '#875A12'],
        'red': ['#E74C3C', '#781F16']
    }.get(input_color, ['#29b5e8', '#155F7A'])
    
    source = pd.DataFrame({
        "Topic": ['', input_text],
        "% value": [100 - input_response, input_response]
    })
    source_bg = pd.DataFrame({
        "Topic": ['', input_text],
        "% value": [100, 0]
    })
    
    plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color=alt.Color(
            "Topic:N",
            scale=alt.Scale(domain=[input_text, ''], range=chart_color),
            legend=None,
        ),
    ).properties(width=130, height=130)
    
    text = plot.mark_text(
        align='center', color=chart_color[0], font="Helvetica",
        fontSize=32, fontWeight=500, fontStyle="italic"
    ).encode(text=alt.value(f'{input_response} %'))
    
    plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
        theta="% value",
        color=alt.Color(
            "Topic:N",
            scale=alt.Scale(domain=[input_text, ''], range=chart_color),
            legend=None,
        ),
    ).properties(width=130, height=130)
    return plot_bg + plot + text
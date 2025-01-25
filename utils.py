import requests
import json
import pandas as pd
from websocket import create_connection


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
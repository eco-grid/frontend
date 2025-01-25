import requests
import json
import pandas as pd

API_URL = "http://192.168.8.227"
def fetch_live_data():
    # Replace the URL with the actual endpoint or fetch from serial input
    try:
        response = requests.get("http://your-arduino-endpoint.com/data")  # Example API
        if response.status_code == 200:
            json_data = response.json()
            if(json_data):
                data = json.loads(json_data)  # Converts JSON string to a Python dictionary
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
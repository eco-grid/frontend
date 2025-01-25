import requests

def fetch_live_data():
    # Replace the URL with the actual endpoint or fetch from serial input
    try:
        response = requests.get("http://your-arduino-endpoint.com/data")  # Example API
        if response.status_code == 200:
            return response.json()
        else:
            return {"timestamp": "", "voltage": 0, "current": 0, "power": 0, "angle": 0}
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {"timestamp": "", "voltage": 0, "current": 0, "power": 0, "angle": 0}

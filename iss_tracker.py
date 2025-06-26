import requests
from datetime import datetime

def get_iss_position():
    output = []
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        log_request("ISS Position", "Success")

        position = data['iss_position']
        lat = position['latitude']
        lon = position['longitude']

        output.append("🌍 Current ISS Location:")
        output.append(f" - Latitude: {lat}")
        output.append(f" - Longitude: {lon}")

        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n[{datetime.now()}] ISS Position:\n")
            f.write(f" - Latitude: {lat}\n")
            f.write(f" - Longitude: {lon}\n")

        return "\n".join(output)
    
    except Exception as e:
        log_request("ISS Position", f"Failed - {e}")
        return "❌ Failed to fetch ISS position.\n"

def log_request(action, status):
    with open("logs.txt", "a") as log:
        log.write(f"[{datetime.now()}] {action} - {status}\n")

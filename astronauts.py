import requests
from datetime import datetime

def get_astronauts():
    output = []
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        data = response.json()
        log_request("Astronauts", "Success")

        astronauts = data['people']
        
        # Append to output string
        output.append(f"\nTotal astronauts in space: {data['number']}\n")
        for person in astronauts:
            output.append(f" - {person['name']} aboard {person['craft']}")
        
        # Save to file
        with open("data/iss_data.txt", "a") as f:
            f.write(f"\n[{datetime.now()}] Astronauts in space:\n")
            for person in astronauts:
                f.write(f" - {person['name']} aboard {person['craft']}\n")
        
        return "\n".join(output)

    except Exception as e:
        log_request("Astronauts", f"Failed - {e}")
        return "❌ Failed to fetch astronauts data.\n"

def log_request(action, status):
    with open("logs.txt", "a") as log:
        log.write(f"[{datetime.now()}] {action} - {status}\n")

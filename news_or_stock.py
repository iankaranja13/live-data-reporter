import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_news():
    output = []
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") != "ok":
            raise Exception("NewsAPI error: " + data.get("message", "Unknown"))

        log_request("NewsAPI", "Success")

        output.append("📰 Top 3 U.S. Business Headlines:")
        for article in data['articles']:
            output.append(f" - {article['title']}")

        return "\n".join(output)

    except Exception as e:
        log_request("NewsAPI", f"Failed - {e}")
        return "❌ Failed to fetch news headlines.\n"

def log_request(action, status):
    with open("logs.txt", "a") as log:
        log.write(f"[{datetime.now()}] {action} - {status}\n")

#Stock 
# import requests
# from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_stock_price():
#     output = []
#     api_key = os.getenv("STOCK_API_KEY")
#     symbol = "IBM"
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
    
#     try:
#         response = requests.get(url)
#         data = response.json()

#         if "Time Series (5min)" not in data:
#             raise Exception("Alpha Vantage error: " + data.get("Note", "Unknown error"))

#         log_request("Stock Price", "Success")

#         latest_timestamp = list(data["Time Series (5min)"].keys())[0]
#         open_price = data["Time Series (5min)"][latest_timestamp]["1. open"]

#         output.append("📈 IBM Stock Info:")
#         output.append(f" - Time: {latest_timestamp}")
#         output.append(f" - Opening Price: ${open_price}")

#         return "\n".join(output)

#     except Exception as e:
#         log_request("Stock Price", f"Failed - {e}")
#         return "❌ Failed to fetch IBM stock data.\n"

# def log_request(action, status):
#     with open("logs.txt", "a") as log:
#         log.write(f"[{datetime.now()}] {action} - {status}\n")

import requests
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import schedule
import time

# Function to fetch and store data
def fetch_and_store_data():
    today = datetime.now().strftime("%Y-%m-%d")
    last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    
    BASE_URL = "https://api.acleddata.com/acled/read"
    API_KEY = "txFE-Z*qVYsSNcFBGL1j"  
    EMAIL = "anoutsala@berkeley.edu" 
    
    params = {
        "key": API_KEY,
        "email": EMAIL,
        "start_date": last_month,
        "end_date": today,
        "format": "json",
        "limit": 1000,
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            df = pd.DataFrame(data)
            conn = sqlite3.connect("conflict_data.db")
            df.to_sql("conflicts", conn, if_exists="append", index=False)
            conn.close()
            print(f"Data successfully fetched and updated on {datetime.now()}.")
        else:
            print("No new data to update.")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        print(response.json())

fetch_and_store_data()

# Schedule the task to run every 24 hours
schedule.every(24).hours.do(fetch_and_store_data)

# Run the schedule
print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(1)

import datetime
import json
import os
import requests

def get_weather_data():
    API_KEY = os.environ.get("API_KEY")
    BASE_URL = "http://api.weatherstack.com/current"
    CITY = "Chicago"

    params = {
        "access_key": API_KEY,
        "query": CITY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H")

    with open(f"data/weather_{timestamp}.json", "w") as f:
        json.dump(data, f)

    with open("logs/weather.log", "a") as log_file:
        log_file.write(f"{timestamp}: {data['location']}\n")

    print(data)
    return data

if __name__ == "__main__":
    get_weather_data()

import requests

print("fetch_weather.py is loaded")

import requests

def fetch_weather(api_key, city):
    print("fetch_weather.py is loaded")
    # Example API call
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching weather data")

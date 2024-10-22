from src.fetch_weather import fetch_weather # type: ignore
from src.process_data import process_data # type: ignore

def main():
    api_key = 'API Key'  # Replace with your actual API key
    city = 'London'  # You can change this to any city you want
    weather_data = fetch_weather(api_key, city)
    temperature = process_data(weather_data)
    print(f"The temperature in {city} is {temperature}°C")

if __name__ == "__main__":
    main()

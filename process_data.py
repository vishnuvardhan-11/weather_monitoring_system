def process_data(weather_data):
    # Sample function to process weather data
    if weather_data and "main" in weather_data:
        temperature = weather_data["main"]["temp"]
        return {"temperature": temperature}
    return {}

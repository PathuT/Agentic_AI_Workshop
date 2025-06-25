import requests
import os

def get_weather(city: str) -> str:
    key = os.getenv("WEATHER_API_KEY")
    if not key:
        return "Weather API key not found."
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch weather."
    data = response.json()
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    return f"The weather in {city} is {temp}°C with {condition}."

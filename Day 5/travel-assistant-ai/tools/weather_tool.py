from langchain.tools import tool
from utils.weather_api import get_weather

@tool
def get_weather_tool(city: str) -> str:
    """Returns weather for a given city."""
    return get_weather(city)

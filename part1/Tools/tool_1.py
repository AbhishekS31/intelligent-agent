import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TOMORROW_API_KEY")

def get_weather(city: str) -> str:
    try:
        if not API_KEY:
            return "Weather service not configured properly."

        url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={API_KEY}"
        res = requests.get(url).json()

        daily = res.get("timelines", {}).get("daily", [])
        if not daily:
            return f"Sorry, couldn't fetch weather for '{city}'."

        day = daily[0]["values"]
        temp = day.get("temperatureAvg")
        return f"The weather in {city} today is approximately {temp}°C."
    except:
        return "Failed to retrieve weather data."

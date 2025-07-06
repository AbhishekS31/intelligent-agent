import requests

API_KEY = "qRht5n8sTUo4K5d7wJdgJk2gaskzFZ6A" 

def get_weather(city: str) -> str:
    try:
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

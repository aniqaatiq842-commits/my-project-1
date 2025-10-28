# api/weather.py
from fastapi import FastAPI, Query
import requests

app = FastAPI()  # MUST be named "app"

@app.get("/")
def get_weather(city: str = Query(...)):
    try:
        url = f"http://wttr.in/{city}?format=%C+%t+%h"
        data = requests.get(url).text.strip().split()
        condition = data[0]
        temperature = data[1]
        humidity = data[2]
        return {"city": city, "condition": condition, "temperature": temperature, "humidity": humidity}
    except Exception:
        return {"error": "Unable to fetch weather"}

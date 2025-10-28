# api/agentic.py
from fastapi import FastAPI, Query

app = FastAPI()  # MUST be named "app"

@app.get("/")
def get_advice(condition: str = Query(...), temperature: str = Query(...), humidity: str = Query(...), weather: str = Query(...)):
    risk = 0
    reasons = []
    temp = int(temperature.replace("°C",""))
    hum = int(humidity.replace("%",""))

    if temp > 34: risk +=2; reasons.append("High temperature")
    if hum > 75: risk +=1; reasons.append("High humidity")

    advice = "✅ Safe to go outside"
    if risk >= 2: advice = "⚠️ Moderate risk — take precautions"
    if risk >= 4: advice = "🚨 High risk — avoid outdoor activity"

    return {"advice": advice, "reasons": reasons, "condition": condition}

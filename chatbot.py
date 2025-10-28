# api/chatbot.py
from fastapi import FastAPI, Query

app = FastAPI()  # MUST be named "app"

@app.get("/")
def chatbot(query: str = Query(...)):
    q = query.lower()
    response = "🤖 Sorry, I don’t have data on that yet."
    if "pollution" in q:
        response = "🌫️ Pollution can damage lungs, worsen asthma, increase heart disease risk."
    elif "heat" in q:
        response = "🥵 High temperatures can cause dehydration and heat stress."
    elif "cold" in q:
        response = "❄️ Cold can trigger asthma or joint pain."
    return {"response": response}

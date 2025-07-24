from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow React Native to access this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend host
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY in .env file")

@app.get("/autocomplete")
def autocomplete(input: str):
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input,
        "key": GOOGLE_API_KEY,
        "language": "en",
        "types": "geocode"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        raise HTTPException(status_code=400, detail=data.get("error_message", "Autocomplete failed"))

    return data

@app.get("/place-details")
def place_details(place_id: str):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": GOOGLE_API_KEY,
        "language": "en"
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        raise HTTPException(status_code=400, detail=data.get("error_message", "Place details failed"))

    return data

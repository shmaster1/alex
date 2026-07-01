import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.providers.waves import fetch_conditions, fetch_day7

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/current")
def current():
    wave_height, wind_speed = fetch_conditions()
    return {"wave_height": wave_height, "wind_speed": wind_speed}


@app.get("/forecast")
def forecast():
    try:
        return fetch_day7()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            raise HTTPException(status_code=503, detail="Rate limited by weather provider. Try again later.")
        raise HTTPException(status_code=502, detail="Weather provider error.")

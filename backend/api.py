from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from providers.waves import fetch_conditions, fetch_forecast

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
    return {"days": fetch_forecast()}

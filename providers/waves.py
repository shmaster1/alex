import httpx
from config.config import config

MARINE_API_URL = "https://marine-api.open-meteo.com/v1/marine"
FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_conditions() -> tuple[float, float]:
    wave_response = httpx.get(
        MARINE_API_URL,
        params={
            "latitude": config.latitude,
            "longitude": config.longitude,
            "current": "wave_height",
        },
        timeout=10,
    )
    wave_response.raise_for_status()

    wind_response = httpx.get(
        FORECAST_API_URL,
        params={
            "latitude": config.latitude,
            "longitude": config.longitude,
            "current": "wind_speed_10m,wind_direction_10m",
            "wind_speed_unit": "kn",
        },
        timeout=10,
    )
    wind_response.raise_for_status()

    wave_height = wave_response.json()["current"]["wave_height"]
    wind_speed = wind_response.json()["current"]["wind_speed_10m"]

    return wave_height, wind_speed

from datetime import datetime

import httpx
from backend.config import config

MARINE_API_URL = "https://marine-api.open-meteo.com/v1/marine"
FORECAST_API_URL = "https://api.open-meteo.com/v1/forecast"
DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


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


def fetch_day7() -> dict:
    wave_response = httpx.get(
        MARINE_API_URL,
        params={"latitude": config.latitude, "longitude": config.longitude, "hourly": "wave_height", "forecast_days": 7, "timezone": "auto"},
        timeout=10,
    )
    wave_response.raise_for_status()

    wind_response = httpx.get(
        FORECAST_API_URL,
        params={"latitude": config.latitude, "longitude": config.longitude, "hourly": "wind_speed_10m", "wind_speed_unit": "kn", "forecast_days": 7, "timezone": "auto"},
        timeout=10,
    )
    wind_response.raise_for_status()

    wave_h = wave_response.json()["hourly"]["wave_height"]
    wind_h = wind_response.json()["hourly"]["wind_speed_10m"]
    times  = wave_response.json()["hourly"]["time"]

    am, pm = 6 * 24 + 8, 6 * 24 + 14  # day 7 (index 6), 8am and 2pm
    date = datetime.fromisoformat(times[am])

    return {
        "label":   DAY_NAMES[date.isoweekday() % 7],
        "date":    date.strftime("%d %b"),
        "am_wave": round(wave_h[am] or 0.0, 2),
        "am_wind": round(wind_h[am] or 0.0, 1),
        "pm_wave": round(wave_h[pm] or 0.0, 2),
        "pm_wind": round(wind_h[pm] or 0.0, 1),
    }

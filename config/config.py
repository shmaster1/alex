from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent

class Config(BaseSettings):
    latitude: float
    longitude: float
    wave_height_threshold: float
    wind_max_speed_threshold: float
    wind_min_speed_threshold: float
    req_url: str
    chat_id: int

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8"
    )


config = Config()
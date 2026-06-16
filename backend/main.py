from config.config import config
from providers.waves import fetch_conditions
from notifiers.whatsapp import notify


def run() -> None:
    wave_height, wind_speed = fetch_conditions()
    if wave_height < config.wave_height_threshold and config.wind_min_speed_threshold <= wind_speed <= config.wind_max_speed_threshold:
        notify(f"waves: {wave_height}m , wind: {wind_speed}kn")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"err received: {e}")


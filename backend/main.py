from backend.config import config
from backend.providers.waves import fetch_day7
from backend.notifiers.whatsapp import notify


def run() -> None:
    day = fetch_day7()
    am_good = (day['am_wave'] < config.wave_height_threshold and
               config.wind_min_speed_threshold <= day['am_wind'] <= config.wind_max_speed_threshold)
    pm_good = (day['pm_wave'] < config.wave_height_threshold and
               config.wind_min_speed_threshold <= day['pm_wind'] <= config.wind_max_speed_threshold)

    if am_good or pm_good:
        periods = []
        if am_good:
            periods.append(f"AM: waves {day['am_wave']}m, wind {day['am_wind']}kn")
        if pm_good:
            periods.append(f"PM: waves {day['pm_wave']}m, wind {day['pm_wind']}kn")
        notify(f"Good conditions in 7 days ({day['label']}, {day['date']}): {' | '.join(periods)}")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"err received: {e}")

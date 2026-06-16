import requests
from backend.config import config


def notify(text):
    url = config.req_url
    payload = {
        "chat_id": config.chat_id,
        "text": f"🌊 {text}"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"WhatsApp notify failed: {e}")
        raise

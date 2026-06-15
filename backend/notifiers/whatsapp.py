import requests
from config.config import config


def notify(text):
    url = config.req_url
    payload = {
        "chat_id": config.chat_id,
        "text": f"🌊 {text}"
    }
    requests.post(url, json=payload)

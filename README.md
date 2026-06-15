# Alex — Wave Alert

Checks wave height once a day and sends a WhatsApp notification if it's below your threshold.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env .env
```

Edit `.env`:
```
LATITUDE=32.0853
LONGITUDE=34.7818
WAVE_HEIGHT_THRESHOLD=1.5

CALLMEBOT_PHONE=+972xxxxxxxxx
CALLMEBOT_API_KEY=your_key_here
```

### 3. Get your CallMeBot API key
1. Add **+34 644 48 19 16** to your WhatsApp contacts
2. Send this message to that number: `I allow callmebot to send me messages`
3. You'll receive your API key via WhatsApp within a minute

### 4. Run
```bash
python main.py
```

## Schedule (run once a day)

**Mac/Linux — cron:**
```bash
crontab -e
# add:
0 7 * * * /usr/bin/python3 /path/to/alex/main.py
```

## Data source

[Open-Meteo Marine API](https://open-meteo.com/en/docs/marine-weather-api) — free, no API key required.

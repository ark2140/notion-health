import requests
import os
from datetime import datetime

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "ntn_D42510382927IzfqpWSZF6OecQvcntjG9axVgk7lNRab4u")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "1cf0fd61b25481a4bc81d1ed92b5f7b6")

def send_to_notion(data):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    date_str = data.get("date", datetime.today().strftime('%Y-%m-%d'))

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Date": {"date": {"start": date_str}},
            "Weight": {"number": float(data.get("weight", 0))},
            "RHR": {"number": float(data.get("rhr", 0))},
            "HRV": {"number": float(data.get("hrv", 0))},
            "Steps": {"number": int(data.get("steps", 0))},
            "VO2 Max": {"number": float(data.get("vo2max", 0))},
            "Sleep Hours": {"number": float(data.get("sleep_hours", 0))}
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if not response.ok:
        raise Exception(f"Failed to create Notion page: {response.text}")
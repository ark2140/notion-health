from fastapi import FastAPI, Request
import httpx
from datetime import datetime

app = FastAPI()

# Hardcoded for personal use
NOTION_SECRET = "ntn_D42510382927IzfqpWSZF6OecQvcntjG9axVgk7lNRab4u"
NOTION_DATABASE_ID = "1cf0fd61b25481a4bc81d1ed92b5f7b6"

@app.post("/webhook")
async def receive_health_data(request: Request):
    body = await request.json()

    notion_data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Date": {"date": {"start": datetime.now().isoformat()}},
            "HRV": {"number": body.get("HRV")},
            "RHR": {"number": body.get("RHR")},
            "VO2 Max": {"number": body.get("VO2")},
            "Steps": {"number": body.get("Steps")},
            "Weight": {"number": body.get("Weight")},
            "Sleep Hours": {"number": body.get("Sleep")}
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.notion.com/v1/pages",
            headers={
                "Authorization": f"Bearer {NOTION_SECRET}",
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28"
            },
            json=notion_data
        )

    return {"status": "ok", "notion_response": response.json()}

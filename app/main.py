from fastapi import FastAPI, Query, Depends
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
event_collection = db["events"]

# Event model
class Event(BaseModel):
    name: str
    date: datetime
    description: Optional[str] = None
    visibility: str  # "public", "private", "university-only"

# Create an event
@app.post("/events/", response_model=dict)
async def create_event(event: Event):
    event_dict = event.dict()
    event_dict["created_at"] = datetime.utcnow()
    result = await event_collection.insert_one(event_dict)
    return {"id": str(result.inserted_id), "message": "Event created successfully"}

# Get events with filtering
@app.get("/events/", response_model=List[Event])
async def get_events(
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    visibility: Optional[str] = Query(None)
):
    query = {}
    if start_time and end_time:
        query["date"] = {"$gte": start_time, "$lte": end_time}
    if visibility:
        query["visibility"] = visibility
    
    events = await event_collection.find(query).to_list(length=100)
    return events

# Event integrations will be placed in separate files (Google Calendar, Slack, LumaEvents, LLM Processing)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

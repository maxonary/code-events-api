from datetime import datetime
from app.database import event_collection
from app.models import Event

# Create an event in the database
async def create_event_service(event: Event):
    event_dict = event.dict()
    event_dict["created_at"] = datetime.utcnow()

    # Insert event into MongoDB
    result = await event_collection.insert_one(event_dict)
    
    return {
        "id": str(result.inserted_id),
        "message": "Event created successfully",
        "event": event_dict
    }

# Get events with optional filtering
async def get_events_service(start_time, end_time, visibility):
    query = {}

    # Filtering by time range
    if start_time and end_time:
        query["date"] = {"$gte": start_time, "$lte": end_time}
    
    # Filtering by visibility
    if visibility:
        query["visibility"] = visibility

    # Fetch events from MongoDB
    events = await event_collection.find(query).to_list(length=100)

    return [
        {
            "id": str(event["_id"]),
            "name": event["name"],
            "date": event["date"],
            "description": event.get("description", ""),
            "visibility": event["visibility"],
            "location": event.get("location", ""),
            "link": event.get("link", ""),
            "created_at": event.get("created_at")
        }
        for event in events
    ]

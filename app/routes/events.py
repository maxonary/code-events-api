from fastapi import APIRouter, Query
from typing import Optional, List
from datetime import datetime
from app.models import Event
from app.services.event_service import create_event_service, get_events_service

router = APIRouter()

# Create an event
@router.post("/", response_model=dict)
async def create_event(event: Event):
    return await create_event_service(event)

# Get events with filtering
@router.get("/", response_model=List[Event])
async def get_events(
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    visibility: Optional[str] = Query(None)
):
    return await get_events_service(start_time, end_time, visibility)

from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from datetime import datetime
from app.models import EventCreate, EventResponse
from app.services.event_service import create_event_service, get_events_service
from app.database import get_db

router = APIRouter()

# Create an event
@router.post("/", response_model=dict)
async def create_event(event: EventCreate, db: AsyncSession = Depends(get_db)):
    return await create_event_service(event, db)

# Get events with filtering
@router.get("/", response_model=List[EventResponse])
async def get_events(
    db: AsyncSession = Depends(get_db),
    start_time: Optional[datetime] = Query(None),
    end_time: Optional[datetime] = Query(None),
    visibility: Optional[str] = Query(None)
):
    return await get_events_service(db, start_time, end_time, visibility)

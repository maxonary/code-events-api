from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload
from app.models import Event, EventCreate, EventResponse
from typing import Optional, List
from datetime import datetime

async def create_event_service(event_data: EventCreate, db: AsyncSession) -> dict:
    """Create a new event"""
    db_event = Event(**event_data.model_dump())
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    
    return {
        "id": db_event.id,
        "message": "Event created successfully"
    }

async def get_events_service(
    db: AsyncSession,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    visibility: Optional[str] = None
) -> List[EventResponse]:
    """Get events with optional filtering"""
    query = select(Event)
    
    # Apply filters
    conditions = []
    if start_time:
        conditions.append(Event.date >= start_time)
    if end_time:
        conditions.append(Event.date <= end_time)
    if visibility:
        conditions.append(Event.visibility == visibility)
    
    if conditions:
        query = query.where(and_(*conditions))
    
    # Order by date
    query = query.order_by(Event.date)
    
    result = await db.execute(query)
    events = result.scalars().all()
    
    return [EventResponse.model_validate(event) for event in events]

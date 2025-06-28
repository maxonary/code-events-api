from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.services.jira_service import sync_jira_events, fetch_jira_page, test_jira_connection
from app.database import get_db
from app.models import Event

router = APIRouter()

# API to test Jira connection
@router.get("/test")
async def test_jira():
    return await test_jira_connection()

# API to fetch entire pages from Jira
@router.get("/fetch")
async def fetch_jira():
    return await fetch_jira_page()

# API to sync events from Jira
@router.post("/sync")
async def sync_events(db: AsyncSession = Depends(get_db)):
    return await sync_jira_events(db)

# API to view Jira-imported events
@router.get("/jira-events")
async def get_jira_events(db: AsyncSession = Depends(get_db)):
    # Note: This would need to be updated when you add jira_id field to Event model
    query = select(Event)
    result = await db.execute(query)
    events = result.scalars().all()
    return events
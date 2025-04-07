from fastapi import APIRouter
from app.services.jira_service import sync_jira_events, fetch_jira_page, test_jira_connection
from app.database import event_collection

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
async def sync_events():
    return await sync_jira_events()

# API to view Jira-imported events
@router.get("/jira-events")
async def get_jira_events():
    events = await event_collection.find({"jira_id": {"$exists": True}}).to_list(100)
    return events
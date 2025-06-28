from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.event_service import get_events_service
from app.database import get_db
import datetime

router = APIRouter()

# ICS File Generator
async def generate_ics(db: AsyncSession):
    events = await get_events_service(db, None, None, "public")  # Fetch only public events
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Campus Events//EN\n"

    for event in events:
        event_date = event.date.strftime("%Y%m%dT%H%M%SZ")  # Convert datetime to ICS format
        end_date = event.date + datetime.timedelta(hours=1)  # Default to 1-hour event

        ics_content += f"""BEGIN:VEVENT
SUMMARY:{event.name}
DTSTART:{event_date}
DTEND:{end_date.strftime("%Y%m%dT%H%M%SZ")}
DESCRIPTION:{event.description or ""}
LOCATION:{event.location or ""}
URL:{event.link or ""}
STATUS:CONFIRMED
END:VEVENT
"""

    ics_content += "END:VCALENDAR"
    return ics_content

# FastAPI Route to Serve ICS File
@router.get("/calendar.ics", response_class=Response)
async def serve_ics(db: AsyncSession = Depends(get_db)):
    ics_content = await generate_ics(db)
    return Response(content=ics_content, media_type="text/calendar")

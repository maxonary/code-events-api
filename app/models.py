from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    name: str
    date: datetime
    description: Optional[str] = None
    visibility: str  # "public", "private", "university-only"
    location: Optional[str] = None
    link: Optional[str] = None
    created_at: Optional[datetime] = None
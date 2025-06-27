from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from enum import Enum

class VisibilityEnum(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    UNIVERSITY_ONLY = "university-only"

class Event(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Event name")
    date: datetime = Field(..., description="Event date and time")
    description: Optional[str] = Field(None, max_length=1000, description="Event description")
    visibility: VisibilityEnum = Field(default=VisibilityEnum.PUBLIC, description="Event visibility")
    location: Optional[str] = Field(None, max_length=200, description="Event location")
    link: Optional[str] = Field(None, description="Event link")
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    
    @validator('date')
    def validate_date(cls, v):
        if v < datetime.utcnow():
            raise ValueError('Event date cannot be in the past')
        return v
    
    @validator('link')
    def validate_link(cls, v):
        if v and not v.startswith(('http://', 'https://')):
            raise ValueError('Link must be a valid URL')
        return v

class EventResponse(Event):
    id: str = Field(..., description="Event ID")
    
    class Config:
        from_attributes = True
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, Text, Enum as SQLEnum
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime
from enum import Enum

class VisibilityEnum(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    UNIVERSITY_ONLY = "university-only"

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)
    description = Column(Text, nullable=True)
    visibility = Column(SQLEnum(VisibilityEnum), default=VisibilityEnum.PUBLIC, nullable=False)
    location = Column(String(200), nullable=True)
    link = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class EventCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    date: datetime = Field(...)
    description: Optional[str] = Field(None, max_length=1000)
    visibility: VisibilityEnum = Field(default=VisibilityEnum.PUBLIC)
    location: Optional[str] = Field(None, max_length=200)
    link: Optional[str] = Field(None)

class EventResponse(BaseModel):
    id: int
    name: str
    date: datetime
    description: Optional[str]
    visibility: VisibilityEnum
    location: Optional[str]
    link: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
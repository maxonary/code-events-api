from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import events, calendar, jira

app = FastAPI(
    title="Campus Event Organizer API",
    description="A FastAPI-based application for organizing and managing events on a university campus",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(calendar.router, prefix="", tags=["Calendar"])
app.include_router(jira.router, prefix="/jira", tags=["Jira"])

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "campus-event-organizer"}

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Campus Event Organizer API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

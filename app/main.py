from fastapi import FastAPI
from app.routes import events, calendar, jira

app = FastAPI()

# Include routes
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(calendar.router, prefix="", tags=["Calendar"])
app.include_router(jira.router, prefix="/jira", tags=["Jira"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

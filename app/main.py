from fastapi import FastAPI
from app.routes.events import router as event_router
from app.routes.calendar import router as calendar_router

app = FastAPI()

# Include routes
app.include_router(event_router, prefix="/events", tags=["Events"])
app.include_router(calendar_router, prefix="", tags=["Calendar"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

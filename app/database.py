import motor.motor_asyncio
from app.config import MONGO_URI, DB_NAME

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
event_collection = db["events"]

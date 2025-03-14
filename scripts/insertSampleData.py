from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB connection
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client[os.getenv("DB_NAME")] 
collection = db["events"]

# Sample event data
events = [
    {
        "name": "Tech Talk on AI",
        "date": datetime(2025, 4, 1, 14, 0, 0),
        "description": "A discussion on the future of AI and its ethical implications.",
        "visibility": "university-only",
        "created_at": datetime.utcnow()
    },
    {
        "name": "Spring Music Festival",
        "date": datetime(2025, 4, 15, 18, 30, 0),
        "description": "Live music and performances by student bands.",
        "visibility": "public",
        "created_at": datetime.utcnow()
    },
    {
        "name": "Private Leadership Workshop",
        "date": datetime(2025, 3, 25, 9, 0, 0),
        "description": "Exclusive workshop for student council members.",
        "visibility": "private",
        "created_at": datetime.utcnow()
    },
    {
        "name": "Hackathon 2025",
        "date": datetime(2025, 4, 20, 9, 0, 0),
        "description": "24-hour coding challenge with exciting prizes.",
        "visibility": "university-only",
        "created_at": datetime.utcnow()
    }
]

# Insert data into MongoDB
result = collection.insert_many(events)
print(f"Inserted {len(result.inserted_ids)} events into MongoDB.")
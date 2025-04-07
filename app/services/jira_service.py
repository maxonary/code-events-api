import os
import httpx
from dotenv import load_dotenv
from app.database import event_collection
from datetime import datetime

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_PROJECT_KEY = "EV" # Rokas Event Calendar

import base64

# Concatenate email and API token with a colon
auth_value = f"{JIRA_USER_EMAIL}:{JIRA_API_TOKEN}"
# Base64 encode the string
encoded_auth = base64.b64encode(auth_value.encode("utf-8")).decode("utf-8")

HEADERS = {
    "Authorization": f"Basic {encoded_auth}",
    "Content-Type": "application/json"
}

async def test_jira_connection():
    """
    Test the Jira connection by fetching the Jira instance info asynchronously.
    """
    url = f"{JIRA_BASE_URL}/rest/api/3/myself"  # This will fetch information about the authenticated user.

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)

    if response.status_code == 200:
        return {"message": "Connection successful!", "jira_user_info": response.json()}
    else:
        return {"error": f"Failed to connect to Jira: {response.text}"}

async def fetch_jira_page():
    """
    Fetches event issues from Jira using JQL query.
    """
    url = f"{JIRA_BASE_URL}/rest/api/3/project/{JIRA_PROJECT_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch Jira page: {response.text}")
    
    return response.json()

async def fetch_jira_events():
    """
    Fetches event issues from Jira using JQL query.
    """
    url = f"{JIRA_BASE_URL}/rest/api/3/search"
    jql_query = f'project="{JIRA_PROJECT_KEY}" ORDER BY created DESC'

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS, params={"jql": jql_query, "maxResults": 20})
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch Jira events: {response.text}")
    
    return response.json().get("issues", [])

async def sync_jira_events():
    """
    Fetches events from Jira and updates them in MongoDB.
    """
    jira_events = await fetch_jira_events()
    events_to_insert = []

    for issue in jira_events:
        event_data = {
            "jira_id": issue["id"],
            "name": issue["fields"]["summary"],
            "date": issue["fields"].get("customfield_10010", None),  # Adjust if Jira has a custom date field
            "description": issue["fields"].get("description", ""),
            "visibility": "public",  # Adjust if needed
            "location": issue["fields"].get("customfield_10020", None),  # Adjust if Jira has a location field
            "link": f"{JIRA_BASE_URL}/browse/{issue['key']}",
            "created_at": datetime.utcnow()
        }
        events_to_insert.append(event_data)

    if events_to_insert:
        await event_collection.insert_many(events_to_insert)
    
    return {"message": f"Synced {len(events_to_insert)} events from Jira"}
# Campus Event Organizer (FastAPI)

This project is a FastAPI-based application for organizing and managing events on a university campus. It allows users to create, retrieve, and filter events based on time range and visibility settings. The application also integrates with Google Calendar, Slack, and LumaEvents, while leveraging an LLM to process event descriptions.

## Features
- **Event Management**: Create, retrieve, and filter events
- **Time Filtering**: Show recent and future events
- **Visibility Options**: Events can be public, private, or university-only
- **MongoDB Storage**: Events are stored in MongoDB for efficient querying
- **Modular Integrations**:
  - **Jira**: Source events from Tickets
  - **Google Calendar**: Sync events
  - **Slack Notifications**: Notify a Slack channel about new events
  - **Luma Events**: Manage RSVPs
  - **LLM Processing**: Automatically process event descriptions

## Tech Stack
- **FastAPI**: API framework
- **MongoDB**: Database (using Motor for async operations)
- **Jira API**: Event sourcing
- **Google Calendar API**: Event synchronization
- **Slack API**: Event sourcing via LLM
- **Luma Events API**: Event management
- **OpenAI API**: Event description processing

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/campus-event-organizer.git
   cd campus-event-organizer
   ```
2. **Create a Virtual Environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Fill out the .env file**
   Copy the .env.example file to .env
   ```sh
   cp .env.example .env
   ```
5. **Start MongoDB**
   Ensure you have MongoDB installed and running:
   ```sh
   mongod --dbpath /path/to/your/db
   ```
6. **Run the FastAPI Server**
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints
### Create an Event
**POST** `/events/`
```json
{
  "name": "Campus Tech Talk",
  "date": "2025-03-15T15:00:00",
  "description": "A discussion on emerging technologies.",
  "visibility": "university-only"
}
```
### Get Events with Filters
**GET** `/events/`
- Optional Query Parameters:
  - `start_time` (ISO format)
  - `end_time` (ISO format)
  - `visibility` (`public`, `private`, `university-only`)

## Upcoming Integrations
- [x] Jira Event Sourcing
- [ ] Google Calendar Sync
- [ ] Slack Event Sourcing
- [ ] LumaEvents API Integration
- [ ] LLM-powered Description Processing

## Contributing
1. Fork the repo and create a new branch.
2. Make your changes and commit them.
3. Submit a pull request!
Contanct Maximilian Arnold for support questions around the setup or database key acess at [email](mailto:maximilian.arnold@code.berlin)

## License
This project is licensed under the Apache 2.0 License.


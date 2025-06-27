# Campus Event Organizer API

A FastAPI-based application for organizing and managing events on a university campus. It allows users to create, retrieve, and filter events based on time range and visibility settings. The application integrates with Google Calendar, Slack, and LumaEvents, while leveraging an LLM to process event descriptions.

## 🚀 Features

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

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **MongoDB**: NoSQL database (using Motor for async operations)
- **Pydantic**: Data validation using Python type annotations
- **Jira API**: Event sourcing from project management
- **Google Calendar API**: Event synchronization
- **Slack API**: Event sourcing via LLM
- **Luma Events API**: Event management
- **OpenAI API**: Event description processing

## 📋 Prerequisites

- Python 3.9 or higher
- MongoDB (local or cloud)
- API keys for integrations (Google, Slack, OpenAI, Jira)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/campus-event-organizer.git
cd campus-event-organizer

# Run the setup script
python scripts/setup_dev.py
```

### Option 2: Manual Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/campus-event-organizer.git
   cd campus-event-organizer
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Install production dependencies
   uv pip install -e .
   
   # Or install with development tools
   uv pip install -e ".[dev]"
   ```

4. **Environment Configuration**
   ```bash
   cp env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Start MongoDB**
   ```bash
   # Local MongoDB
   mongod --dbpath /path/to/your/db
   
   # Or use Docker
   docker run -d -p 27017:27017 --name mongodb mongo:7.0
   ```

6. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

### Option 3: Docker Compose (Easiest)

```bash
# Clone and setup
git clone https://github.com/yourusername/campus-event-organizer.git
cd campus-event-organizer

# Copy environment template
cp env.example .env
# Edit .env with your configuration

# Start services
docker-compose up -d
```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
# Database Configuration
MONGO_URI=mongodb://localhost:27017
DB_NAME=campus_events

# API Keys
GOOGLE_API_KEY=your_google_api_key_here
SLACK_WEBHOOK_URL=your_slack_webhook_url_here
OPENAI_API_KEY=your_openai_api_key_here

# Jira Configuration
JIRA_URL=https://your-domain.atlassian.net
JIRA_USERNAME=your_jira_username
JIRA_API_TOKEN=your_jira_api_token

# Application Settings
DEBUG=True
LOG_LEVEL=INFO
```

## 📚 API Documentation

Once the application is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### Example API Usage

#### Create an Event
```bash
curl -X POST "http://localhost:8000/events/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Campus Tech Talk",
    "date": "2025-03-15T15:00:00",
    "description": "A discussion on emerging technologies.",
    "visibility": "university-only",
    "location": "Main Auditorium"
  }'
```

#### Get Events with Filters
```bash
# Get all events
curl "http://localhost:8000/events/"

# Filter by visibility
curl "http://localhost:8000/events/?visibility=public"

# Filter by time range
curl "http://localhost:8000/events/?start_time=2025-01-01T00:00:00&end_time=2025-12-31T23:59:59"
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_events.py
```

## 🚀 Deployment

### Docker Deployment

```bash
# Build and run with Docker
docker build -t campus-event-organizer .
docker run -p 8000:8000 --env-file .env campus-event-organizer
```

### Legacy Deployment (requires requirements.txt)

If your deployment platform requires `requirements.txt`:

```bash
# Generate requirements.txt from pyproject.toml
make generate-requirements

# This creates:
# - requirements.txt (production dependencies)
# - requirements-dev.txt (development dependencies)
```

### Production Considerations

1. **Environment Variables**: Use proper secrets management
2. **Database**: Use MongoDB Atlas or managed MongoDB service
3. **CORS**: Configure allowed origins for production
4. **Logging**: Set up proper logging and monitoring
5. **SSL/TLS**: Use HTTPS in production
6. **Rate Limiting**: Implement API rate limiting
7. **Health Checks**: Monitor application health

### Deployment Platforms

- **Heroku**: Use the provided Dockerfile
- **AWS**: Deploy to ECS or EKS
- **Google Cloud**: Deploy to Cloud Run or GKE
- **Azure**: Deploy to Container Instances or AKS

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Development

### Project Structure
```
code-events-api/
├── app/
│   ├── config.py          # Configuration management
│   ├── database.py        # Database connection
│   ├── main.py           # FastAPI application
│   ├── models.py         # Pydantic models
│   ├── routes/           # API routes
│   ├── services/         # Business logic
│   └── utils/            # Utilities
├── tests/                # Test files
├── scripts/              # Development scripts
├── docker-compose.yml    # Docker services
├── Dockerfile           # Container configuration
└── pyproject.toml       # Project metadata and dependencies
```

### Code Style

This project follows PEP 8 and uses:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Development Commands

```bash
# Install development dependencies
make install-dev

# Run development server
make run

# Format code
make format

# Run tests
make test

# Run all quality checks
make check

# Generate requirements.txt (if needed)
make generate-requirements
```

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support questions around setup or database access, contact Maximilian Arnold at [email](mailto:maximilian.arnold@code.berlin)


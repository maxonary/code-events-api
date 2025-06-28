from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    # Database Configuration
    database_url: str = "postgresql://postgres:password@localhost:5432/campus_events"
    
    # API Keys
    google_api_key: Optional[str] = None
    slack_webhook_url: Optional[str] = None
    openai_api_key: Optional[str] = None
    
    # Jira Configuration
    jira_url: Optional[str] = None
    jira_username: Optional[str] = None
    jira_api_token: Optional[str] = None
    
    # Application Settings
    debug: bool = True
    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS Settings
    cors_origins: list = ["*"]
    
    @field_validator('database_url')
    @classmethod
    def validate_database_url(cls, v):
        if not v.startswith(('postgresql://', 'postgresql+asyncpg://')):
            raise ValueError('Invalid PostgreSQL URL')
        return v
    
    @field_validator('log_level')
    @classmethod
    def validate_log_level(cls, v):
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f'Log level must be one of {valid_levels}')
        return v.upper()
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Create settings instance
settings = Settings()

# Backward compatibility
DATABASE_URL = settings.database_url
GOOGLE_API_KEY = settings.google_api_key
SLACK_WEBHOOK_URL = settings.slack_webhook_url
OPENAI_API_KEY = settings.openai_api_key

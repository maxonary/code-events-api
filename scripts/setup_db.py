#!/usr/bin/env python3
"""
Database setup script for Campus Event Organizer API
"""
import subprocess
import sys
from pathlib import Path

def run_command(command: str, description: str) -> bool:
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def setup_database():
    """Setup the database with migrations"""
    print("🗄️  Setting up PostgreSQL database")
    print("=" * 50)
    
    # Check if .env exists
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file not found. Creating from template...")
        if Path("env.example").exists():
            run_command("cp env.example .env", "Copying environment template")
            print("📝 Please edit .env file with your database configuration")
        else:
            print("❌ env.example not found. Please create .env file manually")
            return False
    
    # Create initial migration
    if not run_command("alembic revision --autogenerate -m 'create events table'", "Creating initial migration"):
        print("❌ Failed to create migration")
        return False
    
    # Apply migrations
    if not run_command("alembic upgrade head", "Applying migrations"):
        print("❌ Failed to apply migrations")
        return False
    
    print("\n🎉 Database setup completed!")
    print("\nNext steps:")
    print("1. Start the application: docker-compose up")
    print("2. Or run locally: uvicorn app.main:app --reload")
    print("3. Visit http://localhost:8000/docs for API documentation")

if __name__ == "__main__":
    setup_database() 
#!/usr/bin/env python3
"""
Development setup script for Campus Event Organizer API
"""
import os
import sys
import subprocess
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

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9 or higher is required")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")

def setup_environment():
    """Setup the development environment"""
    print("🚀 Setting up Campus Event Organizer API development environment")
    print("=" * 60)
    
    # Check Python version
    check_python_version()
    
    # Check if .env file exists
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  .env file not found. Creating from template...")
        if Path("env.example").exists():
            run_command("cp env.example .env", "Copying environment template")
            print("📝 Please edit .env file with your configuration")
        else:
            print("❌ env.example not found. Please create .env file manually")
    
    # Install dependencies
    if not run_command("uv pip install -e .", "Installing dependencies"):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Check if MongoDB is running
    print("🔍 Checking MongoDB connection...")
    try:
        import motor.motor_asyncio
        client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
        print("✅ MongoDB connection successful")
    except Exception as e:
        print(f"⚠️  MongoDB connection failed: {e}")
        print("💡 Make sure MongoDB is running or use Docker Compose")
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Edit .env file with your API keys and configuration")
    print("2. Start the application: uvicorn app.main:app --reload")
    print("3. Or use Docker Compose: docker-compose up")
    print("4. Visit http://localhost:8000/docs for API documentation")

if __name__ == "__main__":
    setup_environment() 
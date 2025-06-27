#!/usr/bin/env python3
"""
Generate requirements.txt from pyproject.toml
Useful for deployment scenarios that require requirements.txt
"""
import subprocess
import sys
from pathlib import Path

def generate_requirements():
    """Generate requirements.txt from pyproject.toml"""
    try:
        # Generate requirements.txt for production dependencies
        subprocess.run([
            "uv", "pip", "compile", 
            "--pyproject", "pyproject.toml",
            "--output-file", "requirements.txt"
        ], check=True)
        
        print("✅ Generated requirements.txt from pyproject.toml")
        
        # Also generate dev requirements
        subprocess.run([
            "uv", "pip", "compile", 
            "--pyproject", "pyproject.toml",
            "--extra", "dev",
            "--output-file", "requirements-dev.txt"
        ], check=True)
        
        print("✅ Generated requirements-dev.txt for development dependencies")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to generate requirements: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ uv not found. Please install uv: pip install uv")
        sys.exit(1)

if __name__ == "__main__":
    generate_requirements() 
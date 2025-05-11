import os
import sys
import subprocess
from pathlib import Path

def setup_project():
    """Set up the project structure and database"""
    print("Setting up project structure and database...")
    # Run the setup script
    import setup
    print("Setup completed successfully!")

def run_streamlit():
    """Run the Streamlit application"""
    print("Starting Streamlit application...")
    # Run the Streamlit app
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app/main.py"])

def main():
    # Check if the database exists
    db_path = Path('database/projects.db')
    if not db_path.exists():
        setup_project()
    
    # Run the Streamlit app
    run_streamlit()

if __name__ == "__main__":
    main()
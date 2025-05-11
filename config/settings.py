import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# Project paths
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATABASE_PATH = os.path.join(PROJECT_ROOT, 'database', 'projects.db')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Application settings
APP_NAME = "AI-Powered Business/Systems Analyst"
APP_VERSION = "1.0.0"
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

# CrewAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
DEFAULT_AI_MODEL = os.getenv('DEFAULT_AI_MODEL', 'gpt-4')

# Database settings
DATABASE_URL = os.getenv('DATABASE_URL', f'sqlite:///{DATABASE_PATH}')

# Streamlit settings
STREAMLIT_PORT = int(os.getenv('STREAMLIT_PORT', '8501'))
STREAMLIT_HOST = os.getenv('STREAMLIT_HOST', 'localhost')
# AI-Powered Business/Systems Analyst

This project implements an AI-powered Business/Systems Analyst platform with a Streamlit web interface and CrewAI for automating the Software Development Life Cycle (SDLC).

## Features

- **AI-Powered SDLC Automation**: Leverages CrewAI to automate different phases of the SDLC
- **Project Management**: Track and manage projects, phases, tasks, and test cases
- **Professional Web Interface**: Built with Streamlit for intuitive project monitoring and management
- **Database Integration**: Store and retrieve project data and generated documentation

## Project Structure

```
├── app/                    # Streamlit web application
│   ├── pages/             # Additional pages for the Streamlit app
│   └── components/        # Reusable UI components
├── crews/                 # CrewAI implementation
│   ├── agents/            # Individual AI agents for SDLC phases
│   └── tasks/             # Task definitions for agents
├── database/              # Database models and connection
├── models/                # Data models
├── utils/                 # Utility functions
└── config/                # Configuration files
```

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Set up the database: `python setup_db.py`
3. Run the Streamlit app: `streamlit run app/main.py`

## Technologies Used

- **Streamlit**: Web interface
- **CrewAI**: AI agent orchestration
- **SQLite/SQLAlchemy**: Database management
- **Python**: Core programming language
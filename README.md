# AI-Powered Business/Systems Analyst

This project implements an AI-powered Business/Systems Analyst platform with a Streamlit web interface and CrewAI for automating the Software Development Life Cycle (SDLC).

## Features

- **AI-Powered SDLC Automation**: Leverages CrewAI to automate different phases of the SDLC
- **Project Management**: Track and manage projects, phases, tasks, and test cases
- **Professional Web Interface**: Built with Streamlit for intuitive project monitoring and management
- **Database Integration**: Store and retrieve project data and generated documentation
- **AI Crews**: Specialized AI agents that work together to complete SDLC tasks

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

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SDLC2.git
cd SDLC2
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the setup script to initialize the database and project structure:

```bash
python setup.py
```

## Usage

### Running the Application

To start the application, run:

```bash
python run.py
```

This will:
1. Set up the project structure and database (if not already done)
2. Start the Streamlit web application

The application will be available at http://localhost:8501 in your web browser.

### Using the Platform

1. **Dashboard**: View project statistics and overview
2. **Projects**: Create, view, and manage your SDLC projects
3. **Project Details**: Manage phases, tasks, documents, and test cases for each project
4. **AI Crews**: Run specialized AI crews to automate different SDLC phases:
   - Requirements Analysis Crew: Analyzes business needs and creates detailed requirements documents
   - System Design Crew: Designs system architecture and components based on requirements
   - Testing Crew: Creates and executes test cases based on requirements

## AI Crews

The platform uses CrewAI to implement specialized AI crews that can automate different phases of the SDLC:

1. **Requirements Analysis Crew**: Analyzes business needs and creates detailed requirements documents
2. **System Design Crew**: Designs system architecture and components based on requirements
3. **Testing Crew**: Creates and executes test cases based on requirements

Each crew consists of specialized AI agents that work together to complete tasks.

## Database

The application uses SQLite for data storage. The database stores information about:

- Projects
- Phases
- Tasks
- Documents
- Test Cases

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
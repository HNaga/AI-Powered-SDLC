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

## How to Commit to GitHub

This section provides a step-by-step guide on how to commit your changes to GitHub.

### Prerequisites

- [Git](https://git-scm.com/downloads) installed on your local machine
- A [GitHub](https://github.com/) account
- Appropriate permissions to the repository

### Initial Setup

1. **Clone the Repository**
   
   If you haven't already, clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/SDLC2.git
   cd SDLC2
   ```

2. **Configure Git**
   
   Set up your Git identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### Making Changes

1. **Create a Branch**
   
   Always create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   
   Edit files, add new features, fix bugs, etc.

3. **Check Status**
   
   See which files have been modified:
   ```bash
   git status
   ```

4. **Stage Changes**
   
   Add your changes to the staging area:
   ```bash
   # Add specific files
   git add file1.py file2.py
   
   # Add all changed files
   git add .
   ```

5. **Commit Changes**
   
   Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature: brief description of changes"
   ```

### Pushing Changes to GitHub

1. **Push Your Branch**
   
   Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   
   - Go to the repository on GitHub
   - Click on "Pull requests" > "New pull request"
   - Select your branch and create the pull request
   - Add a description of your changes
   - Request reviews if necessary

### Best Practices

1. **Commit Messages**
   
   Write clear, concise commit messages that explain what changes were made and why:
   ```
   Add feature: Implement requirements analysis crew
   
   - Added new agent for requirements gathering
   - Integrated with existing project database
   - Updated documentation
   ```

2. **Pull Before Push**
   
   Always pull the latest changes before pushing:
   ```bash
   git pull origin main
   ```

3. **Resolve Conflicts**
   
   If there are conflicts, resolve them before pushing:
   ```bash
   # After resolving conflicts in your editor
   git add .
   git commit -m "Resolve merge conflicts"
   ```

4. **Keep Branches Updated**
   
   Regularly update your branch with changes from the main branch:
   ```bash
   git checkout main
   git pull
   git checkout your-branch
   git merge main
   ```

5. **Use .gitignore**
   
   This project already has a `.gitignore` file that excludes:
   - Python bytecode files
   - Distribution packages
   - Virtual environments
   - IDE specific files
   - Database files
   - Logs
   - Local configuration
   
   If you need to add more files to ignore, edit the `.gitignore` file.

### Common Git Commands

```bash
# View commit history
git log

# Discard changes in working directory
git checkout -- file.py

# Create and switch to a new branch
git checkout -b branch-name

# Switch to an existing branch
git checkout branch-name

# Merge a branch into current branch
git merge branch-name

# Delete a branch locally
git branch -d branch-name

# Delete a branch on GitHub
git push origin --delete branch-name
```

### Troubleshooting

- **Authentication Issues**: Ensure you have the correct permissions and your SSH keys are set up if using SSH.
- **Large Files**: Avoid committing large files. Use Git LFS if necessary.
- **Commit to Wrong Branch**: Use `git reset` and `git stash` to move changes to the correct branch.

By following these guidelines, you'll maintain a clean and organized Git history for the SDLC2 project.
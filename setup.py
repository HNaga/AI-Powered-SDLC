import os
import sqlite3
from pathlib import Path

# Create necessary directories
directories = [
    'app',
    'app/pages',
    'app/components',
    'crews',
    'crews/agents',
    'crews/tasks',
    'database',
    'models',
    'utils',
    'config',
    'data'
]

for directory in directories:
    Path(directory).mkdir(parents=True, exist_ok=True)
    # Create __init__.py in each directory to make them proper Python packages
    init_file = Path(directory) / '__init__.py'
    if not init_file.exists():
        init_file.touch()

# Set up SQLite database
db_path = Path('database/projects.db')
if not db_path.exists():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Projects table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'Not Started'
    )
    ''')
    
    # Create Phases table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS phases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Not Started',
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    ''')
    
    # Create Tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phase_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Not Started',
        assigned_to TEXT,
        due_date TIMESTAMP,
        FOREIGN KEY (phase_id) REFERENCES phases (id)
    )
    ''')
    
    # Create Documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        name TEXT NOT NULL,
        content TEXT,
        doc_type TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    ''')
    
    # Create TestCases table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        expected_result TEXT,
        actual_result TEXT,
        status TEXT DEFAULT 'Not Run',
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )
    ''')
    
    conn.commit()
    conn.close()
    
    print("Database setup completed successfully!")

print("Project structure created successfully!")
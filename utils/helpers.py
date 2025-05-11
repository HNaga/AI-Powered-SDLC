import datetime
import re
from pathlib import Path
import os

def format_date(date_str):
    """Format a date string for display"""
    if not date_str:
        return ""
    
    try:
        # Parse the date string
        if isinstance(date_str, str):
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        else:
            date_obj = date_str
        
        # Format the date
        return date_obj.strftime('%B %d, %Y')
    except Exception:
        # If parsing fails, try another format
        try:
            if isinstance(date_str, str):
                date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            else:
                date_obj = date_str
            
            return date_obj.strftime('%B %d, %Y')
        except Exception:
            # Return the original string if all parsing fails
            return date_str

def get_status_class(status):
    """Get the CSS class for a status"""
    status = status.lower().replace(' ', '-')
    return f"status-{status}"

def get_status_pill_class(status):
    """Get the CSS class for a status pill"""
    status = status.lower().replace(' ', '-')
    return f"pill-{status}"

def slugify(text):
    """Convert text to a URL-friendly slug"""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove non-alphanumeric characters (except hyphens)
    text = re.sub(r'[^\w\-]', '', text)
    # Remove consecutive hyphens
    text = re.sub(r'\-+', '-', text)
    # Remove leading and trailing hyphens
    text = text.strip('-')
    return text

def ensure_dir_exists(dir_path):
    """Ensure a directory exists"""
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def get_project_root():
    """Get the project root directory"""
    # This assumes the utils directory is directly under the project root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_phase_completion_percentage(phases):
    """Calculate the completion percentage of phases"""
    if not phases:
        return 0
    
    completed_phases = sum(1 for p in phases if p['status'] == 'Completed')
    return (completed_phases / len(phases)) * 100

def get_task_completion_percentage(tasks):
    """Calculate the completion percentage of tasks"""
    if not tasks:
        return 0
    
    completed_tasks = sum(1 for t in tasks if t['status'] == 'Completed')
    return (completed_tasks / len(tasks)) * 100
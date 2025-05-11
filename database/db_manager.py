import sqlite3
import os
from datetime import datetime
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path='database/projects.db'):
        self.db_path = db_path
        self._ensure_db_exists()
    
    def _ensure_db_exists(self):
        """Ensure the database file exists"""
        if not Path(self.db_path).exists():
            # Run the setup script if database doesn't exist
            import setup
    
    def _get_connection(self):
        """Get a connection to the database"""
        return sqlite3.connect(self.db_path)
    
    # Project methods
    def create_project(self, name, description):
        """Create a new project"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO projects (name, description) VALUES (?, ?)",
            (name, description)
        )
        project_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return project_id
    
    def get_projects(self):
        """Get all projects"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects ORDER BY created_at DESC")
        projects = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return projects
    
    def get_project(self, project_id):
        """Get a project by ID"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
        project = cursor.fetchone()
        conn.close()
        return dict(project) if project else None
    
    def update_project(self, project_id, name=None, description=None, status=None):
        """Update a project"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Build update query dynamically based on provided parameters
        update_parts = []
        params = []
        
        if name is not None:
            update_parts.append("name = ?")
            params.append(name)
        
        if description is not None:
            update_parts.append("description = ?")
            params.append(description)
        
        if status is not None:
            update_parts.append("status = ?")
            params.append(status)
        
        if update_parts:
            update_parts.append("updated_at = ?")
            params.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            query = f"UPDATE projects SET {', '.join(update_parts)} WHERE id = ?"
            params.append(project_id)
            
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    # Phase methods
    def create_phase(self, project_id, name, description):
        """Create a new phase"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO phases (project_id, name, description) VALUES (?, ?, ?)",
            (project_id, name, description)
        )
        phase_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return phase_id
    
    def get_phases(self, project_id):
        """Get all phases for a project"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phases WHERE project_id = ? ORDER BY id", (project_id,))
        phases = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return phases
    
    def update_phase(self, phase_id, name=None, description=None, status=None, start_date=None, end_date=None):
        """Update a phase"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Build update query dynamically
        update_parts = []
        params = []
        
        if name is not None:
            update_parts.append("name = ?")
            params.append(name)
        
        if description is not None:
            update_parts.append("description = ?")
            params.append(description)
        
        if status is not None:
            update_parts.append("status = ?")
            params.append(status)
        
        if start_date is not None:
            update_parts.append("start_date = ?")
            params.append(start_date)
        
        if end_date is not None:
            update_parts.append("end_date = ?")
            params.append(end_date)
        
        if update_parts:
            query = f"UPDATE phases SET {', '.join(update_parts)} WHERE id = ?"
            params.append(phase_id)
            
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    # Task methods
    def create_task(self, phase_id, name, description, assigned_to=None, due_date=None):
        """Create a new task"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (phase_id, name, description, assigned_to, due_date) VALUES (?, ?, ?, ?, ?)",
            (phase_id, name, description, assigned_to, due_date)
        )
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return task_id
    
    def get_tasks(self, phase_id):
        """Get all tasks for a phase"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE phase_id = ? ORDER BY id", (phase_id,))
        tasks = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tasks
    
    def update_task(self, task_id, name=None, description=None, status=None, assigned_to=None, due_date=None):
        """Update a task"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Build update query dynamically
        update_parts = []
        params = []
        
        if name is not None:
            update_parts.append("name = ?")
            params.append(name)
        
        if description is not None:
            update_parts.append("description = ?")
            params.append(description)
        
        if status is not None:
            update_parts.append("status = ?")
            params.append(status)
        
        if assigned_to is not None:
            update_parts.append("assigned_to = ?")
            params.append(assigned_to)
        
        if due_date is not None:
            update_parts.append("due_date = ?")
            params.append(due_date)
        
        if update_parts:
            query = f"UPDATE tasks SET {', '.join(update_parts)} WHERE id = ?"
            params.append(task_id)
            
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    # Document methods
    def create_document(self, project_id, name, content, doc_type):
        """Create a new document"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO documents (project_id, name, content, doc_type) VALUES (?, ?, ?, ?)",
            (project_id, name, content, doc_type)
        )
        doc_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return doc_id
    
    def get_documents(self, project_id):
        """Get all documents for a project"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents WHERE project_id = ? ORDER BY created_at DESC", (project_id,))
        documents = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return documents
    
    # Test case methods
    def create_test_case(self, project_id, name, description, expected_result):
        """Create a new test case"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test_cases (project_id, name, description, expected_result) VALUES (?, ?, ?, ?)",
            (project_id, name, description, expected_result)
        )
        test_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return test_id
    
    def get_test_cases(self, project_id):
        """Get all test cases for a project"""
        conn = self._get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_cases WHERE project_id = ? ORDER BY id", (project_id,))
        test_cases = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return test_cases
    
    def update_test_case(self, test_id, actual_result=None, status=None):
        """Update a test case with results"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Build update query dynamically
        update_parts = []
        params = []
        
        if actual_result is not None:
            update_parts.append("actual_result = ?")
            params.append(actual_result)
        
        if status is not None:
            update_parts.append("status = ?")
            params.append(status)
        
        if update_parts:
            query = f"UPDATE test_cases SET {', '.join(update_parts)} WHERE id = ?"
            params.append(test_id)
            
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Task:
    id: Optional[int] = None
    phase_id: int = None
    name: str = ""
    description: str = ""
    status: str = "Not Started"
    assigned_to: Optional[str] = None
    due_date: Optional[str] = None

@dataclass
class Phase:
    id: Optional[int] = None
    project_id: int = None
    name: str = ""
    description: str = ""
    status: str = "Not Started"
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    tasks: List[Task] = None
    
    def __post_init__(self):
        if self.tasks is None:
            self.tasks = []

@dataclass
class Document:
    id: Optional[int] = None
    project_id: int = None
    name: str = ""
    content: str = ""
    doc_type: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class TestCase:
    id: Optional[int] = None
    project_id: int = None
    name: str = ""
    description: str = ""
    expected_result: str = ""
    actual_result: Optional[str] = None
    status: str = "Not Run"

@dataclass
class Project:
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    status: str = "Not Started"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    phases: List[Phase] = None
    documents: List[Document] = None
    test_cases: List[TestCase] = None
    
    def __post_init__(self):
        if self.phases is None:
            self.phases = []
        if self.documents is None:
            self.documents = []
        if self.test_cases is None:
            self.test_cases = []
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
import os

# Add the project root to the path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from database.db_manager import DatabaseManager
from crews.crew_manager import CrewManager

# Initialize the database and crew managers
db = DatabaseManager()
crew_manager = CrewManager()

# Page configuration
st.set_page_config(
    page_title="Project Details - AI-Powered Business/Systems Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #424242;
        margin-bottom: 1rem;
    }
    .card {
        border-radius: 5px;
        padding: 1.5rem;
        background-color: #f8f9fa;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
        margin-bottom: 1.5rem;
    }
    .phase-card {
        border-radius: 5px;
        padding: 1rem;
        background-color: white;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1);
        margin-bottom: 1rem;
    }
    .task-card {
        border-radius: 5px;
        padding: 0.8rem;
        background-color: #f8f9fa;
        border-left: 4px solid #1E88E5;
        margin-bottom: 0.8rem;
    }
    .status-not-started { color: #9E9E9E; }
    .status-in-progress { color: #FFA000; }
    .status-completed { color: #43A047; }
    .status-delayed { color: #E53935; }
    .status-pill {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 10rem;
        font-size: 0.75rem;
        font-weight: 600;
        text-align: center;
    }
    .pill-not-started { background-color: #EEEEEE; color: #616161; }
    .pill-in-progress { background-color: #FFF3E0; color: #E65100; }
    .pill-completed { background-color: #E8F5E9; color: #2E7D32; }
    .pill-delayed { background-color: #FFEBEE; color: #C62828; }
    .pill-not-run { background-color: #E3F2FD; color: #1565C0; }
    .pill-passed { background-color: #E8F5E9; color: #2E7D32; }
    .pill-failed { background-color: #FFEBEE; color: #C62828; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=80)
    st.markdown("<h1 style='font-size: 1.5rem;'>AI-Powered SDLC</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation
    if st.button("Back to Projects"):
        st.switch_page("main.py")

# Get project ID from query params or session state
query_params = st.query_params
project_id = None

if 'project_id' in query_params:
    project_id = int(query_params['project_id'][0])
elif 'selected_project' in st.session_state:
    project_id = st.session_state['selected_project']

if not project_id:
    st.error("No project selected. Please go back to the Projects page and select a project.")
    st.stop()

# Get project details
project = db.get_project(project_id)
if not project:
    st.error("Project not found. Please go back to the Projects page and select a valid project.")
    st.stop()

# Main content
st.markdown(f"<h1 class='main-header'>{project['name']}</h1>", unsafe_allow_html=True)

# Project overview
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("<h2 class='sub-header'>Project Overview</h2>", unsafe_allow_html=True)
    st.markdown(f"""<div class='card'>
        <p><strong>Description:</strong> {project['description']}</p>
        <p><strong>Status:</strong> <span class='status-{project['status'].lower().replace(' ', '-')}'>{project['status']}</span></p>
        <p><strong>Created:</strong> {project['created_at']}</p>
        <p><strong>Last Updated:</strong> {project['updated_at']}</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("<h2 class='sub-header'>Actions</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Update project status
    status_options = ["Not Started", "In Progress", "Completed", "Delayed"]
    new_status = st.selectbox(
        "Update Status",
        status_options,
        index=status_options.index(project['status']) if project['status'] in status_options else 0
    )
    
    if st.button("Update Status"):
        db.update_project(project_id, status=new_status)
        st.success("Status updated!")
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Tabs for different sections
tabs = st.tabs(["Phases & Tasks", "Documents", "Test Cases", "AI Crews"])

# Phases & Tasks tab
with tabs[0]:
    st.markdown("<h2 class='sub-header'>Project Phases</h2>", unsafe_allow_html=True)
    
    # Get phases for this project
    phases = db.get_phases(project_id)
    
    if not phases:
        st.info("No phases found for this project.")
    else:
        # Calculate phase completion percentage
        phase_statuses = [p['status'] for p in phases]
        completed_phases = sum(1 for s in phase_statuses if s == 'Completed')
        completion_percentage = (completed_phases / len(phases)) * 100 if phases else 0
        
        # Progress bar
        st.progress(completion_percentage / 100)
        st.markdown(f"<p style='text-align: center;'><strong>Project Completion:</strong> {completion_percentage:.1f}%</p>", unsafe_allow_html=True)
        
        # Display phases
        for phase in phases:
            with st.expander(f"{phase['name']} - {phase['status']}", expanded=True):
                st.markdown(f"""<div class='phase-card'>
                    <p><strong>Description:</strong> {phase['description']}</p>
                    <p><strong>Status:</strong> <span class='status-pill pill-{phase['status'].lower().replace(' ', '-')}'>{phase['status']}</span></p>
                </div>""", unsafe_allow_html=True)
                
                # Phase actions
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    # Get tasks for this phase
                    tasks = db.get_tasks(phase['id'])
                    
                    if tasks:
                        st.markdown("<strong>Tasks:</strong>", unsafe_allow_html=True)
                        for task in tasks:
                            st.markdown(f"""<div class='task-card'>
                                <p><strong>{task['name']}</strong></p>
                                <p>{task['description']}</p>
                                <p><span class='status-pill pill-{task['status'].lower().replace(' ', '-')}'>{task['status']}</span>
                                {f"<span style='margin-left: 10px;'><strong>Assigned to:</strong> {task['assigned_to']}</span>" if task['assigned_to'] else ""}
                                {f"<span style='margin-left: 10px;'><strong>Due:</strong> {task['due_date']}</span>" if task['due_date'] else ""}</p>
                            </div>""", unsafe_allow_html=True)
                    else:
                        st.info("No tasks found for this phase.")
                
                with col2:
                    # Update phase status
                    status_options = ["Not Started", "In Progress", "Completed", "Delayed"]
                    new_phase_status = st.selectbox(
                        "Update Phase Status",
                        status_options,
                        index=status_options.index(phase['status']) if phase['status'] in status_options else 0,
                        key=f"phase_{phase['id']}"
                    )
                    
                    if st.button("Update", key=f"update_phase_{phase['id']}"):
                        db.update_phase(phase['id'], status=new_phase_status)
                        st.success("Phase status updated!")
                        st.rerun()
                    
                    # Add task button
                    if st.button("Add Task", key=f"add_task_{phase['id']}"):
                        st.session_state['adding_task'] = True
                        st.session_state['current_phase'] = phase['id']
                
                # Add task form
                if st.session_state.get('adding_task', False) and st.session_state.get('current_phase') == phase['id']:
                    with st.form(key=f"task_form_{phase['id']}"):
                        st.markdown("<h4>Add New Task</h4>", unsafe_allow_html=True)
                        task_name = st.text_input("Task Name")
                        task_description = st.text_area("Task Description")
                        task_assigned_to = st.text_input("Assigned To")
                        task_due_date = st.date_input("Due Date")
                        
                        submit_task = st.form_submit_button("Add Task")
                        
                        if submit_task:
                            if not task_name:
                                st.error("Task name is required!")
                            else:
                                # Format due date
                                due_date_str = task_due_date.strftime('%Y-%m-%d') if task_due_date else None
                                
                                # Create task
                                db.create_task(
                                    phase['id'],
                                    task_name,
                                    task_description,
                                    task_assigned_to if task_assigned_to else None,
                                    due_date_str
                                )
                                
                                st.success(f"Task '{task_name}' added successfully!")
                                st.session_state['adding_task'] = False
                                st.rerun()

# Documents tab
with tabs[1]:
    st.markdown("<h2 class='sub-header'>Project Documents</h2>", unsafe_allow_html=True)
    
    # Get documents for this project
    documents = db.get_documents(project_id)
    
    if not documents:
        st.info("No documents found for this project.")
    else:
        for doc in documents:
            with st.expander(f"{doc['name']} ({doc['doc_type']})", expanded=False):
                st.markdown(f"""<div class='card'>
                    <p><strong>Type:</strong> {doc['doc_type']}</p>
                    <p><strong>Created:</strong> {doc['created_at']}</p>
                    <p><strong>Updated:</strong> {doc['updated_at']}</p>
                    <hr>
                    <p>{doc['content']}</p>
                </div>""", unsafe_allow_html=True)
    
    # Add document form
    with st.expander("Add New Document", expanded=False):
        with st.form(key="document_form"):
            doc_name = st.text_input("Document Name")
            doc_type = st.selectbox(
                "Document Type",
                ["Requirements", "Design", "Implementation", "Testing", "User Manual", "Other"]
            )
            doc_content = st.text_area("Document Content", height=300)
            
            submit_doc = st.form_submit_button("Add Document")
            
            if submit_doc:
                if not doc_name or not doc_content:
                    st.error("Document name and content are required!")
                else:
                    # Create document
                    db.create_document(
                        project_id,
                        doc_name,
                        doc_content,
                        doc_type
                    )
                    
                    st.success(f"Document '{doc_name}' added successfully!")
                    st.rerun()

# Test Cases tab
with tabs[2]:
    st.markdown("<h2 class='sub-header'>Test Cases</h2>", unsafe_allow_html=True)
    
    # Get test cases for this project
    test_cases = db.get_test_cases(project_id)
    
    if not test_cases:
        st.info("No test cases found for this project.")
    else:
        for test in test_cases:
            with st.expander(f"{test['name']} - {test['status']}", expanded=False):
                st.markdown(f"""<div class='card'>
                    <p><strong>Description:</strong> {test['description']}</p>
                    <p><strong>Expected Result:</strong> {test['expected_result']}</p>
                    <p><strong>Status:</strong> <span class='status-pill pill-{test['status'].lower().replace(' ', '-')}'>{test['status']}</span></p>
                    {f"<p><strong>Actual Result:</strong> {test['actual_result']}</p>" if test['actual_result'] else ""}
                </div>""", unsafe_allow_html=True)
                
                # Update test case status
                col1, col2 = st.columns([3, 1])
                
                with col2:
                    status_options = ["Not Run", "Passed", "Failed"]
                    new_test_status = st.selectbox(
                        "Update Status",
                        status_options,
                        index=status_options.index(test['status']) if test['status'] in status_options else 0,
                        key=f"test_{test['id']}"
                    )
                    
                    actual_result = st.text_area(
                        "Actual Result",
                        value=test['actual_result'] if test['actual_result'] else "",
                        key=f"result_{test['id']}"
                    )
                    
                    if st.button("Update", key=f"update_test_{test['id']}"):
                        db.update_test_case(
                            test['id'],
                            actual_result=actual_result if actual_result else None,
                            status=new_test_status
                        )
                        st.success("Test case updated!")
                        st.rerun()
    
    # Add test case form
    with st.expander("Add New Test Case", expanded=False):
        with st.form(key="test_case_form"):
            test_name = st.text_input("Test Case Name")
            test_description = st.text_area("Test Case Description")
            test_expected = st.text_area("Expected Result")
            
            submit_test = st.form_submit_button("Add Test Case")
            
            if submit_test:
                if not test_name or not test_expected:
                    st.error("Test case name and expected result are required!")
                else:
                    # Create test case
                    db.create_test_case(
                        project_id,
                        test_name,
                        test_description,
                        test_expected
                    )
                    
                    st.success(f"Test case '{test_name}' added successfully!")
                    st.rerun()

# AI Crews tab
with tabs[3]:
    st.markdown("<h2 class='sub-header'>AI Crews</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <p>Run AI Crews to automate different phases of the SDLC for this project.</p>
        <p>Each crew consists of specialized AI agents that work together to complete tasks.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display available crews
    crews = [
        {
            "id": "requirements",
            "name": "Requirements Analysis Crew",
            "description": "Analyzes business needs and creates detailed requirements documents",
            "phase": "Requirements Analysis"
        },
        {
            "id": "design",
            "name": "System Design Crew",
            "description": "Designs system architecture and components based on requirements",
            "phase": "System Design"
        },
        {
            "id": "testing",
            "name": "Testing Crew",
            "description": "Creates and executes test cases based on requirements",
            "phase": "Testing"
        }
    ]
    
    for crew in crews:
        st.markdown(f"""
        <div class='card'>
            <h3>{crew['name']}</h3>
            <p>{crew['description']}</p>
            <p><strong>Associated Phase:</strong> {crew['phase']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Run {crew['name']}", key=f"run_{crew['id']}"):
            with st.spinner(f"Running {crew['name']}... This may take several minutes."):
                try:
                    # Call the crew manager to run the crew
                    result = crew_manager.run_crew(crew['id'], project_id)
                    
                    # Show success message
                    st.success(f"{crew['name']} completed successfully!")
                    st.markdown("### Result:")
                    st.markdown(result.raw if hasattr(result, 'raw') else str(result))
                    
                    # Refresh the page to show the new document
                    st.rerun()
                except Exception as e:
                    st.error(f"Error running crew: {str(e)}")
    
    # Note: The crew execution is now handled directly by the crew_manager.run_crew() method
    # which creates the document and updates the phase status automatically

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    AI-Powered Business/Systems Analyst Platform | &copy; 2023
</div>
""", unsafe_allow_html=True)
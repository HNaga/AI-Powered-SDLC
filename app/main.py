import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
import os

# Add the project root to the path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import DatabaseManager

# Initialize the database manager
db = DatabaseManager()

# Page configuration
st.set_page_config(
    page_title="AI-Powered Business/Systems Analyst",
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
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 5px;
        background-color: white;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.1);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E88E5;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #616161;
    }
    .status-not-started { color: #9E9E9E; }
    .status-in-progress { color: #FFA000; }
    .status-completed { color: #43A047; }
    .status-delayed { color: #E53935; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=80)
    st.markdown("<h1 style='font-size: 1.5rem;'>AI-Powered SDLC</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["Dashboard", "Projects", "Create Project", "AI Crews", "Documentation"]
    )

# Main content
if page == "Dashboard":
    st.markdown("<h1 class='main-header'>SDLC Dashboard</h1>", unsafe_allow_html=True)
    
    # Get all projects
    projects = db.get_projects()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>{}</div>
            <div class='metric-label'>Total Projects</div>
        </div>
        """.format(len(projects)), unsafe_allow_html=True)
    
    with col2:
        in_progress = sum(1 for p in projects if p['status'] == 'In Progress')
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>{}</div>
            <div class='metric-label'>In Progress</div>
        </div>
        """.format(in_progress), unsafe_allow_html=True)
    
    with col3:
        completed = sum(1 for p in projects if p['status'] == 'Completed')
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>{}</div>
            <div class='metric-label'>Completed</div>
        </div>
        """.format(completed), unsafe_allow_html=True)
    
    with col4:
        not_started = sum(1 for p in projects if p['status'] == 'Not Started')
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>{}</div>
            <div class='metric-label'>Not Started</div>
        </div>
        """.format(not_started), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent projects
    st.markdown("<h2 class='sub-header'>Recent Projects</h2>", unsafe_allow_html=True)
    
    if projects:
        # Convert to DataFrame for easier display
        df_projects = pd.DataFrame(projects)
        
        # Format dates
        df_projects['created_at'] = pd.to_datetime(df_projects['created_at'])
        df_projects['created_at'] = df_projects['created_at'].dt.strftime('%Y-%m-%d')
        
        # Display recent projects
        st.dataframe(
            df_projects[['id', 'name', 'status', 'created_at']].head(5),
            column_config={
                "id": "ID",
                "name": "Project Name",
                "status": "Status",
                "created_at": "Created Date"
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.info("No projects found. Create a new project to get started!")
    
    # Project status chart
    if projects:
        st.markdown("<h2 class='sub-header'>Project Status Overview</h2>", unsafe_allow_html=True)
        
        # Count projects by status
        status_counts = {}
        for p in projects:
            status = p['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        # Create DataFrame for chart
        df_status = pd.DataFrame({
            'Status': list(status_counts.keys()),
            'Count': list(status_counts.values())
        })
        
        # Create pie chart
        fig = px.pie(
            df_status, 
            values='Count', 
            names='Status',
            color='Status',
            color_discrete_map={
                'Not Started': '#9E9E9E',
                'In Progress': '#FFA000',
                'Completed': '#43A047',
                'Delayed': '#E53935'
            }
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        
        st.plotly_chart(fig, use_container_width=True)

elif page == "Projects":
    st.markdown("<h1 class='main-header'>Projects</h1>", unsafe_allow_html=True)
    
    # Get all projects
    projects = db.get_projects()
    
    if not projects:
        st.info("No projects found. Create a new project to get started!")
    else:
        # Filter options
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Not Started", "In Progress", "Completed", "Delayed"]
        )
        
        filtered_projects = projects
        if status_filter != "All":
            filtered_projects = [p for p in projects if p['status'] == status_filter]
        
        # Display projects as cards
        for project in filtered_projects:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""<div class='card'>
                    <h3>{project['name']}</h3>
                    <p>{project['description']}</p>
                    <p><strong>Status:</strong> <span class='status-{project['status'].lower().replace(' ', '-')}'>{project['status']}</span></p>
                    <p><strong>Created:</strong> {project['created_at']}</p>
                </div>""", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("View Details", key=f"view_{project['id']}"):
                    st.session_state['selected_project'] = project['id']
                    st.rerun()
                
                st.markdown("<br>", unsafe_allow_html=True)
                status_options = ["Not Started", "In Progress", "Completed", "Delayed"]
                new_status = st.selectbox(
                    "Update Status",
                    status_options,
                    index=status_options.index(project['status']) if project['status'] in status_options else 0,
                    key=f"status_{project['id']}"
                )
                
                if st.button("Update", key=f"update_{project['id']}"):
                    db.update_project(project['id'], status=new_status)
                    st.success("Status updated!")
                    st.rerun()

elif page == "Create Project":
    st.markdown("<h1 class='main-header'>Create New Project</h1>", unsafe_allow_html=True)
    
    with st.form("project_form"):
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Project Description")
        
        # Default SDLC phases
        st.markdown("<h3>Default SDLC Phases</h3>", unsafe_allow_html=True)
        st.markdown("The following phases will be created automatically:")
        phases = [
            "Requirements Analysis",
            "System Design",
            "Implementation",
            "Testing",
            "Deployment",
            "Maintenance"
        ]
        for phase in phases:
            st.markdown(f"- {phase}")
        
        submitted = st.form_submit_button("Create Project")
        
        if submitted:
            if not project_name:
                st.error("Project name is required!")
            else:
                # Create project
                project_id = db.create_project(project_name, project_description)
                
                # Create default phases
                phase_descriptions = {
                    "Requirements Analysis": "Gather and document project requirements",
                    "System Design": "Design the system architecture and components",
                    "Implementation": "Develop the system according to design specifications",
                    "Testing": "Test the system to ensure it meets requirements",
                    "Deployment": "Deploy the system to production",
                    "Maintenance": "Maintain and update the system as needed"
                }
                
                for phase in phases:
                    db.create_phase(project_id, phase, phase_descriptions[phase])
                
                st.success(f"Project '{project_name}' created successfully!")
                st.markdown("""<a href="#" onclick='window.location.href="?page=Projects"'>View All Projects</a>""", unsafe_allow_html=True)

elif page == "AI Crews":
    st.markdown("<h1 class='main-header'>AI Crews</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>About AI Crews</h3>
        <p>This platform uses CrewAI to automate different phases of the Software Development Life Cycle (SDLC).</p>
        <p>Each crew consists of specialized AI agents that work together to complete tasks in different SDLC phases.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display available crews
    st.markdown("<h2 class='sub-header'>Available Crews</h2>", unsafe_allow_html=True)
    
    crews = [
        {
            "name": "Requirements Analysis Crew",
            "description": "Analyzes business needs and creates detailed requirements documents",
            "agents": ["Business Analyst", "Domain Expert", "Requirements Documenter"]
        },
        {
            "name": "System Design Crew",
            "description": "Designs system architecture and components based on requirements",
            "agents": ["System Architect", "Database Designer", "UI/UX Designer"]
        },
        {
            "name": "Development Crew",
            "description": "Implements the system according to design specifications",
            "agents": ["Backend Developer", "Frontend Developer", "Database Developer"]
        },
        {
            "name": "Testing Crew",
            "description": "Tests the system to ensure it meets requirements",
            "agents": ["Test Manager", "Test Case Designer", "Test Executor"]
        }
    ]
    
    for crew in crews:
        st.markdown(f"""
        <div class='card'>
            <h3>{crew['name']}</h3>
            <p>{crew['description']}</p>
            <p><strong>Agents:</strong> {', '.join(crew['agents'])}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            st.button("Run Crew", key=f"run_{crew['name']}")

elif page == "Documentation":
    st.markdown("<h1 class='main-header'>Documentation</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>About This Platform</h3>
        <p>The AI-Powered Business/Systems Analyst platform is designed to automate and streamline the Software Development Life Cycle (SDLC) using artificial intelligence.</p>
        <p>This platform leverages CrewAI to create specialized AI agents that work together to complete tasks in different SDLC phases.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='sub-header'>User Guide</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>Getting Started</h3>
        <ol>
            <li>Create a new project from the "Create Project" page</li>
            <li>View your projects on the "Projects" page</li>
            <li>Run AI Crews to automate SDLC tasks</li>
            <li>Monitor project progress on the Dashboard</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='card'>
        <h3>AI Crews</h3>
        <p>Each AI Crew consists of specialized agents that work together to complete tasks in different SDLC phases:</p>
        <ul>
            <li><strong>Requirements Analysis Crew:</strong> Analyzes business needs and creates detailed requirements documents</li>
            <li><strong>System Design Crew:</strong> Designs system architecture and components based on requirements</li>
            <li><strong>Development Crew:</strong> Implements the system according to design specifications</li>
            <li><strong>Testing Crew:</strong> Tests the system to ensure it meets requirements</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    AI-Powered Business/Systems Analyst Platform | &copy; 2023
</div>
""", unsafe_allow_html=True)
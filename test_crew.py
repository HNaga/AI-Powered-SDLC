import os
import sys
from crews.crew_manager import CrewManager
from database.db_manager import DatabaseManager

def setup_test_project():
    """Create a test project in the database"""
    db = DatabaseManager()
    
    # Create a test project
    project_name = "Online Grocery Ordering and Delivery"
    project_description = "Online Grocery Ordering and Delivery Mobile Application"
    
    # Check if test project already exists
    projects = db.get_projects()
    test_project = next((p for p in projects if p['name'] == project_name), None)
    
    if test_project:
        print(f"Using existing test project (ID: {test_project['id']})")
        return test_project['id']
    else:
        project_id = db.create_project(project_name, project_description)
        print(f"Created new test project (ID: {project_id})")
        
        # Create default phases
        phases = [
            ("Requirements Analysis", "Gather and document project requirements"),
            ("System Design", "Design the system architecture and components"),
            ("Implementation", "Implement the designed system"),
            ("Testing", "Test the implemented system"),
            ("Deployment", "Deploy the system to production"),
            ("Maintenance", "Maintain and update the system")
        ]
        
        for phase_name, phase_description in phases:
            db.create_phase(project_id, phase_name, phase_description)
        
        return project_id

def run_crew_test(crew_type, project_id):
    """Run a specific crew and display the results"""
    print(f"\n{'=' * 50}")
    print(f"Running {crew_type.upper()} crew for project ID: {project_id}")
    print(f"{'=' * 50}\n")
    
    # Explain the crew's role and dependencies
    if crew_type == "requirements":
        print("The Requirements Analysis crew will gather and document project requirements.")
        print("This is the first step in the development process.")
        print("The output from this crew will be used by the Design crew.")
    elif crew_type == "design":
        print("The System Design crew will create the system architecture based on requirements.")
        print("This crew builds upon the output from the Requirements Analysis crew.")
        print("The output from this crew will be used by the Testing crew.")
    elif crew_type == "testing":
        print("The Testing crew will create test plans and cases based on requirements and design.")
        print("This crew builds upon the outputs from both Requirements and Design crews.")
    
    crew_manager = CrewManager()
    
    try:
        result = crew_manager.run_crew(crew_type, project_id)
        print(f"\n{'=' * 50}")
        print(f"RESULT FROM {crew_type.upper()} CREW:")
        print(f"{'=' * 50}\n")
        print(result)
        return True
    except Exception as e:
        print(f"Error running {crew_type} crew: {str(e)}")
        return False

def main():
    # Ensure environment variables are set
    if not os.getenv("GEMINI_MODEL") or not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_MODEL and GEMINI_API_KEY environment variables must be set.")
        print("Example:")
        print("  set GEMINI_MODEL=gemini-pro")
        print("  set GEMINI_API_KEY=your_api_key")
        return
    
    # Create or get test project
    project_id = setup_test_project()
    
    # Ask user which crew to run
    print("\nWhich crew would you like to test?")
    print("1. Requirements Analysis Crew")
    print("2. System Design Crew")
    print("3. Testing Crew")
    print("4. Run All Crews Sequentially")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        run_crew_test("requirements", project_id)
    elif choice == "2":
        run_crew_test("design", project_id)
    elif choice == "3":
        run_crew_test("testing", project_id)
    elif choice == "4":
        print("\nRunning all crews sequentially...")
        print("This will run each crew in order, with each crew building upon the previous crew's output:")
        print("1. Requirements Analysis → 2. System Design → 3. Testing")
        print("\nEach crew will access and incorporate the documents created by previous crews.")
        
        # Run requirements crew first
        print("\nStep 1: Running Requirements Analysis crew...")
        if run_crew_test("requirements", project_id):
            # If requirements crew succeeds, run design crew
            print("\nStep 2: Running System Design crew...")
            print("The Design crew will use the requirements document created in the previous step.")
            if run_crew_test("design", project_id):
                # If design crew succeeds, run testing crew
                print("\nStep 3: Running Testing crew...")
                print("The Testing crew will use both the requirements and design documents created in previous steps.")
                run_crew_test("testing", project_id)
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
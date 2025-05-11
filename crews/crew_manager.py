from crewai import Crew, Agent, Task, LLM
import os
import sys

llm_model = os.getenv("GEMINI_MODEL")
llm_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(
    model=llm_model,
    api_key=llm_api_key
)
# Add the project root to the path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db_manager import DatabaseManager

class CrewManager:
    def __init__(self):
        self.db = DatabaseManager()
    
    def create_requirements_crew(self, project_id):
        """Create a crew for requirements analysis"""
        # Get project details
        project = self.db.get_project(project_id)
        
        # Create agents
        business_analyst = Agent(
            role="Business Analyst",
            goal="Understand business needs and translate them into system requirements",
           backstory="You are an experienced business analyst with expertise in gathering and analyzing business requirements.",
           llm=llm,
           verbose=True
        )
        
        domain_expert = Agent(
            role="Domain Expert",
            goal="Provide domain-specific knowledge and validate requirements",
            backstory="You have deep knowledge of the business domain and can provide insights into industry-specific requirements.",
            llm=llm,
            verbose=True
        )
        
        requirements_documenter = Agent(
            role="Requirements Documenter",
            goal="Create clear, comprehensive requirements documentation",
            backstory="You specialize in documenting requirements in a clear, structured format that can be easily understood by all stakeholders.",
            llm=llm,
            verbose=True
        )
        
        # Create tasks
        gather_requirements = Task(
            description=f"Gather requirements for project: {project['name']}\n\nProject Description: {project['description']}",
            agent=business_analyst,
            expected_output="A comprehensive list of functional and non-functional requirements",
            output_file="Output/requirements.md"
        )
        
        validate_requirements = Task(
            description="Validate the gathered requirements against domain knowledge and best practices",
            agent=domain_expert,
            expected_output="Validated requirements with domain-specific insights",
            output_file="Output/validated_requirements.md",
            context=[gather_requirements]
        )
        
        document_requirements = Task(
            description="Create a formal requirements document based on the validated requirements",
            agent=requirements_documenter,
            expected_output="A structured requirements document with user stories, acceptance criteria, and prioritization",
            output_file="Output/requirements_document.md",
            context=[validate_requirements]
        )
        
        # Create crew
        crew = Crew(
            agents=[business_analyst, domain_expert, requirements_documenter],
            tasks=[gather_requirements, validate_requirements, document_requirements],
            verbose=True
        )
        
        return crew
    
    def create_design_crew(self, project_id):
        """Create a crew for system design"""
        # Get project details
        project = self.db.get_project(project_id)
        
        # Get requirements document
        documents = self.db.get_documents(project_id)
        requirements_doc = next((doc for doc in documents if doc['doc_type'] == 'Requirements'), None)
        
        if not requirements_doc:
            print("Warning: No requirements document found. Design crew may not have complete context.")
            requirements_content = "No requirements document available"
        else:
            print(f"Found requirements document: {requirements_doc['name']}")
            requirements_content = requirements_doc['content']
        
        # Create agents
        system_architect = Agent(
            role="System Architect",
            goal="Design a robust, scalable system architecture",
            backstory="You are a skilled system architect with experience in designing complex systems.",
            llm=llm,
            verbose=True
        )
        
        database_designer = Agent(
            role="Database Designer",
            goal="Design an efficient, normalized database schema",
            backstory="You specialize in database design and optimization.",
            llm=llm,
            verbose=True
        )
        
        ui_designer = Agent(
            role="UI/UX Designer",
            goal="Create intuitive, user-friendly interface designs",
            backstory="You are an experienced UI/UX designer focused on creating engaging user experiences.",
            llm=llm,
            verbose=True
        )
        
        # Create tasks
        design_architecture = Task(
            description=f"Design system architecture for project: {project['name']}\n\nRequirements: {requirements_content}",
            agent=system_architect,
            expected_output="A comprehensive system architecture document with component diagrams",
            output_file="Output/architecture_document.md"
        )
        
        design_database = Task(
            description="Design database schema based on the system architecture",
            agent=database_designer,
            expected_output="A database schema with entity-relationship diagrams",
            output_file="Output/database_schema.md",
            context=[design_architecture]
        )
        
        design_ui = Task(
            description=f"Create UI/UX designs based on the system architecture and requirements\n\nRequirements: {requirements_content}",
            agent=ui_designer,
            expected_output="UI/UX mockups and user flow diagrams",
            output_file="Output/ui_designs.md",
            context=[design_architecture]
        )
        
        # Create crew
        crew = Crew(
            agents=[system_architect, database_designer, ui_designer],
            tasks=[design_architecture, design_database, design_ui],
            verbose=True
        )
        
        return crew
    
    def create_testing_crew(self, project_id):
        """Create a crew for testing"""
        # Get project details
        project = self.db.get_project(project_id)
        
        # Get requirements and design documents
        documents = self.db.get_documents(project_id)
        requirements_doc = next((doc for doc in documents if doc['doc_type'] == 'Requirements'), None)
        design_doc = next((doc for doc in documents if doc['doc_type'] == 'Design'), None)
        
        if not requirements_doc:
            print("Warning: No requirements document found. Testing crew may not have complete context.")
            requirements_content = "No requirements document available"
        else:
            print(f"Found requirements document: {requirements_doc['name']}")
            requirements_content = requirements_doc['content']
            
        if not design_doc:
            print("Warning: No design document found. Testing crew may not have complete context.")
            design_content = "No design document available"
        else:
            print(f"Found design document: {design_doc['name']}")
            design_content = design_doc['content']
        
        # Create agents
        test_manager = Agent(
            role="Test Manager",
            goal="Plan and coordinate testing activities",
            backstory="You are an experienced test manager with expertise in test planning and coordination.",
            llm=llm,
            verbose=True
        )
        
        test_designer = Agent(
            role="Test Case Designer",
            goal="Design comprehensive test cases",
            backstory="You specialize in creating test cases that thoroughly validate system functionality.",
            llm=llm,
            verbose=True
        )
        
        test_executor = Agent(
            role="Test Executor",
            goal="Execute test cases and report results",
            backstory="You are detail-oriented and skilled at executing test cases and identifying defects.",
            llm=llm,
            verbose=True
        )
        
        # Create tasks
        create_test_plan = Task(
            description=f"Create a test plan for project: {project['name']}\n\nRequirements: {requirements_content}\n\nSystem Design: {design_content}",
            agent=test_manager,
            expected_output="A comprehensive test plan with testing strategy and schedule",
            output_file="Output/test_plan.md"
        )
        
        design_test_cases = Task(
            description=f"Design test cases based on the test plan, requirements, and system design\n\nRequirements: {requirements_content}\n\nSystem Design: {design_content}",
            agent=test_designer,
            expected_output="A set of detailed test cases with steps, expected results, and traceability to requirements",
            output_file="Output/test_cases.md",
            context=[create_test_plan]
        )
        
        execute_tests = Task(
            description="Execute test cases and report results",
            agent=test_executor,
            expected_output="Test execution results with pass/fail status and defect reports",
            output_file="Output/test_results.md",
            context=[design_test_cases]
        )
        
        # Create crew
        crew = Crew(
            agents=[test_manager, test_designer, test_executor],
            tasks=[create_test_plan, design_test_cases, execute_tests],
            verbose=True
        )
        
        return crew
    
    def run_crew(self, crew_type, project_id):
        """Run a specific crew for a project"""
        # Check prerequisites for each crew type
        if crew_type == "design" or crew_type == "testing":
            # Check if requirements document exists
            documents = self.db.get_documents(project_id)
            requirements_doc = next((doc for doc in documents if doc['doc_type'] == 'Requirements'), None)
            if not requirements_doc:
                print(f"Warning: No requirements document found for project {project_id}.")
                print("It's recommended to run the requirements crew first.")
        
        if crew_type == "testing":
            # Check if design document exists
            documents = self.db.get_documents(project_id)
            design_doc = next((doc for doc in documents if doc['doc_type'] == 'Design'), None)
            if not design_doc:
                print(f"Warning: No design document found for project {project_id}.")
                print("It's recommended to run the design crew before the testing crew.")
        
        # Create the appropriate crew
        if crew_type == "requirements":
            crew = self.create_requirements_crew(project_id)
        elif crew_type == "design":
            crew = self.create_design_crew(project_id)
        elif crew_type == "testing":
            crew = self.create_testing_crew(project_id)
        else:
            raise ValueError(f"Unknown crew type: {crew_type}")
        
        print(f"\nStarting {crew_type.capitalize()} crew...")
        # Run the crew
        result = crew.kickoff()
        
        
        # Save the result as a document
        doc_type = {
            "requirements": "Requirements",
            "design": "Design",
            "testing": "Testing"
        }.get(crew_type)
        
        self.db.create_document(
            project_id=project_id,
            name=f"{doc_type} Document",
            content=result.raw,
            doc_type=doc_type
        )
        print(f"\n{doc_type} document saved to database.")
        
        # Update the corresponding phase status
        phases = self.db.get_phases(project_id)
        phase_mapping = {
            "requirements": "Requirements Analysis",
            "design": "System Design",
            "testing": "Testing"
        }
        
        phase_name = phase_mapping.get(crew_type)
        if phase_name:
            phase = next((p for p in phases if p['name'] == phase_name), None)
            if phase:
                self.db.update_phase(phase['id'], status="Completed")
                print(f"Phase '{phase_name}' marked as completed.")
        
        return result
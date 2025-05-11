from crewai import Task
from typing import List, Optional
from crewai import Agent

class SDLCTasks:
    """Factory class for creating SDLC tasks"""
    
    @staticmethod
    def gather_requirements(agent: Agent, project_name: str, project_description: str) -> Task:
        """Create a task for gathering requirements"""
        return Task(
            description=f"Gather requirements for project: {project_name}\n\nProject Description: {project_description}\n\n"
                      f"Your task is to analyze the project description and identify all functional and non-functional requirements. "
                      f"Consider user needs, system constraints, and business objectives. "
                      f"Organize requirements into categories and prioritize them.",
            agent=agent,
            expected_output="A comprehensive list of functional and non-functional requirements"
        )
    
    @staticmethod
    def validate_requirements(agent: Agent, context: List[Task]) -> Task:
        """Create a task for validating requirements"""
        return Task(
            description="Validate the gathered requirements against domain knowledge and best practices.\n\n"
                      "Your task is to review the requirements and ensure they are complete, consistent, and feasible. "
                      "Identify any conflicts, ambiguities, or missing requirements. "
                      "Provide domain-specific insights and recommendations.",
            agent=agent,
            expected_output="Validated requirements with domain-specific insights",
            context=context
        )
    
    @staticmethod
    def document_requirements(agent: Agent, context: List[Task]) -> Task:
        """Create a task for documenting requirements"""
        return Task(
            description="Create a formal requirements document based on the validated requirements.\n\n"
                      "Your task is to organize the requirements into a structured document with clear sections. "
                      "Include user stories, acceptance criteria, and prioritization. "
                      "Ensure the document is clear, concise, and unambiguous.",
            agent=agent,
            expected_output="A structured requirements document with user stories, acceptance criteria, and prioritization",
            context=context
        )
    
    @staticmethod
    def design_architecture(agent: Agent, project_name: str, requirements: str) -> Task:
        """Create a task for designing system architecture"""
        return Task(
            description=f"Design system architecture for project: {project_name}\n\nRequirements: {requirements}\n\n"
                      f"Your task is to create a high-level system architecture that satisfies the requirements. "
                      f"Define system components, their interactions, and data flows. "
                      f"Consider scalability, performance, security, and maintainability.",
            agent=agent,
            expected_output="A comprehensive system architecture document with component diagrams"
        )
    
    @staticmethod
    def design_database(agent: Agent, context: List[Task]) -> Task:
        """Create a task for designing database schema"""
        return Task(
            description="Design database schema based on the system architecture.\n\n"
                      "Your task is to create a database schema that supports the system requirements. "
                      "Define tables, relationships, constraints, and indexes. "
                      "Ensure the schema is normalized and optimized for performance.",
            agent=agent,
            expected_output="A database schema with entity-relationship diagrams",
            context=context
        )
    
    @staticmethod
    def design_ui(agent: Agent, context: List[Task]) -> Task:
        """Create a task for designing UI/UX"""
        return Task(
            description="Create UI/UX designs based on the system architecture and requirements.\n\n"
                      "Your task is to design user interfaces that are intuitive, accessible, and visually appealing. "
                      "Create wireframes for key screens and define user flows. "
                      "Consider usability principles and accessibility guidelines.",
            agent=agent,
            expected_output="UI/UX mockups and user flow diagrams",
            context=context
        )
    
    @staticmethod
    def create_test_plan(agent: Agent, project_name: str, requirements: str) -> Task:
        """Create a task for creating a test plan"""
        return Task(
            description=f"Create a test plan for project: {project_name}\n\nRequirements: {requirements}\n\n"
                      f"Your task is to develop a comprehensive test plan that covers all aspects of the system. "
                      f"Define testing objectives, scope, approach, and schedule. "
                      f"Identify resources needed and risks to be mitigated.",
            agent=agent,
            expected_output="A comprehensive test plan with testing strategy and schedule"
        )
    
    @staticmethod
    def design_test_cases(agent: Agent, context: List[Task]) -> Task:
        """Create a task for designing test cases"""
        return Task(
            description="Design test cases based on the test plan and requirements.\n\n"
                      "Your task is to create detailed test cases that verify system functionality. "
                      "Include test steps, expected results, and traceability to requirements. "
                      "Ensure coverage of both positive and negative scenarios.",
            agent=agent,
            expected_output="A set of detailed test cases with steps, expected results, and traceability to requirements",
            context=context
        )
    
    @staticmethod
    def execute_tests(agent: Agent, context: List[Task]) -> Task:
        """Create a task for executing tests"""
        return Task(
            description="Execute test cases and report results.\n\n"
                      "Your task is to run the test cases and document the results. "
                      "Identify any defects and provide detailed information to reproduce them. "
                      "Categorize defects by severity and priority.",
            agent=agent,
            expected_output="Test execution results with pass/fail status and defect reports",
            context=context
        )
    
    @staticmethod
    def implement_feature(agent: Agent, feature_name: str, feature_description: str, design_docs: List[str]) -> Task:
        """Create a task for implementing a feature"""
        return Task(
            description=f"Implement feature: {feature_name}\n\nFeature Description: {feature_description}\n\n"
                      f"Design Documents: {''.join(design_docs)}\n\n"
                      f"Your task is to implement the feature according to the design specifications. "
                      f"Write clean, maintainable code that follows best practices. "
                      f"Include appropriate error handling and logging.",
            agent=agent,
            expected_output="Implementation code and documentation"
        )
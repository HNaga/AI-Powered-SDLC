from crewai import Agent, LLM
import os
from langchain.tools import BaseTool
from typing import List, Optional
llm_model = os.getenv("GEMINI_MODEL")
llm_api_key = os.getenv("GEMINI_API_KEY")
llm = LLM(
    model=llm_model,
    api_key=llm_api_key
)

class SDLCAgents:
    """Factory class for creating SDLC agents"""
    
    @staticmethod
    def create_business_analyst(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Business Analyst agent"""
        return Agent(
            role="Business Analyst",
            goal="Understand business needs and translate them into system requirements",
            backstory="You are an experienced business analyst with expertise in gathering and analyzing business requirements. "
                     "You excel at interviewing stakeholders, identifying pain points, and documenting clear requirements.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_domain_expert(domain: str, tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Domain Expert agent"""
        return Agent(
            role=f"{domain} Domain Expert",
            goal=f"Provide {domain}-specific knowledge and validate requirements",
            backstory=f"You have deep knowledge of the {domain} domain with years of experience. "
                     f"You understand the specific challenges, regulations, and best practices in {domain}.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_requirements_documenter(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Requirements Documenter agent"""
        return Agent(
            role="Requirements Documenter",
            goal="Create clear, comprehensive requirements documentation",
            backstory="You specialize in documenting requirements in a clear, structured format that can be easily understood by all stakeholders. "
                     "You know how to organize information logically and write unambiguous specifications.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_system_architect(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a System Architect agent"""
        return Agent(
            role="System Architect",
            goal="Design a robust, scalable system architecture",
            backstory="You are a skilled system architect with experience in designing complex systems. "
                     "You understand various architectural patterns and can select the most appropriate one for a given problem.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_database_designer(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Database Designer agent"""
        return Agent(
            role="Database Designer",
            goal="Design an efficient, normalized database schema",
            backstory="You specialize in database design and optimization. "
                     "You understand relational database principles, normalization, and can create efficient schemas.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_ui_designer(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a UI/UX Designer agent"""
        return Agent(
            role="UI/UX Designer",
            goal="Create intuitive, user-friendly interface designs",
            backstory="You are an experienced UI/UX designer focused on creating engaging user experiences. "
                     "You understand design principles, accessibility, and how to create interfaces that users love.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_test_manager(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Test Manager agent"""
        return Agent(
            role="Test Manager",
            goal="Plan and coordinate testing activities",
            backstory="You are an experienced test manager with expertise in test planning and coordination. "
                     "You know how to create comprehensive test strategies and ensure thorough coverage.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_test_designer(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Test Case Designer agent"""
        return Agent(
            role="Test Case Designer",
            goal="Design comprehensive test cases",
            backstory="You specialize in creating test cases that thoroughly validate system functionality. "
                     "You know how to identify edge cases and ensure all requirements are testable.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_test_executor(tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Test Executor agent"""
        return Agent(
            role="Test Executor",
            goal="Execute test cases and report results",
            backstory="You are detail-oriented and skilled at executing test cases and identifying defects. "
                     "You have a keen eye for spotting inconsistencies and can provide clear bug reports.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
    
    @staticmethod
    def create_developer(specialty: str, tools: Optional[List[BaseTool]] = None) -> Agent:
        """Create a Developer agent with a specific specialty"""
        return Agent(
            role=f"{specialty} Developer",
            goal=f"Implement high-quality {specialty} code",
            backstory=f"You are an experienced {specialty} developer with a strong background in software engineering. "
                     f"You write clean, maintainable code and follow best practices.",
            tools=tools or [],
            llm=llm,
            verbose=True
        )
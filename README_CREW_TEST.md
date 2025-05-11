# CrewAI Test Script

This script allows you to test the CrewAI functionality directly without using the UI. It provides a way to verify that the different crews (Requirements, Design, and Testing) are working correctly.

## Prerequisites

1. Make sure you have all the required dependencies installed:
   ```
   pip install crewai
   ```

2. Set up your environment variables for the LLM:
   ```
   set GEMINI_MODEL=gemini-pro
   set GEMINI_API_KEY=your_api_key
   ```

## Running the Test Script

To run the test script, execute the following command:

```
python test_crew.py
```

The script will:

1. Create a test project in the database (or use an existing one if it already exists)
2. Ask you which crew you want to test:
   - Requirements Analysis Crew
   - System Design Crew
   - Testing Crew
   - Run All Crews Sequentially

## How It Works

The test script:

1. Sets up a test project with all the necessary phases
2. Initializes the CrewManager
3. Runs the selected crew(s) for the test project
4. Displays the results of each crew's execution
5. Saves the results to the database as documents

## Troubleshooting

If you encounter any issues:

1. Make sure your environment variables are set correctly
2. Check that the database exists and is properly initialized
3. Verify that all dependencies are installed

## Note

Running the crews sequentially is recommended for the first test, as each crew depends on the output of the previous one:

- The Design crew uses the requirements document created by the Requirements crew
- The Testing crew uses the design documents created by the Design crew
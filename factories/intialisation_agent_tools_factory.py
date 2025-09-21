"""
Tool factory for creating onboarding agent tools.
"""

from langchain_core.tools import tool
from tools.intialisation_agent_tools import (
    fb_get_next_question, fb_mark_question_asked, fb_mark_question_answered,
    fb_check_step_completion, fb_get_progress
)

def make_onboarding_tools(state):
    """Create tools for the initialisation agent."""
    
    @tool("get_next_question", description="Get the next unanswered question from Step 1 onboarding")
    def get_next_question_tool():
        """Get the next unanswered question that needs to be asked to the user."""
        question = fb_get_next_question(state)
        if question:
            return f"Next question (ID: {question['question_id']}): {question['question']}"
        return "All questions have been answered!"

    @tool("mark_question_asked", description="Mark a question as asked in the onboarding progress")
    def mark_question_asked_tool(question_id: str):
        """Mark a question as asked. Use this when you present a question to the user."""
        return fb_mark_question_asked(question_id, state)

    @tool("mark_question_answered", description="Mark a question as answered and store the user's response")
    def mark_question_answered_tool(question_id: str, answer: str):
        """Record the user's answer for a specific question."""
        return fb_mark_question_answered(question_id, answer, state)

    @tool("check_step_completion", description="Check if Step 1 onboarding is completed")
    def check_step_completion_tool():
        """Check if all Step 1 questions have been answered and the step is complete."""
        return fb_check_step_completion(state)

    @tool("get_progress", description="Get current progress summary of Step 1 onboarding")
    def get_progress_tool():
        """Get the current progress of Step 1 onboarding (how many questions answered)."""
        return fb_get_progress(state)

    return [
        get_next_question_tool,
        mark_question_asked_tool, 
        mark_question_answered_tool,
        check_step_completion_tool,
        get_progress_tool
    ]

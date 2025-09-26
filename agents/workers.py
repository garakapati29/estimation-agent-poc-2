"""
Initialisation agent for handling Step 1 onboarding.
"""

import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from prompts.prompts import INTIALISATION_AGENT_PROMPT
# Load environment variables
load_dotenv()

def create_initialisation_agent():
    """Create the initialisation agent for Step 1 onboarding."""

    # Initialize LLM for initialization agent
    model = ChatOpenAI(model="gpt-4o", temperature=0)

    # Get tools from factory    
    # Create and return the react agent
    # This already returns a complete node function that handles tool usage
    agent = create_react_agent(
        tools=[],
        model=model,
        prompt=INTIALISATION_AGENT_PROMPT,
        name="initialisation_agent"
    )

    return agent

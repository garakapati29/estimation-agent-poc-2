"""
Initialisation agent for handling Step 1 onboarding.
"""

from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from prompts.agent_prompts import INITIALISATION_AGENT_PROMPT
from factories.intialisation_agent_tools_factory import make_onboarding_tools
from tools.intialisation_agent_tools import load_onboarding_state

def create_initialisation_agent(state):
    """Create the initialisation agent for Step 1 onboarding."""
    
    # Initialize LLM for initialization agent
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Get tools from factory
    tools = make_onboarding_tools(state)
    
    # Create and return the react agent
    # This already returns a complete node function that handles tool usage
    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=INITIALISATION_AGENT_PROMPT,
        name="initialisation_agent"
    )

    return agent

def create_onboarding_graph():
    """Create the onboarding workflow using the initialization agent."""
    onboarding_state = load_onboarding_state()
    return create_initialisation_agent(onboarding_state)

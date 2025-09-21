"""
Main entry point for the onboarding estimation agent system.
Uses the initialization agent directly.
"""

from agents.workers import create_initialisation_agent
from tools.intialisation_agent_tools import load_onboarding_state

def create_onboarding_graph():
    """Create the onboarding workflow using the initialization agent."""
    onboarding_state = load_onboarding_state()
    return create_initialisation_agent(onboarding_state)

if __name__ == "__main__":
    app = create_onboarding_graph()
    print("Graph compiled successfully!")
"""
Individual JSON management tools for onboarding state.
Each tool handles a specific JSON operation while maintaining state consistency.
"""

import json
import os
import asyncio
from typing import Dict, Any, Optional
from pathlib import Path

# JSON file path
ONBOARDING_JSON_PATH = "data/onboarding_preferences.json"

def ensure_data_directory():
    """Ensure the data directory exists, create it if it doesn't."""
    data_dir = Path(ONBOARDING_JSON_PATH).parent
    data_dir.mkdir(parents=True, exist_ok=True)

def load_onboarding_state():
    """Load onboarding state from disk."""
    if not os.path.exists(ONBOARDING_JSON_PATH):
        # Create initial structure
        initial_data = {
            "overall_progress": {
                "total_number_of_steps": 1,
                "steps_completed": 0,
                "total_number_of_steps_completed": 0,
                "current_step": 1,
                "loadService": False,
                "loadPricingSetup": False,
                "current_step_number": 1
            },
            "step_history": {
                "step_1": {
                    "progress": {
                        "total_number_of_questions": 4,
                        "total_number_of_questions_answered": 0,
                        "current_question_number": 1,
                        "isStepCompleted": False
                    },
                    "question_history": [
                        {
                            "question_id": "q1",
                            "question": "What are your operating regions?",
                            "isAsked": False,
                            "isAnswered": False,
                            "answer": ""
                        },
                        {
                            "question_id": "q2", 
                            "question": "What's your annual estimation bid amount? (USD/CAD)",
                            "isAsked": False,
                            "isAnswered": False,
                            "answer": ""
                        },
                        {
                            "question_id": "q3",
                            "question": "What kind of projects do you handle? (Residential, Commercial, Government & Institutional)",
                            "isAsked": False,
                            "isAnswered": False,
                            "answer": ""
                        },
                        {
                            "question_id": "q4",
                            "question": "What kind of services do you offer? (General Landscaping, Irrigation, Chemical Services, Landscaping Construction, Snow Services)",
                            "isAsked": False,
                            "isAnswered": False,
                            "answer": ""
                        }
                    ]
                }
            }
        }
        save_onboarding_state_sync(initial_data)
        return initial_data
    
    with open(ONBOARDING_JSON_PATH, 'r') as f:
        return json.load(f)

def save_onboarding_state_sync(state):
    """Save onboarding state to disk (synchronous version)."""
    ensure_data_directory()
    with open(ONBOARDING_JSON_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def save_onboarding_state(state):
    """Save onboarding state to disk."""
    save_onboarding_state_sync(state)

def get_next_unanswered_question(state):
    """Get the next unanswered question from the state."""
    for q in state["step_history"]["step_1"]["question_history"]:
        if not q["isAnswered"]:
            return q
    return None

def mark_question_asked(state, question_id):
    """Mark a question as asked in the state."""
    for q in state["step_history"]["step_1"]["question_history"]:
        if q["question_id"] == question_id:
            q["isAsked"] = True
            break
    return state

def mark_question_answered(state, question_id, answer):
    """Mark a question as answered and store the answer."""
    step_data = state["step_history"]["step_1"]
    
    for q in step_data["question_history"]:
        if q["question_id"] == question_id:
            q["isAnswered"] = True
            q["answer"] = answer
            break
    
    # Update progress counters
    answered_count = sum(1 for q in step_data["question_history"] if q["isAnswered"])
    step_data["progress"]["total_number_of_questions_answered"] = answered_count
    
    # Check if step is completed
    if answered_count == step_data["progress"]["total_number_of_questions"]:
        step_data["progress"]["isStepCompleted"] = True
        state["overall_progress"]["steps_completed"] = 1
        state["overall_progress"]["total_number_of_steps_completed"] = 1
    
    return state

def is_step_completed(state):
    """Check if Step 1 is completed."""
    return state["step_history"]["step_1"]["progress"]["isStepCompleted"]

def get_progress_summary(state):
    """Get a summary of current progress."""
    step_data = state["step_history"]["step_1"]["progress"]
    answered = step_data["total_number_of_questions_answered"]
    total = step_data["total_number_of_questions"]
    return f"Progress: {answered}/{total} questions answered"

# File-backed operations that maintain state consistency
def fb_get_next_question(state):
    """File-backed: get next unanswered question."""
    question = get_next_unanswered_question(state)
    return question

def fb_mark_question_asked(question_id, state):
    """File-backed: mark question as asked."""
    mark_question_asked(state, question_id)
    save_onboarding_state(state)
    return f"Marked question {question_id} as asked"

def fb_mark_question_answered(question_id, answer, state):
    """File-backed: mark question as answered."""
    mark_question_answered(state, question_id, answer)
    save_onboarding_state(state)
    return f"Recorded answer for question {question_id}: {answer}"

def fb_check_step_completion(state):
    """File-backed: check if step is completed."""
    completed = is_step_completed(state)
    if completed:
        return "Step 1 is completed! All questions have been answered."
    else:
        progress = get_progress_summary(state)
        return f"Step 1 is not completed. {progress}"

def fb_get_progress(state):
    """File-backed: get progress summary."""
    return get_progress_summary(state)
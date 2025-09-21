# Onboarding Estimation Agent Setup Guide

## Environment Setup

Create a `.env` file in the project root with the following variables:

```bash
# Required
OPENAI_API_KEY=your-openai-api-key-here

# Optional
OPENAI_MODEL=gpt-4o
OPENAI_TEMPERATURE=0
DEBUG=false
LOG_LEVEL=INFO
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   cp .env.template .env
   # Edit .env with your OpenAI API key
   ```

3. **Run the development server:**
   ```bash
   langgraph dev
   ```

4. **Test the system:**
   - Open http://localhost:8123 in your browser
   - Use the LangGraph Studio interface to test your graph

## System Architecture

- **main.py**: Entry point that creates the onboarding agent directly
- **agents/workers.py**: Initialization agent for Step 1 onboarding
- **factories/**: Tool factories for creating agent tools
- **tools/**: Backend tools for state management
- **prompts/**: Agent prompts and instructions

## How It Works

1. **User sends message** → Goes directly to initialization agent
2. **Agent processes message** → Uses tools to handle onboarding
3. **Agent responds** → Provides helpful onboarding assistance
4. **Agent tracks progress** → Shows user their advancement through 4 questions
5. **Agent completes onboarding** → Celebrates when all data is collected

## Error Handling

The system includes comprehensive error handling:
- State validation and structure checking
- File operation safety with atomic writes
- Graceful error messages for users
- Automatic directory creation
- Input validation for all functions

## Data Storage

Onboarding data is stored in `data/onboarding_preferences.json` with automatic:
- Directory creation
- Atomic file writes
- Data structure validation
- Error recovery

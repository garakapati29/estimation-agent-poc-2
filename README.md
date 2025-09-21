# Onboarding Estimation Agent

A streamlined LangGraph-based system for collecting Step 1 onboarding data from users.

## Features

- **Single Agent Architecture**: Direct communication with initialization agent
- **Step-by-Step Onboarding**: Collects 4 required business data points
- **Progress Tracking**: Shows users their advancement through questions
- **Failproof Design**: Handles all user inputs gracefully
- **Async Operations**: Non-blocking file I/O for better performance

## Quick Start

1. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

2. Run the development server:
   ```bash
   langgraph dev
   ```

3. Open http://localhost:8123 to test the system

## Architecture

- **main.py**: Entry point that creates the agent directly
- **agents/workers.py**: Initialization agent with onboarding tools
- **tools/**: Backend tools for state management
- **prompts/**: Agent instructions and conversation rules

## Data Collected

1. Operating regions
2. Annual estimation bid amount (USD/CAD)
3. Project types (Residential/Commercial/Government & Institutional)
4. Services offered (Landscaping/Irrigation/Chemical/etc.)
# Justice Navigator - Journal Companion

## Overview
A CLI-based Journal Companion application that assists users with journal entries by determining their mood, providing empathetic responses, and offering reflective journaling prompts. Built as a capstone project for AI Edge '25 at Columbia University.

## Project Structure
```
/
├── src/
│   ├── app.py                    # Main application entry point
│   ├── chatbot.py                # Unified chatbot with empathetic responses
│   ├── decision_table.py         # Menu decision logic
│   ├── justice_navigator_info.py # Project info display
│   ├── mood_assessment.py        # Mood scale and assessment
│   ├── rules.py                  # CLI argument parsing and validation
│   └── smoke_test.py             # Basic smoke tests
├── test/
│   ├── test_chatbot.py           # Chatbot unit tests
│   ├── test_decision_table.py    # Decision table tests
│   ├── test_mood_assessment.py   # Mood assessment tests
│   └── test_rules.py             # Rules module tests
├── README.md                      # Project documentation
└── reflection.md                  # Team reflection document
```

## How to Run
- Run the app: `cd src && python app.py`
- Version check: `python src/app.py --version`
- Show mood scale: `python src/app.py --show-scale`
- Start with mood: `python src/app.py --mood 4`
- Run tests: `python src/app.py --test`

## Key Features
- **Initial Mood Check-In**: Assesses user mood immediately upon opening
- **Daily Reflection**: Guided daily journaling with mood tracking
- **Weekly Check-In**: Deeper reflection on weekly experiences
- **Chat Mode**: Conversational interaction with the companion
- **Weekly Recap**: AI-generated summary of journal entries
- **Entry Storage**: Saves journal entries to text files

## Mood Scale
1. Very Low (Critical/Distress)
2. Low (Struggling/Stressed)
3. Neutral (Okay/Mixed)
4. Good (Happy/Motivated)
5. Very Good (Thriving/Excited)

## Dependencies
- Python 3.11+
- colorama (colored terminal output)
- pandas (data handling)
- numpy (numerical operations)

## Recent Changes
- December 17, 2025: Initial Replit setup and configuration
- Fixed f-string syntax issues in justice_navigator_info.py

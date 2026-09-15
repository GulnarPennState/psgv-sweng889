# AI-Assisted Development Prompts

## Application Structure

Prompt used:
"Review this project and suggest a simple structure for a Streamlit
application that separates the UI, bike-demand prediction logic,
and local Ollama interaction."

What I used:
I adopted a simple separation of responsibilities using:
- app.py for the Streamlit interface
- predict.py for bike-demand prediction logic
- llm_service.py for local Ollama interaction

This structure keeps the user interface separate from the machine learning logic and from the local LLM integration, which makes the application easier to maintain and test.

## Local LLM Integration

Prompt used:
"Help me connect this Python application to the local Ollama service.
The ML prediction should still be displayed if Ollama is unavailable."

What I used:
I incorporated the suggested fallback behavior so that:
- the machine learning prediction is still shown when the local LLM is unavailable,
- the user sees a clear message if the LLM request fails,
- and the application does not crash when Ollama is offline or unreachable.

This ensures the app satisfies the requirement that the prediction remains available even if the local LLM cannot respond.
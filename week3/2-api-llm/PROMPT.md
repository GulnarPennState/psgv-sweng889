# Generation Prompt

This file documents the exact prompt used to generate this project. It can be used to reproduce the application or understand the development process.

## Prompt Used

```
Create a very small Python application directly inside this existing folder:

`/Users/nathalia/VisualStudio/psgv-sweng889/week3/2-api-llm`

Do NOT create another project folder.

The purpose of this application is to demonstrate a simple API call to an LLM for a software engineering class.

### **Application scenario**

We need to develop a simple **AI Explainer**.

The program should:

1. Ask the user to enter a topic.
2. Send the topic to the OpenAI API.
3. Ask the AI to explain the topic in 2-3 simple sentences.
4. Print the AI response in the terminal.

Example:

Enter a topic: recursion

AI response:

Recursion is a programming technique where a function calls itself to solve smaller versions of the same problem…

### **Files**

Create only these files inside the existing folder:

- `app.py`
- `.env.example`
- `.gitignore`
- `requirements.txt`

### **Python requirements**

Use:

- Python
- the official `openai` Python package
- `python-dotenv`

Keep `app.py` very short and beginner-friendly.

Use the OpenAI Responses API.

The general flow should be:

1. Load environment variables.
2. Create the OpenAI client.
3. Ask the user for a topic using `input()`.
4. Send a prompt asking OpenAI to explain the topic in 2-3 simple sentences.
5. Print the response.
6. Calculate how many tokens you spent with this question and estimate the price for answering the question. Print it.

### **API key security**

The API key must NOT be written directly in the Python code.

Load it from an environment variable:

`OPENAI_API_KEY`

Use `python-dotenv` to load variables from a local `.env` file.

Create `.env.example` containing:

`OPENAI_API_KEY=your_api_key_here`

Do NOT create a `.env` file containing a real API key.

Create `.gitignore` containing at least:

`.env`

`__pycache__/`

This is important because I do not want my API key committed to GitHub.

### **requirements.txt**

Include only the packages needed to run the application.

### **Important**

Keep everything as simple as possible. This is a short classroom demonstration of:

**Python application → OpenAI API → LLM → response**

Do not add a web interface, Flask, FastAPI, database, classes, tests, Docker, or other unnecessary components.
```

## Reproducibility

To reproduce this project with the same or similar output:

1. Use the prompt above with an AI assistant (Claude, ChatGPT, Copilot, etc.)
2. Follow the same requirements and constraints
3. The generated code should be functionally equivalent to `app.py`

This demonstrates the principle of **prompt engineering** and shows how AI can generate consistent, reproducible code when given clear specifications.

## Learning Objectives

This exercise highlights:
- The importance of clear, detailed requirements
- How AI assistants can generate production-ready code
- The reproducibility of AI-generated solutions
- Best practices for API integration and security
- The role of documentation in AI-assisted development

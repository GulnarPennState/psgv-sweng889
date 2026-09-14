# AI Explainer - OpenAI API Demo

A simple Python application that demonstrates how to call the OpenAI API to explain any topic in simple terms. Built for SWENG889 software engineering coursework.

## Features

- ✨ Interactive topic input
- 🤖 AI-powered explanations using OpenAI GPT-4o-mini
- 💰 Token usage tracking and cost estimation
- 🔐 Secure API key management using environment variables

## Prerequisites

- Python 3.8+
- An OpenAI API key (get one at [platform.openai.com](https://platform.openai.com/account/api-keys))

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

3. **Run the application:**
   ```bash
   python3 app.py
   ```

## Usage

```
$ python3 app.py
Enter a topic: recursion

AI response:

Recursion is a programming technique where a function calls itself to solve smaller 
versions of the same problem. It's useful for tasks like traversing trees or searching, 
and requires a base case to stop calling itself. Each recursive call works on a simpler 
version of the original problem until it reaches the base case.

Tokens used: 45
Estimated price: $0.00003429
```

## Files

- `app.py` — Main application script
- `requirements.txt` — Python package dependencies
- `.env.example` — Template for environment variables
- `.gitignore` — Git ignore rules (prevents committing `.env`)
- `PROMPT.md` — The generation prompt used to create this project
- `README.md` — This file

## API Costs

This application uses the `gpt-4o-mini` model, which is one of the most affordable options. Typical usage:
- ~$0.00003 per simple explanation
- Input token pricing: $0.15 per 1M tokens
- Output token pricing: $0.60 per 1M tokens

---

## AI-Assisted Development Note

This project was generated with AI assistance to demonstrate:
- How LLM APIs can be integrated into Python applications
- Best practices for secure API key management
- Simple, readable code for classroom learning
- The reproduction capability of AI-generated code using documented prompts

For transparency and reproducibility, see `PROMPT.md` for the exact prompt used to generate this application. This enables instructors and students to understand how the code was created and to experiment with prompt engineering.

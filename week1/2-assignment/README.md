# SWENG 889 — Week 1 Assignment

## AI-Assisted Software Engineering

This assignment introduces the basic Software Engineering workflow that will be used throughout SWENG 889.

You will work with a small Python application that reads a text report and generates a word cloud. The application runs inside a Docker container so that the required Python environment and dependencies are consistent across different computers.

During the assignment, you will use an AI assistant to propose an additional test, validate the result, and track your changes using Git and GitHub.

> The complete assignment instructions and submission requirements are available in Canvas.

---

## Project Structure

The assignment directory contains:

```text
2-assignment/
├── app.py
├── Dockerfile
├── README.md
├── report.txt
├── requirements.txt
├── tests/
│   └── test_app.py
└── output/
```

### Files

- `app.py` — Python application that processes the report and generates the word cloud.
- `report.txt` — input text used by the application.
- `requirements.txt` — Python dependencies required by the application.
- `Dockerfile` — defines the Docker environment used to run the application.
- `tests/test_app.py` — automated tests for the application.
- `output/` — directory where the generated word cloud is stored.

---

## Prerequisites

Before beginning the assignment, make sure you have:

- Git
- Visual Studio Code
- Docker Desktop
- a GitHub account

You do **not** need to install the Python dependencies directly on your computer. They will be installed inside the Docker image.

See the Week 1 tutorial in Canvas for installation and configuration instructions.

---

## Running the Application

Open a terminal in Visual Studio Code and navigate to this directory:

```bash
cd week1/2-assignment
```

### 1. Build the Docker Image

```bash
docker build -t sweng889-week1 .
```

This creates a Docker image containing Python and the dependencies required by the application.

### 2. Run the Application

On macOS or Linux:

```bash
docker run --rm -v "$(pwd)/output:/app/output" sweng889-week1
```

The application reads `report.txt` and generates:

```text
output/wordcloud.png
```

You should also see a confirmation message similar to:

```text
Word cloud created: output/wordcloud.png
```

Open `wordcloud.png` to inspect the generated result.

---

## Running the Automated Tests

Run the test suite inside Docker:

```bash
docker run --rm sweng889-week1 python -m pytest
```

Review the test results and confirm that the existing tests pass before modifying the application.

---

## Assignment Workflow

For this assignment, you will follow a basic Software Engineering workflow:

```text
Clone
  ↓
Review
  ↓
Build
  ↓
Run
  ↓
Test
  ↓
Create Branch
  ↓
Use AI to Propose a Test
  ↓
Review the AI Suggestion
  ↓
Test Again
  ↓
Inspect Changes
  ↓
Commit
  ↓
Push
```

The detailed steps are provided in the Week 1 tutorial in Canvas.

---

## AI-Assisted Test

As part of the assignment, you will use an AI assistant to propose **one additional automated test** for the application.

The AI-generated suggestion should not be accepted automatically.

You are responsible for reviewing the proposed test, determining whether it is meaningful and correct, modifying it if necessary, and verifying that the final test behaves as expected.

This reflects an important principle of AI-Assisted Software Engineering:

> **AI can assist with engineering work, but the software engineer remains responsible for validating the result.**

---

## Before You Submit

Before submitting the assignment, verify that:

- the application builds successfully with Docker;
- the application generates the expected word cloud;
- the existing automated tests pass;
- you added and validated one additional test;
- all final tests pass;
- you reviewed your changes using Git;
- your work has been committed;
- your assignment branch has been pushed to GitHub.

See Canvas for the complete submission requirements and grading criteria.

---

## Important

Do not commit passwords, API keys, access tokens, credentials, or other sensitive information to the repository.

Generated files such as `output/wordcloud.png` do not need to be committed unless specifically requested in the assignment instructions.

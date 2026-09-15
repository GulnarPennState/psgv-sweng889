## New version of the Copilot instruction for 4-bike-demand2

## Project Goal
Build a simple Python application that predicts bike rental demand using a trained machine learning model and enhances the result with a local LLM explanation or recommendation.

## Development Guidelines
- Use Python.
- Prefer simple, readable implementations.
- Keep the original raw dataset unchanged.
- Keep data preparation, model training, and application code separated.
- Explain significant proposed changes.
- Do not proceed beyond the task currently requested.
- Run and validate generated code when appropriate.
- Report relevant results, assumptions, and problems.

## Core Requirements

### R1. Machine Learning Prediction
- The application must allow the user to enter the required prediction inputs.
- The app must pass those inputs through the model preprocessing pipeline and return a bike-demand prediction.
- Prediction logic must be implemented as a reusable function or module, not embedded directly in the UI.
- Prefer a simple interface (like Streamlit) that is easy to run and test.

### R2. Local LLM Capability
- The application must use a local LLM to provide an explanation, recommendation, summary, or other complementary output.
- The local LLM output should meaningfully add context to the prediction, such as:
  - why demand is likely high or low,
  - recommended operational advice,
  - a concise explanation of the prediction,
  - or a short summary for a user.
- If a local model is used via Ollama or a similar local inference setup, keep the integration simple and robust.
- The LLM response should be optional in execution flow but present when the local model is available.

### R3. Failure Handling
- The application must validate required input before making predictions.
- Missing, blank, or invalid values must produce a clear, user-friendly error message.
- If the local LLM is unavailable, offline, or returns an error, the app must still return the machine learning prediction.
- Any LLM failure should not block the prediction result.
- Error handling should be explicit and user-visible, not silent.

### R4. Separation of Responsibilities
- Keep the code organized into separate modules/components for:
  1. user interface / input collection,
  2. machine learning prediction logic,
  3. local LLM interaction logic.
- Do not mix UI logic with model inference code.
- Do not mix LLM calls directly into the prediction function.
- Keep each component focused and reusable.

## Implementation Guidance
- Use Python and keep the solution simple and readable.
- Preserve the original dataset and preprocessing logic if they already exist.
- Prefer small, testable functions over large monolithic scripts.
- If needed, create a shared configuration or settings module for model path, local LLM endpoint, and app settings.
- Keep error messages clear, concise, and user-friendly.
- If the local LLM is unavailable, log or print a warning but continue prediction processing.

## Expected Behavior
The final application should behave as follows:
1. User provides valid input required for prediction.
2. Machine learning model predicts bike demand.
3. Local LLM generates a brief explanation or recommendation based on the prediction and input context.
4. If input is invalid, the user sees a clear validation message.
5. If the LLM cannot run, the user still receives the prediction without the app crashing.

## Quality Bar
- Simple and maintainable code
- Clear separation of concerns
- Good validation and failure handling
- Minimal unnecessary complexity
- Ready to run from a local environment
- Evidence of actual execution when appropriate

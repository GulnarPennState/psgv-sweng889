# Bike Demand Prediction with Local LLM Support

This application predicts hourly bike rental demand using a machine learning model trained on the Seoul Bike Sharing Demand dataset. It also integrates with a local LLM so the user can receive a short explanation or recommendation that complements the prediction.

## What the application does

- Accepts input such as hour, temperature, humidity, wind speed, visibility, rainfall, snowfall, season, holiday status, and whether the day is a functioning day.
- Validates the required input values.
- Uses a trained machine learning model to estimate expected bike demand.
- Calls a local LLM (via Ollama) to provide a brief explanation or recommendation.
- If the local LLM is unavailable, the app still shows the machine learning prediction and a clear fallback message.

## Required Python packages

Install the dependencies from the project folder:

```bash
cd /Users/gulnaraldaseva/psgv-sweng889/week3/4-bike-demand2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The project dependencies are:

```text
streamlit
pandas
numpy
scikit-learn
requests
```

## Start the local LLM environment

This app is designed to use a local Ollama server. Start Ollama locally on your machine if it is not already running.

Typical steps:

1. Install Ollama from https://ollama.com/
2. Start the Ollama service.
3. Pull a model such as:

```bash
ollama pull llama3.2
```

The app expects the local model name to be `llama3.2` by default in `llm_service.py`.

If Ollama is not running, the app will still show the machine learning prediction, but the LLM explanation will be replaced by a fallback message.

## Run the application

Start the app with:

```bash
cd /Users/gulnaraldaseva/psgv-sweng889/week3/4-bike-demand2
source .venv/bin/activate
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## LLM-enabled capability added

The application adds a local LLM explanation layer that complements the prediction. For example, once the prediction is calculated, the system can provide a short explanation such as:

- why demand is expected to be high or low,
- whether the weather conditions support higher or lower bike activity,
- and a brief operational recommendation.

This adds value beyond the raw numeric forecast and satisfies the requirement that the local LLM meaningfully complements the prediction.

## Notes

- The app validates input before prediction.
- Invalid or missing values show a clear user-facing error.
- If the local LLM fails, the app still returns the prediction without crashing.

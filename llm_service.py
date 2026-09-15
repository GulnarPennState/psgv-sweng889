from __future__ import annotations

from typing import Any, Dict

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"


def generate_explanation(prediction: float, input_summary: Dict[str, Any]) -> Dict[str, Any]:
    """Call the local Ollama service if available and return a fallback if it is not."""
    prompt = (
        "You are a helpful bike-rental operations assistant. "
        f"The predicted bike demand is {prediction:.0f} bikes per hour. "
        f"Weather: temperature {input_summary.get('temperature')}°C, humidity {input_summary.get('humidity')}%, "
        f"wind speed {input_summary.get('wind_speed')} m/s, rainfall {input_summary.get('rainfall')} mm, "
        f"snowfall {input_summary.get('snowfall')} cm, season {input_summary.get('season')}, "
        f"holiday={input_summary.get('holiday')}, functioning_day={input_summary.get('functioning_day')}. "
        "Give a brief explanation and a practical recommendation in 2-3 sentences."
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=5,
        )
        response.raise_for_status()
        payload = response.json()
        answer = (payload.get("response") or "").strip()

        if not answer:
            raise ValueError("Empty response from Ollama")

        return {"available": True, "message": answer}
    except Exception:
        return {
            "available": False,
            "message": (
                "Local LLM unavailable, so the prediction is shown without the explanation. "
                "The model output is still available and valid."
            ),
        }

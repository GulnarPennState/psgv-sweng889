from __future__ import annotations

from typing import Any, Dict

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

DATA_PATH = "data/raw/SeoulBikeData.csv"

_MODEL_CACHE: Dict[str, Any] | None = None


def _build_feature_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare a DataFrame for model input using the same transformations as training."""
    working = df.copy()

    if "Date" in working.columns:
        working = working.drop(columns=["Date"])
    if "Dew point temperature(°C)" in working.columns:
        working = working.drop(columns=["Dew point temperature(°C)"])

    working["is_peak_hour"] = working["Hour"].between(18, 22).astype(int)
    working["is_night"] = working["Hour"].between(0, 6).astype(int)
    working["is_working_day"] = (working["Functioning Day"] == "Yes").astype(int)
    working["is_holiday"] = (working["Holiday"] == "Holiday").astype(int)

    working = working.drop(columns=["Functioning Day", "Holiday"])
    working = pd.get_dummies(working, columns=["Seasons"], prefix="season", drop_first=True)

    return working


def _load_trained_model() -> Dict[str, Any]:
    """Train the bike-demand model once and cache it for reuse."""
    global _MODEL_CACHE

    if _MODEL_CACHE is not None:
        return _MODEL_CACHE

    df = pd.read_csv(DATA_PATH, encoding="latin-1")
    df = df.dropna(subset=["Rented Bike Count"]).copy()

    prepared = _build_feature_frame(df)
    target_col = "Rented Bike Count"
    feature_cols = [
        "Hour",
        "Temperature(°C)",
        "Humidity(%)",
        "Wind speed (m/s)",
        "Visibility (10m)",
        "Solar Radiation (MJ/m2)",
        "Rainfall(mm)",
        "Snowfall (cm)",
        "is_peak_hour",
        "is_night",
        "is_working_day",
        "is_holiday",
    ] + [c for c in prepared.columns if c.startswith("season_")]

    X = prepared[feature_cols]
    y = prepared[target_col]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestRegressor(
        n_estimators=250,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(X_scaled, y)

    _MODEL_CACHE = {
        "model": model,
        "scaler": scaler,
        "feature_cols": feature_cols,
    }
    return _MODEL_CACHE


def validate_prediction_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and normalize user input before prediction."""
    required_fields = {
        "hour": int,
        "temperature": float,
        "humidity": float,
        "wind_speed": float,
        "visibility": float,
        "rainfall": float,
        "snowfall": float,
        "season": str,
        "holiday": bool,
        "functioning_day": bool,
    }

    cleaned: Dict[str, Any] = {}

    for field, expected_type in required_fields.items():
        value = data.get(field)

        if value is None or value == "":
            raise ValueError(f"Missing required value: {field}.")

        try:
            if expected_type is int:
                value = int(value)
            elif expected_type is float:
                value = float(value)
            elif expected_type is bool:
                if isinstance(value, str):
                    value = value.lower() in {"true", "yes", "1", "y"}
                    value = bool(value)
                else:
                    value = bool(value)
            elif expected_type is str:
                value = str(value).strip()
        except (TypeError, ValueError):
            raise ValueError(f"Invalid value for {field}.")

        cleaned[field] = value

    if not 0 <= cleaned["hour"] <= 23:
        raise ValueError("Hour must be between 0 and 23.")

    if cleaned["season"] not in {"Spring", "Summer", "Autumn", "Winter"}:
        raise ValueError("Season must be one of Spring, Summer, Autumn, or Winter.")

    cleaned["holiday"] = bool(cleaned["holiday"])
    cleaned["functioning_day"] = bool(cleaned["functioning_day"])
    return cleaned


def _row_to_model_input(data: Dict[str, Any]) -> pd.DataFrame:
    """Convert user input into the same feature format used in training."""
    model_info = _load_trained_model()
    feature_cols = model_info["feature_cols"]

    row = {
        "Hour": int(data["hour"]),
        "Temperature(°C)": float(data["temperature"]),
        "Humidity(%)": float(data["humidity"]),
        "Wind speed (m/s)": float(data["wind_speed"]),
        "Visibility (10m)": float(data["visibility"]),
        "Solar Radiation (MJ/m2)": 0.0,
        "Rainfall(mm)": float(data["rainfall"]),
        "Snowfall (cm)": float(data["snowfall"]),
        "Functioning Day": "Yes" if data["functioning_day"] else "No",
        "Holiday": "Holiday" if data["holiday"] else "No Holiday",
        "Seasons": data["season"],
    }

    frame = pd.DataFrame([row])
    prepared = frame.copy()

    prepared["is_peak_hour"] = prepared["Hour"].between(18, 22).astype(int)
    prepared["is_night"] = prepared["Hour"].between(0, 6).astype(int)
    prepared["is_working_day"] = (prepared["Functioning Day"] == "Yes").astype(int)
    prepared["is_holiday"] = (prepared["Holiday"] == "Holiday").astype(int)

    prepared = pd.get_dummies(prepared, columns=["Seasons"], prefix="season", drop_first=True)
    prepared = prepared.drop(columns=["Functioning Day", "Holiday"], errors="ignore")

    for season_col in [c for c in feature_cols if c.startswith("season_")]:
        prepared[season_col] = 0

    season_name = data["season"]
    season_map = {
        "Spring": "season_Spring",
        "Summer": "season_Summer",
        "Autumn": "season_Autumn",
        "Winter": "season_Winter",
    }
    prepared[season_map[season_name]] = 1

    for col in feature_cols:
        if col not in prepared.columns:
            prepared[col] = 0

    final_row = prepared[feature_cols]
    return final_row


def predict_bike_demand(data: Dict[str, Any]) -> Dict[str, Any]:
    """Return the predicted bike demand and supporting metadata."""
    validated = validate_prediction_input(data)
    model_info = _load_trained_model()
    model = model_info["model"]
    scaler = model_info["scaler"]

    feature_frame = _row_to_model_input(validated)
    scaled = scaler.transform(feature_frame)
    prediction = float(model.predict(scaled)[0])
    prediction = max(prediction, 0.0)

    return {
        "prediction": round(prediction, 2),
        "unit": "bikes/hour",
        "input_summary": validated,
    }

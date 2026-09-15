from __future__ import annotations

import streamlit as st

from llm_service import generate_explanation
from predict import predict_bike_demand, validate_prediction_input

st.set_page_config(page_title="Bike Demand Predictor", page_icon="🚲", layout="centered")


st.title("Bike Demand Prediction")
st.caption("Predict hourly bike demand and get a local LLM explanation when available.")

with st.form("bike_form"):
    date = st.date_input("Date")
    hour = st.slider("Hour of day", 0, 23, 12)
    temperature = st.number_input("Temperature (°C)", value=18.0, step=0.5)
    humidity = st.slider("Humidity (%)", 0, 100, 50)
    wind_speed = st.number_input("Wind speed (m/s)", value=1.5, step=0.1)
    visibility = st.number_input("Visibility (10m)", value=1500.0, step=50.0)
    rainfall = st.number_input("Rainfall (mm)", value=0.0, step=0.1)
    snowfall = st.number_input("Snowfall (cm)", value=0.0, step=0.1)
    season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
    holiday = st.checkbox("Holiday")
    functioning_day = st.checkbox("Functioning Day", value=True)

    submitted = st.form_submit_button("Predict bike demand")

if submitted:
    payload = {
        "hour": hour,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "visibility": visibility,
        "rainfall": rainfall,
        "snowfall": snowfall,
        "season": season,
        "holiday": holiday,
        "functioning_day": functioning_day,
    }

    try:
        validated = validate_prediction_input(payload)
        result = predict_bike_demand(validated)
        prediction = result["prediction"]

        st.metric("Predicted bike demand", f"{prediction:.0f} bikes/hour")

        llm_result = generate_explanation(prediction, validated)
        if llm_result["available"]:
            st.success("Local LLM insight")
            st.write(llm_result["message"])
        else:
            st.warning("Local LLM unavailable")
            st.write(llm_result["message"])

        st.subheader("Input summary")
        st.write({
            "Date": str(date),
            "Hour": validated["hour"],
            "Temperature (°C)": validated["temperature"],
            "Humidity (%)": validated["humidity"],
            "Wind speed (m/s)": validated["wind_speed"],
            "Visibility (10m)": validated["visibility"],
            "Rainfall (mm)": validated["rainfall"],
            "Snowfall (cm)": validated["snowfall"],
            "Season": validated["season"],
            "Holiday": validated["holiday"],
            "Functioning Day": validated["functioning_day"],
        })

    except ValueError as exc:
        st.error(f"Invalid input: {exc}")

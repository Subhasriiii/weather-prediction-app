import streamlit as st
import pickle
import numpy as np

# Load saved model
with open('weather_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🌦️ Weather Temperature Predictor")
st.write("Enter weather conditions to predict temperature:")

humidity = st.slider("Humidity (0.0 - 1.0)", 0.0, 1.0, 0.5)
wind_speed = st.slider("Wind Speed (km/h)", 0.0, 60.0, 10.0)
visibility = st.slider("Visibility (km)", 0.0, 16.0, 10.0)
pressure = st.slider("Pressure (millibars)", 900.0, 1100.0, 1013.0)

if st.button("Predict Temperature 🌡️"):
    features = np.array([[humidity, wind_speed, visibility, pressure]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Temperature: **{prediction:.2f} °C**")
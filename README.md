# 🌦️ Weather Temperature Prediction App

An interactive machine learning web app that predicts temperature
based on weather conditions like humidity, wind speed, 
visibility and pressure.

## 🌐 Live Demo
👉 https://weather-prediction-app-im9zibhiqnmcpe5jhl9yyn.streamlit.app

## 📌 About the Project
This project uses Linear Regression to predict temperature from
historical weather data. Trained on the Szeged Weather dataset
containing ~96,000 real weather records. Deployed as an 
interactive web app using Streamlit.

## ⚙️ How It Works
1. Weather data is loaded from the Szeged Weather dataset
2. Features like humidity, wind speed, visibility and pressure
   are used as inputs
3. A Linear Regression model is trained on 80% of the data
4. User adjusts sliders in the web app for input values
5. Model predicts and displays the temperature in real time

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn
- **Algorithm:** Linear Regression
- **Web App:** Streamlit
- **Dataset:** Szeged Weather Dataset (Kaggle) (~96,000 records)

## 📂 Project Structure
weather-prediction-app/
├── app.py                # Streamlit web app
├── train_model.py        # Model training script
├── weather_model.pkl     # Saved trained model
├── weatherHistory.csv    # Szeged Weather dataset
└── requirements.txt      # Required libraries

## 🚀 How to Run Locally
# Clone the repo
git clone https://github.com/Subhasriiii/weather-prediction-app

# Install dependencies
pip install -r requirements.txt

# Train the model first
python train_model.py

# Run the app
streamlit run app.py

## 📸 Features
- Interactive sliders for humidity, wind speed,
  visibility and pressure
- Real-time temperature prediction
- Clean and simple web interface
- Trained on 96,000+ real weather records

## 📊 Model Performance
- Algorithm: Linear Regression
- Dataset Size: ~96,000 records
- Train/Test Split: 80% / 20%
- Evaluation Metrics: R2 Score, Mean Absolute Error (MAE)

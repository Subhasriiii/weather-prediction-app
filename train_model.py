# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Step 2: Load Dataset
df = pd.read_csv('weatherHistory.csv')
print(df.head())
print(df.columns)

# Step 3: Select Features
features = ['Humidity', 'Wind Speed (km/h)', 'Visibility (km)', 'Pressure (millibars)']
target = 'Temperature (C)'

df = df[features + [target]].dropna()

X = df[features]
y = df[target]

# Step 4: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Step 5: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# Step 7: Save Model
with open('weather_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved!")
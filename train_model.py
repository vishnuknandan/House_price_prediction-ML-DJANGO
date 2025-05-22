import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv('train.csv')

# Rename columns to simpler names
df = df.rename(columns={
    'BHK_NO.': 'bhk',
    'SQUARE_FT': 'sqft',
    'TARGET(PRICE_IN_LACS)': 'price'
})

# Filter and clean
df = df[['bhk', 'sqft', 'price']].dropna()
df = df[(df['price'] < 500) & (df['sqft'] < 10000)]

# Features and target
X = df[['bhk', 'sqft']]
y = df['price']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, 'house_price_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ Model and scaler saved successfully.")

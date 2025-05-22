from django.shortcuts import render
import joblib
import os
from babel.numbers import format_currency

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, 'house_price_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

def predict_price(request):
    prediction = None
    if request.method == 'POST':
        try:
            bhk = float(request.POST['bhk'])
            sqft = float(request.POST['sqft'])

            input_data = scaler.transform([[bhk, sqft]])
            price_lakh = model.predict(input_data)[0]

            # Adjust price to make it more realistic
            price_lakh *= 0.85

            prediction = format_currency(price_lakh * 100000, 'INR', locale='en_IN')

        except Exception as e:
            prediction = f"Error: {e}"

    return render(request, 'predictor/predict.html', {'prediction': prediction})

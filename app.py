from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        longitude = float(request.form['longitude'])
        latitude = float(request.form['latitude'])
        rooms = float(request.form['total_rooms'])
        bedrooms = float(request.form['total_bedrooms'])
        population = float(request.form['population'])
        households = float(request.form['households'])

        # Create DataFrame
        input_df = pd.DataFrame([[longitude, latitude, rooms, bedrooms, population, households]],
            columns=['longitude', 'latitude', 'total_rooms', 'total_bedrooms', 'population', 'households'])

        # Scale and predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]
        prediction = abs(prediction) 

        if prediction == 0:
            return render_template('index.html', prediction_text="Estimated Price: $0.00<br><small>Please ensure your input values follow the guidelines provided in the README.md file.</small>")

        # Format and return prediction
        formatted_price = "${:,.2f}".format(prediction)
        return render_template('index.html', prediction_text=f"Estimated Price: {formatted_price}")

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)

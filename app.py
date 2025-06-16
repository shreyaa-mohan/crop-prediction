from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import requests

app = Flask(__name__)

dataset = pd.read_csv('dataset.csv')
dataset = pd.get_dummies(dataset, columns=['State', 'Crop'], drop_first=True)
dataset = dataset.dropna()

X = dataset.drop(['Yield', 'Price'], axis=1)
y_yield = dataset['Yield']
y_price = dataset['Price']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

yield_model = LinearRegression()
yield_model.fit(X_scaled, y_yield)

price_model = LinearRegression()
price_model.fit(X_scaled, y_price)

def predict_crop(crop_name):
    crop_name = crop_name.strip().capitalize()  
    crop_column = f'Crop_{crop_name.upper()}'  
    print(f"Looking for column: {crop_column}")
    if crop_column not in X.columns:
        return f"Error: Crop '{crop_name}' is not available in the dataset. Available crops: {', '.join(X.columns)}"
    new_data = pd.DataFrame(columns=X.columns)
    new_data.loc[0] = 0  
    new_data[crop_column] = 1  
    new_data_scaled = scaler.transform(new_data)
    predicted_yield = yield_model.predict(new_data_scaled)[0]
    predicted_price = price_model.predict(new_data_scaled)[0]
    return predicted_yield, predicted_price

def send_sms(phone_number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = {
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': phone_number,
    }
    headers = {
        'authorization': 'KQPBiCoRyqczhdYwAklt7SJ4VDx5gLeEXTGa139ruM6IUH208WbPDdXCkZwF7EIMnGesYL6mcrRU4QxW'  # Replace with your Fast2SMS API key
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.status_code == 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    crop = request.form['crop_name'].lower()  
    phone_number = request.form['phone_number']
    prediction = predict_crop(crop)
    if isinstance(prediction, str):
        return render_template('index.html', message=prediction)
    predicted_yield, predicted_price = prediction
    message = f"Dear Farmer, the predicted yield for {crop.capitalize()} is {predicted_yield:.2f} quintals/ha, and the predicted price is {predicted_price:.2f} INR."
    sms_status = send_sms(phone_number, message)
    sms_message = "SMS sent successfully!" if sms_status else "Failed to send SMS."
    return render_template(
        'index.html',
        predicted_yield=f"{predicted_yield:.2f}",
        predicted_price=f"{predicted_price:.2f}",
        sms_message=sms_message
    )

if __name__ == '__main__':
    app.run(debug=True)

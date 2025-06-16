# 🌾 Crop Prediction Web App with SMS Notifications

This is a machine learning-based web application that predicts **crop yield** (in quintals/hectare) and **market price** (in INR) based on the selected crop. Built with **Flask**, it also sends real-time SMS notifications with the prediction results using the **Fast2SMS API**.

---

## ✨ Key Features

- 📊 Predicts **crop yield** and **price**
- 🔔 Sends **SMS notifications** to farmers in real-time
- 🧠 Built with **scikit-learn**, using Linear Regression
- 🌐 Simple, responsive web interface using **Flask** and **Bootstrap**
- 💡 Trained on real agricultural data

---

## 🧠 Machine Learning

- Two separate **Linear Regression** models are trained:
  - One for **predicting yield**
  - One for **predicting price**
- Dataset includes features like `State`, `Crop`, and historical yield/price data
- Data is preprocessed using **pandas**, **StandardScaler**, and **one-hot encoding**

---


## 🔔 SMS Notifications

SMS notifications are sent using [Fast2SMS](https://www.fast2sms.com/) API. After submitting the crop name and phone number on the web form, the user receives a message like:

Dear Farmer, the predicted yield for Wheat is 22.56 quintals/ha,
and the predicted price is 1830.75 INR.


---

## 🛠 Tech Stack

| Layer        | Technology                     |
|--------------|------------------------------- |
| Language     | Python                         |
| Backend      | Flask                          |
| ML Model     | scikit-learn (Linear Regression)|
| Frontend     | HTML, CSS, Bootstrap 5         |
| Data         | pandas, numpy                  |
| Notifications| Fast2SMS API                   |

---

## 🚀 Getting Started

### 1. Clone this repository
git clone https://github.com/shreyaa-mohan/crop-prediction.git
cd crop-prediction

### 2. (Optional) Create a virtual environment

- python -m venv venv
- source venv/bin/activate      # macOS/Linux
- venv\Scripts\activate          # Windows

### 3. Install dependencies
- pip install -r requirements.txt

### 4. Add your Fast2SMS API key
- In app.py, replace the authorization key:
-headers = {
    'authorization': 'YOUR_FAST2SMS_API_KEY'
}

### 5. Run the app
- python app.py
- Open your browser at:
- http://127.0.0.1:5000

## 📌 Use Cases
📲 Farmer assistance in rural areas without internet
📊 Agri-tech demos and hackathon prototypes
🧪 ML model experimentation in agriculture

## 🔮 Future Improvements
-Current Limitation	Possible Enhancement
Basic regression models	Use advanced models (e.g., XGBoost)
SMS in English only	Add regional language support
Static dataset	Integrate real-time weather or soil APIs
No deployment	Deploy on Render, Railway, or Replit

## 🙋‍♀️ Author
Shreya Mohan:shreyamohan74@gmail.com
Open to feedback and collaboration!


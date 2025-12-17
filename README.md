# 💰 Health Insurance Claim Prediction

This project predicts health insurance claim amounts using machine learning based on demographic, health, and lifestyle factors. The best-performing model is deployed using a Streamlit web application for real-time predictions.

---

## 📌 Project Objectives
- Predict insurance claim amounts accurately
- Analyze factors affecting insurance claims
- Compare multiple regression models
- Deploy an interactive web application using Streamlit

---

## 📊 Dataset
- Source: Kaggle
- Contains demographic, health, lifestyle, and profession-related attributes
- Target variable: `claim`

---

## 🛠 Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## 🔍 Exploratory Data Analysis
- Distribution of numerical features
- Categorical feature analysis
- Correlation heatmaps
- Scatter plots, box plots, bar charts
- City-wise and lifestyle-based claim analysis

---

## 🤖 Machine Learning Models Used
- Linear Regression
- Random Forest Regressor
- Support Vector Regression (SVR)
- XGBoost Regressor

Models were evaluated using:
- R² Score
- MAE
- RMSE

---

## 🚀 Streamlit Application
Users can input:
- Age, BMI, Weight, Blood Pressure
- Smoking and diabetes status
- Regular exercise
- Job title

The app returns a real-time predicted insurance claim amount.

---

## 📸 Screenshots
Screenshots of the Streamlit interface and EDA visualizations are available in the `screenshots/` folder.

<img width="1062" height="902" alt="Screenshot 2024-09-14 163821" src="https://github.com/user-attachments/assets/757899ac-9341-4b12-bcb9-b548b05b0fb0" />
<img width="615" height="903" alt="Screenshot 2025-12-17 232746" src="https://github.com/user-attachments/assets/c3112293-ef12-4448-b510-e7447e78464b" />
<img width="859" height="637" alt="Screenshot 2025-12-17 225435" src="https://github.com/user-attachments/assets/7fb9980b-0a3e-4bd7-af02-930f7e43a6cc" />

---

## 📦 Installation & Run
```bash
pip install -r requirements.txt
streamlit run app.py


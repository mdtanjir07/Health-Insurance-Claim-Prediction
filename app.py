import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("best_model.pkl")
training_columns = joblib.load("training_columns.pkl")

st.set_page_config(page_title="Health Insurance Claim Prediction", page_icon="💰")

st.title("💰 Health Insurance Claim Prediction")
st.write("Predict health insurance claim amount based on user details")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 31)
        weight = st.number_input("Weight", 30.0, 200.0, 70.0)
        bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
        dependents = st.number_input("Dependents", 0, 10, 1)
        bloodpressure = st.number_input("Blood Pressure", 80, 200, 120)

    with col2:
        sex = st.selectbox("Sex", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        diabetes = st.selectbox("Diabetes", ["yes", "no"])
        regular_ex = st.selectbox("Regular Exercise", ["yes", "no"])
        job_title = st.selectbox(
            "Job Title",
            ["Teacher", "Engineer", "Doctor", "Manager", "Student"]
        )

    submit = st.form_submit_button("Predict Claim")

if submit:
    try:
        input_df = pd.DataFrame([{
            "age": age,
            "weight": weight,
            "bmi": bmi,
            "no_of_dependents": dependents,
            "bloodpressure": bloodpressure,
            "sex": sex,
            "smoker": smoker,
            "diabetes": diabetes,
            "regular_ex": regular_ex,
            "job_title": job_title
        }])

        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=training_columns, fill_value=0)

        prediction = model.predict(input_df)[0]

        st.success(f"💰 Predicted Insurance Claim Amount: ₹ {prediction:,.2f}")

    except Exception as e:
        st.error("❌ Prediction failed")
        st.exception(e)

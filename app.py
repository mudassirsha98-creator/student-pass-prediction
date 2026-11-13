import streamlit as st
import joblib

model = joblib.load("student_model.pkl")

st.title("Student Pass Prediction")

hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=75)

if st.button("Predict"):
    prediction = model.predict([[hours, attendance]])

    if prediction[0] == 1:
        st.success("Student Will Pass ✅")
    else:
        st.error("Student Will Fail ❌")

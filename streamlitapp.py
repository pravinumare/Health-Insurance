import numpy as np
import pandas as pd
import pickle
import streamlit as st
from utils import Age, Gender_encoding, BMI


rf_model = pickle.load(open("rf_model.pkl", "rb"))
columns_list = pickle.load(open("columns_list.obj", "rb"))


# Creating the title for the app
st.set_page_config(page_title="Health Insurance Prediction",
                   page_icon='💊',
                   layout='centered')

# Creating header
st.header("Health Insurance Predictor")

birthday = st.text_input("Enter your Birthday \"date/month/year\"")

gender = st.selectbox("Select your Gender", ('male', 'female'))

height = st.number_input("Enter your Height in centimeter")

weight = st.number_input("Enter your Weight in kg")

health_insurance_cover = st.selectbox("Choose Premium",
                                      ('500000', '750000', '1000000', '1500000', '2000000', '2500000', '5000000', '7500000', '10000000'))


# Creating button
button = st.button("Predict")

if button:
    with st.spinner("Loading please wait..."):
        
        age = Age(birthday)
        gender = Gender_encoding(gender)
        health_insurance_cover = int(health_insurance_cover)
        bmi = BMI(height, weight)

        test_df = pd.DataFrame({'Age(yrs)':[age],
                        'Gender':[gender],
                        'Health Insurance cover':[health_insurance_cover],
                        'BMI':[bmi]})
        
        prediction = rf_model.predict(test_df)
        print(prediction[0])

        st.write(prediction[0])
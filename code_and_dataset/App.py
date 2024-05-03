import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st

# Load your machine learning model
model = pkl.load(open('C:\\Users\\bnand\\Documents\\SEM 6\\VIEH\\internship_project\\MIPML.pkl', 'rb'))

# Header and input widgets
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>Medical Insurance Premium Predictor</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.postimg.cc/Dy4bfd0p/img1.png");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

gender = st.selectbox('Choose Gender',['Choose','Male','Female'])
smoker = st.selectbox('Are you a smoker?', ['Choose','Yes','No'])
region = st.selectbox('Choose Region', ['Choose','SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.text_input('Age (Max 80)')
bmi = st.text_input('BMI (Max 100)')
children = st.text_input('Number of Children (Max 5)')

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3:
    b = st.button("PREDICT")

if b:
    error_flag = False  # Flag to track if any error occurred

    if gender == 'Choose':
        st.error("Please select a gender.")
        error_flag = True
    if smoker == 'Choose':
        st.error("Please select if you are a smoker or not.")
        error_flag = True
    if region == 'Choose':
        st.error("Please select a region.")
        error_flag = True
    if age == '' or bmi == '' or children == '':
        st.error("Please fill in all input fields.")
        error_flag = True
    else:
        # Validate inputs
        try:
            age = int(age)
            bmi = float(bmi)
            children = int(children)

            if age < 0 or age > 80:
                st.error("Age must be between 0 and 80.")
                error_flag = True
            elif bmi < 0 or bmi > 100:
                st.error("BMI must be between 0 and 100.")
                error_flag = True
            elif children < 0 or children > 5:
                st.error("Number of children must be between 0 and 5.")
                error_flag = True
        except ValueError:
            st.error("Please enter valid numerical values for age, BMI, and number of children.")
            error_flag = True

        if not error_flag:
            if gender == 'Female':
                gender = 0
            else:
                gender = 1

            if smoker == 'Yes':
                smoker = 1
            elif smoker == 'No':
                smoker = 0
            if region == 'SouthEast':
                region = 0
            elif region == 'SouthWest':
                region = 1
            elif region == 'NorthEast':
                region = 2
            else:
                region = 3

            # Prepare input data for prediction
            input_data = (age, gender, bmi, children, smoker, region)
            input_data_array = np.asarray(input_data).reshape(1,-1)
            
            # Make prediction
            predicted_prem = model.predict(input_data_array)

            # Adjusted premium (multiplied by 83)
            adjusted_prem = round(predicted_prem[0]*83)

            # Display result with some styling
            st.markdown(
                f"<h2 style='text-align: center; color: #1f77b4;'>Estimated Insurance Premium:</h2>"
                f"<h1 style='text-align: center; color: #ff6c13;'>₹ {adjusted_prem}</h1>"
                "<p style='text-align: center; font-style: italic;'>This is an estimate. Actual premium may vary.</p>",
                unsafe_allow_html=True
            )

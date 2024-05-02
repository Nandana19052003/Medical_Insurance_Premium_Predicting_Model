#importing Necessary Libraries

import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st

# Load the trained model
model = pkl.load(open('C:\\Users\\bnand\\Documents\\SEM 6\\VIEH\\internship_project\\MIPML.pkl', 'rb'))

# Set page title
st.set_page_config(page_title="Insurance Premium Predictor")

# Page Header with golden color
st.markdown("<h1 style='text-align: center; color: goldenrod;'>Medical Insurance Premium Predictor</h1>", unsafe_allow_html=True)

# Input widgets
st.markdown("## User Input")
gender = st.selectbox('Gender', ['Female', 'Male'])
age = st.number_input('Age', min_value=18, max_value=64, value=25)
bmi = st.number_input('BMI', min_value=15.0, max_value=53.1, value=25.0)
children = st.number_input('Children', min_value=0, max_value=5, value=0)
smoker = st.selectbox('Smoker', ['No', 'Yes'])
region = st.selectbox('Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])

# Predict button
if st.button('Predict'):
    # Map gender to numeric
    gender_num = 0 if gender == 'Female' else 1

    # Map smoker to numeric
    smoker_num = 1 if smoker == 'Yes' else 0

    # Map region to numeric
    region_num = {'SouthEast': 0, 'SouthWest': 1, 'NorthEast': 2, 'NorthWest': 3}[region]

    # Prepare input data
    input_data = np.array([[age, gender_num, bmi, children, smoker_num, region_num]])

    # Predict insurance premium
    predicted_premium = model.predict(input_data)[0]

    # Convert to Indian Rupees
    predicted_premium_inr = predicted_premium * 74.5  # Assuming 1 USD = 74.5 INR

    # Display result
    st.success(f'Insurance Premium: ₹{predicted_premium_inr:.2f}')

# Add some additional information
st.markdown("### About")
st.info("This app predicts medical insurance premiums based on user input.")

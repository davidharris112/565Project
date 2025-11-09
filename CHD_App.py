# Import necessary libraries
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Set up the title and description of the app
st.title('Coronary Heart Disease Predictor')
# subtitle / descriptions
# image

# generic structure for loading pickle file of each model
# this has helped me avoid issues with pickle when deploying to streamlit
BASE_DIR = os.path.dirname(__file__)
pickle_path = os.path.join(BASE_DIR, "model.pickle")
with open(pickle_path, "rb") as model_pickle:
    model_clf = pickle.load(model_pickle)



# Create a sidebar for input collection
with st.sidebar:
    #st.image('sidebar_image.jpg')
    st.header('**Input Features**')
    st.write('You can either upload a data file or manually enter features.')

with st.sidebar.expander("Option 1: Upload CSV File"):
    heart_file = st.file_uploader('Upload CSV')
    sample_csv = pd.read_csv("framingham.csv") 
    st.write("Example Data Format")
    st.dataframe(sample_csv)
    st.warning("Ensure your uploaded file has the same column names and data types as shown above.")



# I'll mess around with the different input types
# toggles might be good for the binary categorical responses
with st.sidebar.expander("Option 2: Fill Out Form"):
    st.write("Enter the data manually using the form below.")
    with st.form(key='input_form'):

        # Categorical inputs
        male = st.selectbox('Gender', options = [0,1], help     ="0 = Female , 1 =    Male")    
        education = st.selectbox('Education Level', options = [1,2,3,4], help="1 = < 11 years , 2 = 11-15 years , 3 = 16+ years , 4 = college")
        currentSmoker = st.selectbox('Current Smoker', options = [0,1], help="0 = No , 1 = Yes")
        BPMeds = st.selectbox('On Blood Pressure Medication', options = [0,1], help="0 = No , 1 = Yes")
        prevalentStroke = st.selectbox('Prevalent Stroke', options = [0,1], help="0 = No , 1 = Yes")        
        prevalentHyp = st.selectbox('Prevalent Hypertension', options = [0,1], help="0 = No , 1 = Yes")
        diabetes = st.selectbox('Diabetes', options = [0,1], help="0 = No , 1 = Yes")

        # Numerical Inputs
        age = st.number_input('Age (in years)', help="Age in years")
        if currentSmoker ==1:
            cigsPerDay = st.number_input('Cigarettes per day', help="Number of cigarettes smoked per day")
        totChol = st.number_input('Total Cholesterol (mg/dL)', help="Total cholesterol in mg/dL")   
        sysBP = st.number_input('Systolic Blood Pressure (mm Hg)', help="Systolic blood pressure in mm Hg")   
        diaBP = st.number_input('Diastolic Blood Pressure (mm Hg)', help="Diastolic blood pressure in mm Hg")  
        BMI = st.number_input('Body Mass Index (BMI)', help="Body Mass Index")
        heartRate = st.number_input('Heart Rate (beats per minute)', help="Heart rate in beats per minute")
        glucose = st.number_input('Glucose (mg/dL)', help="Glucose in mg/dL")   
        
        predict_button = st.form_submit_button("Submit Form Data")  
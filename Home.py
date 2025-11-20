# Import necessary libraries
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import pickle


# Suppress warnings
# import warnings
# warnings.filterwarnings("ignore")



st.set_page_config(page_title="Home", page_icon="❤️")   # change icon to heart

# title & subtitle
# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">10 Year Coronary Heart Disease Risk Predictor</h2>
    """,
    unsafe_allow_html = True,
)

# Initialize session state keys
# male,age,education,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose,TenYearCHD

if 'default_df' not in st.session_state:
    st.session_state['default_df'] = pd.read_csv('framingham.csv')
if 'input_type' not in st.session_state:
    st.session_state['input_type'] = 'Form'  # Default input type
if 'model_type' not in st.session_state:
    st.session_state['model_type'] = "Decision Tree"


if 'male' not in st.session_state:
    st.session_state['male'] = 1  # Default male value
if 'age' not in st.session_state:
    st.session_state['age'] = 30
if 'education' not in st.session_state:
    st.session_state['education'] = 30
if 'currentSmoker' not in st.session_state:
    st.session_state['currentSmoker'] = 30
if 'cigsPerDay' not in st.session_state:
    st.session_state['cigsPerDay'] = 30
if 'BPMeds' not in st.session_state:
    st.session_state['BPMeds'] = 30
if 'prevalentStroke' not in st.session_state:
    st.session_state['prevalentStroke'] = 30
if 'prevalentHyp' not in st.session_state:
    st.session_state['prevalentHyp'] = 30
if 'diabetes' not in st.session_state:
    st.session_state['diabetes'] = 30
if 'totChol' not in st.session_state:
    st.session_state['totChol'] = 30
if 'sysBP' not in st.session_state:
    st.session_state['sysBP'] = 30
if 'diaBP' not in st.session_state:
    st.session_state['diaBP'] = 30
if 'BMI' not in st.session_state:
    st.session_state['BMI'] = 30
if 'heartRate' not in st.session_state:
    st.session_state['heartRate'] = 30
if 'glucose' not in st.session_state:
    st.session_state['glucose'] = 30


if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False # Track if form is submitted
if 'csv' not in st.session_state:
    st.session_state['csv'] = False  #indicated if a csv has been uploaded or not














# NOTE old code, moved and adapted to the other pages

# # Set up the title and description of the app
# st.title('Coronary Heart Disease Predictor')
# # subtitle / descriptions
# # image

# # generic structure for loading pickle file of each model
# # this has helped me avoid issues with pickle when deploying to streamlit
# BASE_DIR = os.path.dirname(__file__)
# pickle_path = os.path.join(BASE_DIR, "decision_tree_chd.pickle")
# with open(pickle_path, "rb") as model_pickle:
#     model_clf = pickle.load(model_pickle)



# # Create a sidebar for input collection
# with st.sidebar:
#     #st.image('sidebar_image.jpg')
#     st.header('**Input Features**')
#     st.write('You can either upload a data file or manually enter features.')

# with st.sidebar.expander("Option 1: Upload CSV File"):
#     heart_file = st.file_uploader('Upload CSV')
#     sample_csv = pd.read_csv("framingham.csv") 
#     st.write("Example Data Format")
#     st.dataframe(sample_csv)
#     st.warning("Ensure your uploaded file has the same column names and data types as shown above.")



# # I'll mess around with the different input types
# # toggles might be good for the binary categorical responses
# with st.sidebar.expander("Option 2: Fill Out Form"):
#     st.write("Enter the risk indicators manually using the form below.")
#     with st.form(key='input_form'):

#         # Categorical inputs


#         male = st.toggle('Male?') 
#         age = st.number_input('Age (in years)', help="Age in years")
#         # TODO confirm education level categories 
#         education = st.selectbox('Education Level', options = [1,2,3,4], help="1 = Some High School , 2 = High School Graduate , 3 = Some College , 4 = College Graduate")
        
        
#         currentSmoker = st.toggle('Current Smoker?')
#         st.write("If you are a current smoker, please specify the number of cigarettes smoked per day.")
#         cigsPerDay = st.number_input('Cigarettes per day', help="Number of cigarettes smoked per day")

#         BPMeds = st.toggle('On Blood Pressure Medication?')

#         prevalentStroke = st.toggle('Prevalent Stroke?')
#         prevalentHyp = st.toggle('Prevalent Hypertension?')
#         diabetes = st.toggle('Diabetic?')


#         totChol = st.number_input('Total Cholesterol (mg/dL)', help="Total cholesterol in mg/dL")   
#         sysBP = st.number_input('Systolic Blood Pressure (mm Hg)', help="Systolic blood pressure in mm Hg")   
#         diaBP = st.number_input('Diastolic Blood Pressure (mm Hg)', help="Diastolic blood pressure in mm Hg")  
#         BMI = st.number_input('Body Mass Index (BMI)', help="Body Mass Index")
#         heartRate = st.number_input('Heart Rate (beats per minute)', help="Heart rate in beats per minute")
#         glucose = st.number_input('Glucose (mg/dL)', help="Glucose in mg/dL")   
        
#         predict_button = st.form_submit_button("Submit Form Data")  

# st.write("Input Summary for debugging")
# st.write("{male}, {education}, {currentSmoker}, {BPMeds}, {prevalentStroke}, {prevalentHyp}, {diabetes}, {age}, {cigsPerDay}, {totChol}, {sysBP}, {diaBP}, {BMI}, {heartRate}, {glucose}".format(male=male, education=education, currentSmoker=currentSmoker, BPMeds=BPMeds, prevalentStroke=prevalentStroke, prevalentHyp=prevalentHyp, diabetes=diabetes, age=age, cigsPerDay=cigsPerDay, totChol=totChol, sysBP=sysBP, diaBP=diaBP, BMI=BMI, heartRate=heartRate, glucose=glucose))

# if heart_file is not None:
#     # if we have a file upload, proceed with that data
#     heart_df = pd.DataFrame(pd.read_csv(heart_file))
#     st.success("File uploaded successfully.")
# if heart_file is None and predict_button:
#     # if we don't have a file but the form was submitted, use the form data
#     # Create a DataFrame from the form inputs
#     input_data = {
#         "male": male,
#         "age": age,
#         "education": education,
#         "currentSmoker": currentSmoker,
#         "cigsPerDay": cigsPerDay,
#         "BPMeds": BPMeds,
#         "prevalentStroke": prevalentStroke,
#         "prevalentHyp": prevalentHyp,
#         "diabetes": diabetes,
#         "totChol": totChol,
#         "sysBP": sysBP,
#         "diaBP": diaBP,
#         "BMI": BMI,
#         "heartRate": heartRate,
#         "glucose": glucose
#     }
#     # replace trues/false with 1/0
#     for key in input_data:
#         if isinstance(input_data[key], bool):
#             input_data[key] = int(input_data[key])
#     heart_df = pd.DataFrame([input_data])
#     st.success("Form data submitted successfully.")
#     st.write(heart_df.head())

# if heart_file is None and not predict_button:
#     st.info("Please upload a CSV file or fill out the form to proceed.")
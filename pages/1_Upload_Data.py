import streamlit as st
import pandas as pd

# st.set_page_config(page_title = "Upload Data", page_icon= "📊")

# title & description

input_type = st.radio("Form or CSV Upload", options=['Form', 'CSV Upload'])
st.session_state['input_type'] = input_type


if input_type== 'Form':
    with st.form("user_input_form"):    

        male = st.toggle('Male?') 
        age = st.number_input('Age (in years)', help="Age in years")
        # TODO confirm education level categories 
        education = st.selectbox('Education Level', options = [1,2,3,4], help="1 = Some High School , 2 = High School Graduate , 3 = Some College , 4 = College Graduate")
        
        currentSmoker = st.toggle('Current Smoker?')
        st.write("If you are a current smoker, please specify the number of cigarettes smoked per day.")
        cigsPerDay = st.number_input('Cigarettes per day', help="Number of cigarettes smoked per day")

        BPMeds = st.toggle('On Blood Pressure Medication?')

        prevalentStroke = st.toggle('Prevalent Stroke?')
        prevalentHyp = st.toggle('Prevalent Hypertension?')
        diabetes = st.toggle('Diabetic?')

        totChol = st.number_input('Total Cholesterol (mg/dL)', help="Total cholesterol in mg/dL")   
        sysBP = st.number_input('Systolic Blood Pressure (mm Hg)', help="Systolic blood pressure in mm Hg")   
        diaBP = st.number_input('Diastolic Blood Pressure (mm Hg)', help="Diastolic blood pressure in mm Hg")  
        BMI = st.number_input('Body Mass Index (BMI)', help="Body Mass Index")
        heartRate = st.number_input('Heart Rate (beats per minute)', help="Heart rate in beats per minute")
        glucose = st.number_input('Glucose (mg/dL)', help="Glucose in mg/dL")   
        
        submit_button = st.form_submit_button("Submit Form Data") 

        if submit_button:
            st.success("Form submitted successfully") 

    # Save the inputs to session state if the form is submitted
    if submit_button:
        st.session_state['male'] = male
        st.session_state['age'] = age
        st.session_state['education'] = education
        st.session_state['currentSmoker'] = currentSmoker
        st.session_state['cigsPerDay'] = cigsPerDay
        st.session_state['BPMeds'] = BPMeds
        st.session_state['prevalentStroke'] = prevalentStroke
        st.session_state['prevalentHyp'] = prevalentHyp
        st.session_state['diabetes'] = diabetes
        st.session_state['totChol'] = totChol
        st.session_state['sysBP'] = sysBP
        st.session_state['diaBP'] = diaBP
        st.session_state['BMI'] = BMI
        st.session_state['heartRate'] = heartRate
        st.session_state['glucose'] = glucose

        st.session_state['form_submitted'] = True

    #st.session_state['csv'] = False # not necessary?
if input_type=='CSV Upload':
    csv = st.file_uploader("Please Upload CSV")
    
    sample_csv = pd.read_csv("user_csv.csv")
    st.write("Example Data Format")
    st.dataframe(sample_csv.head())
    st.warning("Ensure your uploaded file has the same column names and data types as shown above.")
    # TODO add info on column units for numerical variables
    
    if csv is not None:
        st.session_state['csv'] = True                          # says whether a csv was uploaded
        st.session_state['Uploaded_Data'] = pd.read_csv(csv)    # store uploaded csv data
        st.success("CSV file uploaded successfully")
    if csv is None:
        st.session_state['csv'] = False

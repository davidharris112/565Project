import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Reccomendations")

## NOTE rough draft of the structure of this page
# if user submitted a form
    # if user is at risk
        # makes recs
    # if user is not at risk
        # make recs

# if user submitted a csv
# display csv and ask which row (person) they want reccomendations for
    # if selected person is at risk
            # makes recs
    # if selected person is not at risk
        # make recs

# Loop for form inputs
if st.session_state['input_type'] == 'Form' and st.session_state['form_submitted'] == True:
    # user_data = {
    #     'male': st.session_state['male'],                             # can't make reccomendations on
    #     'age': st.session_state['age'],                               # can't make reccomendations on
    #     'education': st.session_state['education'],                   # can't make (practical) reccomendations on
    #     'currentSmoker': st.session_state['currentSmoker'],           # NOTE we can make reccomendations on this
    #     'cigsPerDay': st.session_state['cigsPerDay'],                 # NOTE we can make reccomendations on this
    #     'BPMeds': st.session_state['BPMeds'],                         # not sure, probably not
    #     'prevalentStroke': st.session_state['prevalentStroke'],       # can't make reccomendations on this
    #     'prevalentHyp': st.session_state['prevalentHyp'],             # can't make reccomendations on this (?)
    #     'diabetes': st.session_state['diabetes'],                     # can't make reccomendations on this
    #     'totChol': st.session_state['totChol'],                       # NOTE we can make reccomendations on this
    #     'sysBP': st.session_state['sysBP'],                           # not sure
    #     'diaBP': st.session_state['diaBP'],                           # note sure
    #     'BMI': st.session_state['BMI'],                               # NOTE we can make reccomendations on this
    #     'heartRate': st.session_state['heartRate'],                   # not sure
    #     'glucose': st.session_state['glucose']                        # not sure
    # }
    # if at risk:
    if st.session_state['Form Prediction'] == 1:
        st.markdown("## Based on your input data, you are at risk for Coronary Heart Disease (CHD) within the next 10 years.")
        if st.session_state['currentSmoker'] == 1:
            numCigs = st.session_state['cigsPerDay']
            st.markdown(f"### Recommendation: Stop smoking, or at least reduce your number of cigarettes per day below your current {numCigs}.")
        if st.session_state['totChol'] > 200:
            totCholesterol = st.session_state['totChol']
            st.markdown(f"### Recommendation: Your total cholesterol level is {totCholesterol} mg/dL, which is considered high. Consider dietary changes and consult with a healthcare professional to manage your cholesterol levels.")
        if st.session_state['BMI'] >= 25:
            bmiValue = st.session_state['BMI']
            st.markdown(f"### Recommendation: Your BMI is {bmiValue}, which is in the overweight or obese range. Consider adopting a healthier diet and increasing physical activity to lower your BMI.")   
        else:
            st.markdown("## While we predicted that your are at risk for Coronary Heart Disease (CHD) within the next 10 years, we do not have any reccomendations at this time for your specific inputs.")
    st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")
    
    # if not at risk:
    if st.session_state['Form Prediction'] == 0:
        st.markdown("## Based on your input data, you are not at risk for Coronary Heart Disease (CHD) within the next 10 years.")
        st.markdown("### Recommendation: Maintain your healthy lifestyle! Keep up with regular exercise, a balanced diet, and routine health check-ups to continue minimizing your risk for CHD.")  
        st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")


# Loop for csv inputs

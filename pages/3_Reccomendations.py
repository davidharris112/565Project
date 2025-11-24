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


## TODO: make a function for reccomendations so the loops are more compact and easy to read





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
        made_recs = False
        if st.session_state['currentSmoker'] == 1:
            numCigs = st.session_state['cigsPerDay']
            st.markdown(f"### Recommendation: Stop smoking, or at least reduce your number of cigarettes per day below your current {numCigs}.")
            made_recs = True
        if st.session_state['totChol'] > 200:
            totCholesterol = st.session_state['totChol']
            st.markdown(f"### Recommendation: Your total cholesterol level is {totCholesterol} mg/dL, which is considered high. Consider dietary changes and consult with a healthcare professional to manage your cholesterol levels.")
            made_recs = True
        if st.session_state['BMI'] >= 25:
            bmiValue = st.session_state['BMI']
            st.markdown(f"### Recommendation: Your BMI is {bmiValue}, which is in the overweight or obese range. Consider adopting a healthier diet and increasing physical activity to lower your BMI.")   
            made_recs = True
        if not made_recs:
            st.markdown("## While we predicted that your are at risk for Coronary Heart Disease (CHD) within the next 10 years, we do not have any reccomendations at this time for your specific inputs.")
        
        st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")
    
    # if not at risk:
    if st.session_state['Form Prediction'] == 0:
        st.markdown("## Based on your input data, you are not at risk for Coronary Heart Disease (CHD) within the next 10 years.")
        st.markdown("### Recommendation: Maintain your healthy lifestyle! Keep up with regular exercise, a balanced diet, and routine health check-ups to continue minimizing your risk for CHD.")  
        st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")


# if input type was csv and a csv was uploaded
if st.session_state['input_type'] == 'CSV Upload' and st.session_state['csv']== True:
    
    # Load csv with predictions
    csv_with_predictions = st.session_state['CSV with Predictions']

    # display csv
    st.markdown("## Uploaded CSV with Predictions Added")
    st.dataframe(csv_with_predictions)

    # prompt user for row selections
    st.markdown("## Select which row/person you want reccommendations for:")
    selected_row_number = st.number_input("Row Select", min_value=0, max_value = len(csv_with_predictions)-1, step=1, value=0)

    # retrieve selected row and store in selected_row_data
    selected_row_data = csv_with_predictions.iloc[[selected_row_number]]

    # display selected row
    st.markdown("## Selected Data")
    st.dataframe(selected_row_data)

    if selected_row_data['Risk Prediction'] == 'At Risk':
        st.markdown("## Based on your input data, you are at risk for Coronary Heart Disease (CHD) within the next 10 years.")
        made_recs = False
    if selected_row_data['currentSmoker'] == 1:
        numCigs = selected_row_data['cigsPerDay']
        st.markdown(f"### Recommendation: Stop smoking, or at least reduce your number of cigarettes per day below your current {numCigs}.")
        made_recs = True
    if selected_row_data['totChol'] > 200:
        totCholesterol = selected_row_data['totChol']
        st.markdown(f"### Recommendation: Your total cholesterol level is {totCholesterol} mg/dL, which is considered high. Consider dietary changes and consult with a healthcare professional to manage your cholesterol levels.")
        made_recs = True
    if selected_row_data['BMI'] >= 25:
        bmiValue = selected_row_data['BMI']
        st.markdown(f"### Recommendation: Your BMI is {bmiValue}, which is in the overweight or obese range. Consider adopting a healthier diet and increasing physical activity to lower your BMI.")   
        made_recs = True
    if not made_recs:
        st.markdown("## While we predicted that your are at risk for Coronary Heart Disease (CHD) within the next 10 years, we do not have any reccomendations at this time for your specific inputs.")
    
    st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")

    # if not at risk:
    if selected_row_data['Risk Prediction'] == 'Not At Risk':
        st.markdown("## Based on your input data, you are not at risk for Coronary Heart Disease (CHD) within the next 10 years.")
        st.markdown("### Recommendation: Maintain your healthy lifestyle! Keep up with regular exercise, a balanced diet, and routine health check-ups to continue minimizing your risk for CHD.")  
        st.warning("## As always, please consult with a healthcare professional for personalized medical advice.")


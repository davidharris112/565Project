import streamlit as st
import pandas as pd


# st.set_page_config(page_title = "Model Insights")

# Retrieve which model was used
model_type = st.session_state.get('model_type')

if model_type=="Decision Tree":
    # Showing additional items in tabs
    st.subheader("Prediction Performance")
    tab1, tab2, tab3, tab4 = st.tabs(["Decision Tree", "Feature Importance", "Confusion Matrix", "Classification Report"])

    # Tab 1: Visualizing Decision Tree
    # Changed dt_visual to a png since the svg was too large and was causing issues on my computer
    with tab1:
            st.image('dt_visual.svg')
            st.write("### Decision Tree Visualization")
            st.caption("Visualization of the Decision Tree used in prediction.")


    # Tab 2: Feature Importance Visualization
    with tab2:
        st.write("### Feature Importance")
        st.image('feature_imp_dt.svg')


    # Tab 3: Confusion Matrix
    with tab3:
        st.write("### Confusion Matrix")
        st.image('confusionMat_dt.svg')    


    # Tab 4: Classification Report
    with tab4:
        st.write("### Classification Report")
        report_df = pd.read_csv('class_report_dt.csv', index_col = 0).transpose()
        st.dataframe(report_df.style.background_gradient(cmap='RdBu').format(precision=2))
    st.caption("Classification Report: Precision, Recall, F1-Score, and Support for each class.")

# NOTE are there other metrics we can add for SVC?
if model_type=="Soft Vote Classifier":
    # Showing additional items in tabs
    st.subheader("Prediction Performance")
    tab1, tab2, tab3 = st.tabs(["Feature Importance", "Confusion Matrix"])

    # Tab 1: Feature Importance Visualization
    with tab1:
        st.write("### Feature Importance")
        st.image('feature_imp_SV.svg')


    # Tab 2: Confusion Matrix
    with tab2:
        st.write("### Confusion Matrix")
        st.image('confusionMat_sv.svg')    

if model_type=="AdaBoost":
    # Showing additional items in tabs
    st.subheader("Prediction Performance")
    tab1, tab2, tab3 = st.tabs(["Feature Importance", "Confusion Matrix", "Classification Report"])

    # Tab 1: Visualizing Decision Tree
    # Changed dt_visual to a png since the svg was too large and was causing issues on my computer

    # Tab 2: Feature Importance Visualization
    with tab1:
        st.write("### Feature Importance")
        st.image('feature_imp_Ada.svg')


    # Tab 3: Confusion Matrix
    with tab2:
        st.write("### Confusion Matrix")
        st.image('confusionMat_Ada.svg')
        # Tab 4: Classification Report
    with tab3:
        st.write("### Classification Report")
        report_df = pd.read_csv('class_report_Ada.csv', index_col = 0).transpose()
        st.dataframe(report_df.style.background_gradient(cmap='RdBu').format(precision=2))
    st.caption("Classification Report: Precision, Recall, F1-Score, and Support for each class.")
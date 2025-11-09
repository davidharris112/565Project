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


with st.sidebar.expander("Option 2: Fill Out Form"):
    st.write("Enter the data manually using the form below.")
import pandas as pd
import streamlit as st

names_link = 'C:/Users/David - Juan/dataset.csv'

names_data = pd.read_csv(names_link)

#create the title for the web app
st.title("Streamlit and Panda")

st.dataframe(names_data)
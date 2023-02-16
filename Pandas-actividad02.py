import pandas as pd
import streamlit as st

names_link = 'C:/Users/David - Juan/dataset.csv'

#names_data = pd.read_csv(names_link)

#create the title for the web app
st.title("Streamlit and Panda")

@st.cache
def load_data(nrows):
    data=pd.read_csv(names_link, nrows=nrows)
    return data

data_load_state = st.text('Loading data....')
data = load_data(1000)
data_load_state = st.text('Done! (using cache)')

st.dataframe(data)
#writefile filterbysex.py
import streamlit as st
import pandas as pd

st.title('Streamlit - Filter by sex')

DATA_URL = "https://firebasestorage.googleapis.com/v0/b/streamlit-d4e9d.appspot.com/o/CSV%2Fdataset.csv?alt=media&token=d028617f-8424-4c54-b1f5-6aa5dd247ca9"

@st.cache
def load_data():
    data=pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_bysex(sex):
    data=pd.read_csv(DATA_URL)
    filtered_data_bysex=data[data['sex']==sex]

    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select sex", data['sex'].unique())
btnFilterbySex = st.button('Filter by sex')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row=filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)
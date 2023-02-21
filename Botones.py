#Writefile range.py
import streamlit as st
import pandas as pd

st.title('Streamlit - Search ranges')

DATA_URL = "https://firebasestorage.googleapis.com/v0/b/streamlit-d4e9d.appspot.com/o/CSV%2Fdataset.csv?alt=media&token=d028617f-8424-4c54-b1f5-6aa5dd247ca9"

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    filtered_data_byrange = data [(data['index']>=startid) & (data['index']<= endid)]

    return filtered_data_byrange

startid =st.text_input('Start index : ')
endid = st.text_input('End index : ')
btnRange = st.button('Search by range')

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0] #Gives number of rows
    st.write(f"total times: {count_row}")

    st.dataframe(filterbyrange)
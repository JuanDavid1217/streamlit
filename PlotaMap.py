import streamlit as st 
import numpy as np 
import pandas as pd 

map_data=pd.DataFrame(
    np.random.randn(1, 1)/[50,50]+[18.966111 , -97.016111],
    columns=['lat', 'lon']
)

st.map(map_data)
st.dataframe(map_data)
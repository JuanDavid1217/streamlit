import pandas as pd
import streamlit as st
import codecs

#Obtenemos la informacion
info="https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/movies.csv"

#Config. de pagina
st.set_page_config(page_title="Caso Netflix (Juan David)")

#Ponemos el cache
@st.cache
def load_data(nrows):
    name_link = codecs.open("movies1.csv",'r','latin1')
    data = pd.read_csv(name_link, nrows=nrows)
    return data




#Contenido de la pagina
sidebar=st.sidebar
agree=sidebar.checkbox("Deseas ver los films recuperados?")
if agree:
    data_load_state = st.text('cargando')
    data = load_data(500)
    data_load_state.text('netflix app!! (using st.cache)')
    st.dataframe(data)

sidebar.markdown("##")

title=sidebar.text_input("Ingresa el titulo de un pelicula")
agree=sidebar.button
    




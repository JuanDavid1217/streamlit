import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots() #fig seria la grafica, y su contenido estaria en ex

ax.hist(titanic_data['class'])#ax contiene el histograma con el campo seleccionado de los datos leidos

st.header("Histograma del Titanic")

st.pyplot(fig) #Pyplot es como el dataframe de python

st.markdown("___")

st.dataframe(titanic_data)
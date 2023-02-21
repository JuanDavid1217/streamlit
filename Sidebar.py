import streamlit as st

#Crear el titulo para la aplicación web
st.title("Mi primer App con streamlit")

#Creamos el sidebar
sidebar=st.sidebar

#asignar el titulo a la sidebar
sidebar.title("Esta es la barra lateral")

sidebar.write("Aqui van los elementos de etrada")

#Headers
st.header("Inforación sobre conjuntos de datos")
st.header("descripción de los datos")

#Se agrega texto a la sección principal
st.write("""
Este es un ejemplo de una app para predecir...""")


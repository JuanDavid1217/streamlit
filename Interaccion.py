import streamlit as st
def bienvenida(nombre):
    mymensaje = "Bienvenido /a /e " + nombre
    return mymensaje

myname = st.text_input("Nombre: ")
if (myname):
    mensaje = bienvenida(myname)
    st.write(f"Result : {mensaje}")
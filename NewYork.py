import streamlit as st
import pandas as pd
import numpy as np

st.title('Uso de Bicicletas en New York')


st.markdown("**Realizado por:**")
st.markdown("""Juan David Delgado Muñoz\n
    Matricula: S20006756\n
    email: ZS20006756@estudiantes.uv.mx\n
    Licenciatura en Ingenieria de Software.""")

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Cargando...')
data = load_data(500)
data_load_state.text("Hecho! (Datos cache cargados)")

sd=st.sidebar
sd.image("MiCredencial.jpg")
sd.markdown("___")

if sd.checkbox('Mostrar Informacion cargada'):
    st.subheader('Mostrar')
    st.subheader("Información Cargada")
    st.write(data)

sd.markdown("___")
st.markdown("___")

if sd.checkbox('Recorridos por hora'):
    st.subheader('Número de recorridos por hora')

    valores_cargados = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(valores_cargados)


sd.markdown("___")
st.markdown("___")

st.subheader("Selecciona el rango de hora")
filtrarporHora = st.slider('hora', 0, 23, 1)
valores_filtrados = data[data[DATE_COLUMN].dt.hour == filtrarporHora]

st.subheader('Mapas de recorridos iniciados a las %s:00' % filtrarporHora)
st.map(valores_filtrados)

st.markdown("___")

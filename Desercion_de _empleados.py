import streamlit as st
import pandas as pd
import codecs as cd

# Crear el título para la aplicación web
st.title("Caso Deserción de Empleados")
sidebar = st.sidebar
sidebar.title("Barra Lateral.")
sidebar.write("Este Dash tienen como objetivo analizar el desempeño de los colaboradores con el fin de identificar fortalezas y áreas de oportunidady para así lograr mejorar su rendimiento alcanzando y, a su vez, obtener una mayor calidad en sus servicios")

st.header("Conjunto de peliculas de la plataforma Netflix")

DATA_URL=('movies.csv')
@st.cache
def load_data(nrows):
    doc = cd.open('employee_data.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data=load_data (5000)
st.header("Dataset")
agree = st.sidebar.checkbox("Mostrar todos los filtros")
if agree:
  st.dataframe(data)

st.markdown("_")
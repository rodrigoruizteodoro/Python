import streamlit as st
import pandas as pd
import codecs as cd

# Crear el título para la aplicación web
st.title("Dashboard Netlfix")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")

st.header("Conjunto de peliculas de la plataforma Netflix")

DATA_URL=('movies.csv')
@st.cache
def load_data(nrows):
    doc = cd.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data=load_data (5000)
st.header("Dataset")
agree = st.sidebar.checkbox("Mostrar todos los filtros")
if agree:
  st.dataframe(data)

st.markdown("_")


selected_director = st.sidebar.selectbox("Select Director", data['director'])
st.write(f"Selected Option: {selected_director!r}")

st.write(data.query(f"""director==@selected_director"""))

st.markdown("_")


@st.cache
def load_data_name(filme):
    filtered_data_filme= data[data['name'].str.upper().str.contains(filme)]
    return filtered_data_filme

nameofmovie = st.sidebar.text_input( 'Nombre de la pelicula :')
if (nameofmovie):
    filterbyname = load_data_name (nameofmovie.upper())
    count_row = filterbyname.shape[0]# Gives number of rows
    st.write(f"Total names : {count_row}")
    st.dataframe(filterbyname)

st.markdown("_")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Dash desercion de empleados')
st.header("Streamlit")
st.write("Maria Fernanda y Rodrigo Ruiz")

st.sidebar.image("01.jpeg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    employee = pd.read_csv("Employees.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return employee

employee_load_state = st.text('Cargando Datos...')
employee = load_data(500)
employee_load_state.text("Carga Completada :)")


employee_description = st.sidebar.checkbox("Ver Base de Datos")
if employee_description:
    st.header("Muestra de Variables")
    st.dataframe(employee)

hisplot_by_age= st.sidebar.checkbox("Ver Histograma")
if hisplot_by_age:
    fig, ax = plt.subplots()
    ax.hist(employee.Age)
    st.header("Histograma de los numero de empleados por edad")
    st.pyplot(fig)
    st.markdown("_")



employee_histplot= st.sidebar.checkbox("Ver Histograma de empleados por unidad")
if employee_histplot:
    fig, ax = plt.subplots()
    ax.hist(employee.Unit)
    st.header("Histograma de Empleados por unidad")
    st.pyplot(fig)
    st.markdown("_")


city_attrittion= st.sidebar.checkbox("Ver gráfico de ciudades y tasa de deserción")
if city_attrittion:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Hometown"]
    ax.barh(x,y)
    ax.set_ylabel("City")
    ax.set_xlabel("Attrition_rate")
    st.header("Tasa de deserción por ciudad")
    st.pyplot(fig)
    st.markdown("_")

    
attrition_service= st.sidebar.checkbox("Ver grafico tasa de deserción y tiempo de servicio")
if attrition_service:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Time_of_service"]
    ax.barh(x,y)
    ax.set_ylabel("Time of service")
    ax.set_xlabel("Attrition rate")
    st.header("Tasa de deserción y tiempo de servicio")
    st.pyplot(fig)
    st.markdown("_")



age_attrition= st.sidebar.checkbox("Ver grafico edad y tasa de deserción")
if age_attrition:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Age"]
    ax.barh(x,y)
    ax.set_ylabel("Age")
    ax.set_xlabel("Attrition rate")
    st.header("tasa de deserción por edad")
    st.pyplot(fig)
    st.markdown("_")



@st.cache
def df_hometown(hometown):
    hometown_filter=employee[employee["Hometown"].str.upper().str.contains(hometown.upper())]
    
    return hometown_filter

employees_hometown= st.sidebar.text_input("Lugar de nacimiento")
search_by_hometown=st.sidebar.button("Buscar Lugar de nacimiento")

if(search_by_hometown):
    hometown_filter_if= df_hometown(employees_hometown)
    count_row= hometown_filter_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(hometown_filter_if)


@st.cache
def df_id(id):
    employee_byid=employee[employee["Employee_ID"].str.upper().str.contains(id.upper())]
    
    return employee_byid

employee_id= st.sidebar.text_input("ID de empleado")
search_by_id=st.sidebar.button("Buscar por ID")

if(search_by_id):
    id_filter= df_id(employee_id)
    count_row= id_filter.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(id_filter)

@st.cache
def df_one(one):
    filter_one=employee[employee["Unit"]==one]
    
    return filter_one

select_one= st.sidebar.selectbox("Puesto", employee['Unit'].unique())
search_one=st.sidebar.button("Buscar por Puesto")

if(search_one):
    filter_one_if= df_one(select_one)
    count_row= filter_one_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_one_if)


@st.cache
def df_education(education):
    filter_education=employee[employee["Education_Level"]==education]
    
    return filter_education

select_education= st.sidebar.selectbox("Nivel de educación", employee['Education_Level'].unique())
search_education=st.sidebar.button("Buscar Nivel de educación")

if(search_education):
    filter_education_if= df_education(select_education)
    count_row= filter_education_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_education_if)


@st.cache
def df_unit(unit):
    unit_filter=employee[employee["Unit"].str.upper().str.contains(unit.upper())]
    
    return unit_filter

unit_employee= st.sidebar.text_input("Empleados por unidad")
search_unit=st.sidebar.button("Buscar Unidad")

if(search_unit):
    unit_filter_if= df_unit(unit_employee)
    count_row= unit_filter_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(unit_filter_if)


@st.cache
def hometown_city(city):
    filter_city=employee[employee["Hometown"]==city]
    
    return filter_city

select_city= st.sidebar.selectbox("Ciudad de Nacimiento", employee['Hometown'].unique())
search_city=st.sidebar.button("Buscar Ciudad")

if(search_city):
    filter_city_if= hometown_city(select_city)
    count_row= filter_city_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_city_if)


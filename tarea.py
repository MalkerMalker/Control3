import streamlit as st
import webbrowser
import pandas as pd

archivo = st.file_uploader("database_titanic.csv", type ="csv")
if archivo is not Nore:
    data = pd.read_csv(uploaded_file)
    st.write("Datos cargados exitosamente")
    st.dataframe(data)

st.title("Registro civil")

st.write("""El tratamiento de los datos de carácter personal en registros o bancos de datos por organismos públicos o por particulares se sujetará a las disposiciones 
de esta ley, con excepción del que se efectúe en ejercicio de las libertades de emitir opinión y de informar, el que se regulará por la ley a que se refiere el artículo 
19, Nº 12, de la Constitución Política.""")

st.sidebar.image("descarga.png")
if st.button("Haz click aqui para ver el articulo"):
    webbrowser.open("https://www.dipres.gob.cl/598/articles-51683_Otrasleyes_ley19628.pdf")

ingreso = st.sidebar.text_input("Ingrese su rut")
contraseña = st.sidebar.text_input("Ingrese su clave única")

if st.sidebar.button("Ingresar"):
    st.write("Hola")
    

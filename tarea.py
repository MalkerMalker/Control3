import streamlit as st
import webbrowser
import pandas as pd
import numpy as np

st.title("Registro civil")

st.write("""El tratamiento de los datos de carácter personal en registros o bancos de datos por organismos públicos o por particulares se sujetará a las disposiciones 
de esta ley, con excepción del que se efectúe en ejercicio de las libertades de emitir opinión y de informar, el que se regulará por la ley a que se refiere el artículo 
19, Nº 12, de la Constitución Política.""")

if st.button("Haz click aqui para ver el articulo"):
    webbrowser.open("https://www.dipres.gob.cl/598/articles-51683_Otrasleyes_ley19628.pdf")

video_url = "https://www.youtube.com/watch?v=waObbD-9EsE"
st.video(video_url)


st.sidebar.image("descarga.png")

contraseñaadmin = "11111111"
rutadmin = "22222222"

contraseñareal = "12345678"
rutreal = "220149978"
rut = st.sidebar.text_input("RUT")
contraseña = st.sidebar.text_input("Contraseña", type="password")
if st.sidebar.button("Ingresar"):
    if contraseña == contraseñareal and rut == rutreal:
        st.write("Has ingresado correctamente")
    else:
        st.write("Contraseña o RUT incorrectos. Intente de nuevo.")

with st.expander("Grafico de gente registrada"):
    archivo = st.file_uploader("database_titanic.csv", type = "csv")
    if archivo is not None:
        data = pd.read_csv(archivo)
        st.write("Datos cargados exitosamente")
        st.dataframe(data)
        st.subheader("Estadisticas del archivo")
        st.write(data.describe())

    
    

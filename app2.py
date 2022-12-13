import streamlit as st
import requests
import pandas as pd
st.header("Hagamos predicciones")



satisfaction_level=st.slider(label='Nivel Satisfacción', min_value=0,
                             max_value=100, step=1,
                             value=69)

number_project = st.number_input(label='Número de proyectos',
                                 min_value=2,
                                 max_value=7 ,
                                 step=1,
                                 value=3)

dept= st.selectbox(label='Departamento de la Organización',
                   options=['sales', 'accounting', 'hr', 'technical', 'support', 'management',
              'IT', 'product_mng', 'marketing', 'RandD'])

predecir = st.button("QUE PREDIGAAA QUE PREDIGAAA")
@st.cache()
def hacer_prediccion(satisfaction_level, number_project , dept):
    request_data = str([
      {
        "satisfaction_level": satisfaction_level/100,
        "number_project": number_project,
        "dept": dept
      }
    ]).replace("'",'"')
    url_api = 'https://diplo-fun-api.herokuapp.com/predecir'

    return pd.read_json(requests.post(url=url_api, data=request_data).text)
if predecir:
    resultado = hacer_prediccion(satisfaction_level, number_project , dept)['left'][0]*100
    st.metric(value=f'{str(resultado)}%',
              label='Probabilidad de renuncia')





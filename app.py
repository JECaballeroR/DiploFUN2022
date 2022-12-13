import streamlit as st
import pandas as pd

#importamos datos del repo del profe :)
df = pd.read_csv('https://raw.githubusercontent.com/JECaballeroR/DiplomadoPythonModulo6Cohorte2/master/datos.csv')

st.dataframe(df)
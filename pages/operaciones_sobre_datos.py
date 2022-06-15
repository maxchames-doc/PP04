import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns


con = sqlite3.connect('./data/Base.db')
data = pd.read_sql("Select * from datos_clientes", con)

st.title('Operaciones para filtrar los datos')

st.subheader('Filtrado de registros por criterios - (filas)')

code = """
estados = data.State.unique()
state = st.multiselect("Elija los estados de donde provienen los clientes", estados)
if not state:
    st.error("Elija al menos un Estado")
else:
    filtrado = data[data.State.isin(state)] # Crea el dataset filtrado según los criterios elegidos
    st.dataframe(filtrado)
"""
st.code(code, language="python")

estados = data.State.unique()
state = st.multiselect("Elija los estados de donde provienen los clientes", estados)
if not state:
    st.error("Elija al menos un Estado")
else:
    filtrado = data[data.State.isin(state)]
    st.dataframe(filtrado)

st.subheader('Filtrado de atributos o variables (columnas)')

code= """
variables = data.columns.to_list()
var = st.multiselect("Elija las variables con las que desea trabajar", variables)
if not var:
    st.error("Elija al menos una variable")
else:
    filtrado2 = data.loc[:,var] # Crea el dataset filtrado según las variables elegidas.
    st.dataframe(filtrado2)
"""
st.code(code, language="python")

variables = data.columns.to_list()
var = st.multiselect("Elija las variables con las que desea trabajar", variables)
if not var:
    st.error("Elija al menos una variable")
else:
    filtrado2 = data.loc[:,var]
    st.dataframe(filtrado2)

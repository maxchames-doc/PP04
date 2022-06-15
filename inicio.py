import streamlit as st
import sqlite3
import pandas as pd


st.title('Acceso a fuentes de datos')


st.subheader('Cargando el archivo de datos desde pandas')

code = """ import pandas as pd
data = pd.read_csv('./data/archivo.csv') #Ejecuta la lectura del archivo con pandas.
data.head() # Muestra los primeros cinco registros
       """
st.code(code, language="python")

data = pd.read_csv("./data/Customer Churn Model.txt")
st.dataframe(data.head())


st.subheader('Cargando los datos desde una base de datos usando pandas')

code = """
import pandas as pd
import sqlite3

con = sqlite3.connect('./data/Base.db') # Abre la conexión a la DB.
data = pd.read_sql("SELECT * FROM datos_clientes", con) # Ejecuta la consulta con pandas.
data.head() # Muestra los primeros cinco registros

con.close() # Cierra la conexión.
"""
st.code(code, language="python")

con = sqlite3.connect('./data/Base.db')
data = pd.read_sql("SELECT * FROM datos_clientes", con)
st.dataframe(data.head())
con.close()


st.subheader('Cargando los datos desde una base de datos usando sqlite3')

code = """
import sqlite3

con = sqlite3.connect('./data/Base.db') # Abre la conexión a la DB.
cur = con.cursor() # Crea el cursor para operar sobre la base
cur.execute('SELECT * FROM datos_clientes') #Ejecuta la consulta
data = cur.fetchmany(5) # Pasa los 5 primeros resultados a la variable
print(data) # Muestra el valor de la consulta
con.close() # Cierra la conexión.
"""
st.code(code, language="python")

con = sqlite3.connect('./data/Base.db') # Abre la conexión a la DB.
cur = con.cursor()
cur.execute('SELECT * FROM datos_clientes')
data = cur.fetchmany(5)
st.dataframe(data)
con.close()

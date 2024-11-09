import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualización de los Datos", 
 				   layout="centered")


df = pd.read_csv('iris.csv')
if st.checkbox('Configuraciones'):
	option_x = st.sidebar.selectbox('Seleccione Columna X', 
								  df.columns, index=2)
	option_y = st.sidebar.selectbox('Seleccione Columna Y',
								df.columns, index=3)

selected_columns = st.multiselect("Seleccione Columnas",
	 				options=df.columns, 
	 				default='Ancho_Sepalo')
df_plot = df[selected_columns]
ancho=st.checkbox("Ancho del Contenedor")
hide_index=st.checkbox("Ocultar Index")
st.dataframe(df_plot,
	use_container_width=ancho,
	hide_index=hide_index)							

option_x = 'Longitud_Petalo'
option_y = 'Ancho_Petalo'



fig, ax = plt.subplots()
sns.scatterplot(ax=ax, data=df, 
		x=option_x, y=option_y, 
		hue='NombreEspecieIris')
st.pyplot(fig)

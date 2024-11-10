import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Visualización de los Datos", 
 				   layout="wide", 
 				   initial_sidebar_state="expanded",)

col1, col2= st.columns((0.7,3))
with col1:
	image = Image.open('logo.png') 
	st.image(image, width=150)
with col2:
	st.title("Análisis de Correlación del Dataset BreastCancer")


df= None
uploaded_file = st.file_uploader("Escoja un archivo .CSV")
if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)

if not df is None:
	selected_columns = st.multiselect("Seleccione Columnas",
	 				options=df.columns, 
	 				default='diagnosis')
	df_plot = df[selected_columns]
	ancho=st.checkbox("Ancho del Contenedor")
	hide_index=st.checkbox("Ocultar Index")
	st.dataframe(df_plot, use_container_width=ancho,
						 hide_index=hide_index)
	
	col1, col2, col3= st.columns((1,0.2,1))
	with col1:
		st.header("Matriz  de Correlación")
		matrix_cor = df_plot.corr()
		fig, ax = plt.subplots()
		sns.heatmap(ax=ax,data=matrix_cor,
			annot=True, cmap='coolwarm')
		st.pyplot(fig)

	with col3:
		st.header("Gráfico de Dispersión")
		option_x = st.selectbox('Seleccione  Columna X', df_plot.columns)
		option_y = st.selectbox('Seleccione Columna Y', df_plot.columns)
		fig, ax = plt.subplots()
		sns.scatterplot(ax=ax, data=df_plot, 
			x=option_x, y=option_y, 
			hue='diagnosis')
		st.pyplot(fig)















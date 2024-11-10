import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import pydeck as pdk

st.set_page_config(
	page_title="Visualización de los Datos", 
	layout="wide" )

col1, col2= st.columns((0.7,3)) 

with col1:
	image = Image.open('logo_ecuador.png')
	st.image(image, width=150)
with col2:
	st.title("Información Sitios de Ecuador")

col1, col2, col3= st.columns((1,0.1,1))
data = pd.read_csv('lugares-turisticos.csv', sep=';')
datosfiltrado = data
tipo=None
prov= None
tipo_mapa = 'light'
capa = 'Puntos'

if st.checkbox("Filtros"):
	st.sidebar.header("Configuraciones") 
	st.sidebar.subheader("Parámetros")
	tipo_mapa = st.sidebar.selectbox('Tipo Mapa',
						options= ['light', 'dark', 'road', 'satellite', 
						'dark_no_labels', 'light_no_labels'])

	capa = st.sidebar.selectbox('Capa Mapa', 
								options= ['Puntos', 'Texto'],
								index=0)

	st.sidebar.subheader("Filtros")
	tipo = st.sidebar.radio("Por Tipo", ('Lugar Turístico', 'Universidad', 'Todos'), 
		index=2, horizontal=True)
	if tipo == 'Lugar Turístico':
		datosfiltrado = datosfiltrado[datosfiltrado['Tipo'] == 1]
	elif tipo == 'Universidad':
		datosfiltrado = datosfiltrado[datosfiltrado['Tipo'] == 2]

	if st.sidebar.checkbox("Por Provincia"):
		prov = st.sidebar.selectbox('Seleccione Provincia',
			options= data['Provincia'].unique().tolist())
		if not prov is None:
			datosfiltrado = datosfiltrado[datosfiltrado['Provincia'] == prov]


if(capa=='Puntos'):
	capa_mapa = pdk.Layer('ScatterplotLayer',pickable=True,
		data=datosfiltrado,
		get_position=['Longitud', 'Latitud'],
		auto_highlight=True, get_radius=5000,
		get_fill_color=['Tipo==1?255:0', 'Tipo==1?0:255', 0, 160], )
else:
	capa_mapa = pdk.Layer('TextLayer',pickable=True,data=datosfiltrado, 
		get_position=['Longitud', 'Latitud'],
		get_text="Nombre", get_size=12, 
		auto_highlight=True, get_radius=5000,
		get_fill_color=['Tipo==1?255:0', 'Tipo==1?0:255', 0, 160],)
 

with col1: 
	st.pydeck_chart(
		pdk.Deck(
		map_style=tipo_mapa,
		tooltip={"text": "{Nombre}\n{Ciudad}"},
		initial_view_state=pdk.ViewState(
					latitude=-1.4796280188673958, 
					longitude=-78.55492315029493, 
					zoom=6,
					pitch=7,
					),
		layers=[capa_mapa],
		)
	)
with col3:
	st.header("Datos")
	st.dataframe(datosfiltrado,use_container_width=True, hide_index=True)





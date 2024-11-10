
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import pydeck as pdk

st.set_page_config(
	page_title="Visualización de los Datos",)

col1, col2= st.columns((0.7,3)) 

with col1:
	image = Image.open('escudoquevedo.jpg')
	st.image(image, width=150)
with col2:
	st.title("Lugares Turísticos Quevedo")

df = pd.read_json("https://turismoquevedo.com/categoria/getlistadoCB")
st.header("Categorías")
st.dataframe(df,use_container_width=True, hide_index=True)

categoria_seleccionada  = None
if st.checkbox("Filtro por Categoría"):
	categoria_seleccionada = st.selectbox('Seleccione Categorìas',
									options= df['descripcion'])
	if not categoria_seleccionada is None:
		df = pd.read_json("https://turismoquevedo.com/subcategoria/getlistadoCB/3")
		subcategoria_seleccionada = st.selectbox('Seleccione SuCategorìas',
									options= df['descripcion'])
		
Url = "https://turismoquevedo.com/lugar_turistico/json_getlistadoGridLT"
df = pd.read_json(Url)
df = pd.json_normalize(df["data"])
df = df.dropna(subset=["latitud", "longitud"])
df["latitud"] = pd.to_numeric(df["latitud"], errors="coerce")
df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")

if not categoria_seleccionada is None:
	df = df[df['categoria'] == categoria_seleccionada]

st.header("Lugares Turísticos")
st.dataframe(df,use_container_width=True, hide_index=True)


capa_mapa = pdk.Layer('ScatterplotLayer',pickable=True,
		data=df,
		get_position=['longitud', 'latitud'],
		auto_highlight=True, get_radius=50,
		get_fill_color=[255, 0, 0, 160], )

st.pydeck_chart(
		pdk.Deck(
		map_style='light',
		tooltip={"text": "{nombre_lugar}\n{categoria}"},
		initial_view_state=pdk.ViewState(
					latitude=-1.0227890672500974, 
					longitude=-79.46114989433713, 
					zoom=12,
					pitch=10,
					),
		layers=[capa_mapa],
		)
	)

























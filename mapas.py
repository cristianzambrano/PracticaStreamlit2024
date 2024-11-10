
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import pydeck as pdk

df = pd.read_csv('lugares-turisticos.csv', sep=';')
st.header("Datos")
st.dataframe(df,use_container_width=True, hide_index=True)


st.map(df,latitude='Latitud',
	longitude='Longitud', size=20, color='#0044ff')

#capa_mapa = pdk.Layer('ScatterplotLayer',
#	pickable=True,
#	data=df, 
#	get_position=['Longitud','Latitud'],
#	get_radius=5000, 
#	get_fill_color=['Tipo==1?255:0', 
#					'Tipo==1?0:255', 0, 160],
#  )

capa_mapa = pdk.Layer('TextLayer',
       			pickable=True,
       			data=df,
       			get_position=['Longitud', 'Latitud'],
       			get_text="Nombre",
       			get_size=12,
       			get_radius=5000,
       			get_color=['Tipo==1?255:0',
       			'Tipo==1?0:255', 0, 160],
       )

st.pydeck_chart(
	pdk.Deck(
		map_style='light',
		tooltip={"text": "{Nombre}\n{Ciudad}"},
		initial_view_state=
				pdk.ViewState(
						latitude=-1.4796280188673958, 
						longitude=-78.55492315029493,
						zoom=6,
						pitch=7, ),
        layers=[capa_mapa],
      )
	)


















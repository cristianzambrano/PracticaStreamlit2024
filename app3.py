import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk

df = pd.read_json("https://turismoquevedo.com/categoria/getlistadoCB")
selected_category = st.selectbox("Seleccione una categoría", options=df["descripcion"])
selected_category_id = df[df["descripcion"] == selected_category]["id"].values[0]

json_data = pd.read_json("https://turismoquevedo.com/lugar_turistico/json_getlistadoGridLT/" + str(selected_category_id) )
df = pd.json_normalize(json_data["data"])
df = df.dropna(subset=["latitud", "longitud"])

df["latitud"] = pd.to_numeric(df["latitud"], errors="coerce")
df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")

st.header("Datos")
st.dataframe(df,use_container_width=True,hide_index=True)

     
layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position="[longitud, latitud]",
            get_radius=50,
            get_color=[255, 0, 0],  
            pickable=True,
        )


st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/streets-v11",
            layers=[layer],
            initial_view_state= pdk.ViewState(
                            latitude=-1.0232,
                            longitude=-79.4635,
                            zoom=12,
                            pitch=45,
                         ),
            tooltip={"html": "<b>{nombre_lugar}</b><br>{direccion}", "style": {"color": "white"}}
        ))
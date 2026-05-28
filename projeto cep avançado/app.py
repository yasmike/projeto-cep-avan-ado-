import streamlit as st
from ferramentas  import buscar_cep
import pandas as pd


st.sidebar.image("logo.png")
st.sidebar.title("CEP hacker")
cep = st.sidebar.text_input("Digite o CEP  que deseja consultar:")

if st.sidebar.button("consultar"):
    dados = buscar_cep(cep)
    lat = float(dados.get("lat"))
    lng = float(dados.get("lng"))

    coordenadas = pd.DataFrame({"latitude":[lat], "longitude":[lng]})
    st.map(coordenadas, zoom=15, color="#2B56E21F")

    st.json(dados)
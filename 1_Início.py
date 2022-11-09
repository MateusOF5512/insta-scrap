# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image
from io import BytesIO

import pandas as pd
import numpy as np
import requests

from plots.plots_insta1 import *

im = Image.open("instagram.png")
st.set_page_config(page_title="Instagram Monitor", page_icon=im, layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/


st.title("INSTA SCRAPIZ")
st.markdown("""---""")



col1A, col2A = st.columns([1, 10])
with col1A:
    st.text("")
    st.text("")
    bot = st.button("Pesquisar")
with col2A:
    perfil = st.text_input("Insira o nome da conta que deseja pesquisar:", value="instagram")

st.markdown("""---""")



if bot:
    res = requi(perfil)
    df = convert_csv1(res)

    df_midia = convert_csv_midia(res)
    df_video = convert_csv_video(res)

    response = requests.get(df["foto"][0])
    img = Image.open(BytesIO(response.content))

    col1A, col2A = st.columns([10, 5])
    with col1A:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.dataframe(df)
    with col2A:
        st.image(img, use_column_width=True)

    st.dataframe(df_midia)
    st.dataframe(df_video)





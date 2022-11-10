# BIBLIOTECAS USADAS

import streamlit as st
from PIL import Image
from io import BytesIO

from variaveis.variaveis_css import *

import pandas as pd
import numpy as np
import requests

from plots.plots_insta1 import *
from plots.layout import *

im = Image.open("instagram.png")
st.set_page_config(page_title="Instagram Monitor", page_icon=im, layout="wide")
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

topo()
st.markdown("""---""")

perfil = st.text_input("Insira o nome da conta que deseja pesquisar:")


if len(perfil) != 0:
    parte1(perfil)


st.markdown("""---""")








rodape()
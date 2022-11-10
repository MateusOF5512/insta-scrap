from variaveis.variaveis_css import *
from plots.plots_insta1 import *

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

from PIL import Image
from io import BytesIO

## - Topo e Rodapé da Aplicação:
def topo():
    st.markdown(html_title, unsafe_allow_html=True) #Explorador de Dados Abertos
    st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    return None

def rodape():
    st.markdown(html_rodape, unsafe_allow_html=True) # ---- by: mateus
    return None

def parte1(perfil):
    res = requi(perfil)
    try:
        df = convert_csv2(res)
        df_midia = convert_csv_midia2(res)
        df_video = convert_csv_video2(res)
    except:
        df = convert_csv1(res)
        df_midia = convert_csv_midia(res)
        df_video = convert_csv_video(res)

    response = requests.get(df["foto"][0])
    img = Image.open(BytesIO(response.content))

    col1A, col2A = st.columns([10, 2])
    with col1A:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.dataframe(df)
    with col2A:
        st.image(img, use_column_width=True)

    col1A, col2A, col3A = st.columns([520, 60, 520])
    with col1A:
        st.markdown(html_card_header_A1, unsafe_allow_html=True)
        st.dataframe(df_midia, height=250)
    with col2A:
        st.text("")
    with col3A:
        st.markdown(html_card_header_A2, unsafe_allow_html=True)
        st.dataframe(df_video, height=250)



    col1A, col2A, col3A = st.columns([550, 50, 550])
    with col1A:
        optionx = st.selectbox('Selecione coluna para o eixo X:', df_midia.columns.unique(), index=1)
        optiony = st.selectbox('Selecione coluna para o eixo Y:', df_midia.columns.unique(), index=2)
        x = df_midia[optionx]
        y = df_midia[optiony]

        fig1 = barplot1(x, y)
        st.plotly_chart(fig1, use_container_width=True)
    with col2A:
        st.text("")
    with col3A:

        optionx = st.selectbox('Selecione coluna para o eixo X:', df_video.columns.unique(), index=1)
        optiony = st.selectbox('Selecione coluna para o eixo Y:', df_video.columns.unique(), index=2)
        x = df_video[optionx]
        y = df_video[optiony]

        fig2 = barplot2(x, y)
        st.plotly_chart(fig2, use_container_width=True)

    return
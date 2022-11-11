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

    graficos = ["Gráfico de Barra", "Gráfico de Linha", "Gráfico de Pizza", "Gráfico Funil", "Nuvem de Palavras"]
    grafico = st.selectbox("Selecione o tipo de Gráfico que deseja visualizar os Dados", graficos)

    if grafico == 'Gráfico de Barra':

        col1A, col2A, col3A, col4A, col5A = st.columns([300, 300, 50, 300, 300])
        with col1A:
            df_midia_y = df_midia[['LIKES', 'COMENTARIOS', 'INTER', 'UNIDADE']]
            optiony_midia = st.selectbox('Selecione coluna para o eixo Y:', df_midia_y.columns.unique(), index=2)
        with col2A:
            df_midia_x = df_midia[['TIME', 'TIPO POST', 'DIA', 'HORA', 'SEMANA', 'TURNO', 'ID POST']]
            optionx_midia = st.selectbox('Selecione coluna para o eixo X:', df_midia_x.columns.unique(), index=1)
        with col3A:
            st.text("")
        with col4A:
            df_video_y = df_video[['VISUALIZAÇÕES', 'LIKES', 'COMENTARIOS', 'INTER', 'UNIDADE']]
            optiony_video = st.selectbox('Selecione coluna para o eixo Y:', df_video_y.columns.unique(), index=0)
        with col5A:
            df_video_x = df_video[['TIME', 'TIPO POST', 'DIA', 'HORA', 'SEMANA', 'TURNO', 'ID POST']]
            optionx_video = st.selectbox('Selecione coluna para o eixo X:', df_video_x.columns.unique(), index=0)


        col1A, col2A, col3A = st.columns([600, 50, 600])
        with col1A:
            x = df_midia[optionx_midia]
            y = df_midia[optiony_midia]

            fig1 = barplot1(x, y)
            st.plotly_chart(fig1, use_container_width=True)
        with col2A:
            st.text("")
        with col3A:
            x = df_video[optionx_video]
            y = df_video[optiony_video]

            fig2 = barplot2(x, y)
            st.plotly_chart(fig2, use_container_width=True)

    elif grafico == 'Gráfico de Linha':

        col1A, col2A, col3A, col4A, col5A = st.columns([300, 300, 50, 300, 300])
        with col1A:
            optiony_midia = st.selectbox('Selecione coluna para o eixo Y:', df_midia.columns.unique(), index=2)
        with col2A:
            optionx_midia = st.selectbox('Selecione coluna para o eixo X:', df_midia.columns.unique(), index=0)
        with col3A:
            st.text("")
        with col4A:
            optiony_video = st.selectbox('Selecione coluna para o eixo Y:', df_video.columns.unique(), index=2)
        with col5A:
            optionx_video = st.selectbox('Selecione coluna para o eixo X:', df_video.columns.unique(), index=0)


        col1A, col2A, col3A = st.columns([550, 50, 550])
        with col1A:
            x = df_midia[optionx_midia]
            y = df_midia[optiony_midia]

            fig1 = lineplot1(x, y)
            st.plotly_chart(fig1, use_container_width=True)
        with col2A:
            st.text("")
        with col3A:
            x = df_video[optionx_video]
            y = df_video[optiony_video]

            fig2 = lineplot2(x, y)
            st.plotly_chart(fig2, use_container_width=True)


    elif grafico == 'Nuvem de Palavras':

        col1A, col2A, col3A = st.columns([600, 50, 600])
        with col1A:
            df_midia_t = df_midia[['TEXTO']]
            option_midia = st.selectbox('Selecione coluna para captura das palavras:', df_midia_t.columns.unique(), key=51)
        with col2A:
            st.text("")
        with col3A:
            df_video_t = df_midia[['TEXTO']]
            option_video = st.selectbox('Selecione coluna para captura das palavras:', df_video_t.columns.unique(), key=52)


        col1A, col2A, col3A = st.columns([600, 50, 600])
        with col1A:
            df1 = df_midia_t[option_midia]
            fig1 = wordcloud1(df1)
            st.pyplot(fig1)
        with col2A:
            st.text("")
        with col3A:
            df2 = df_video_t[option_video]
            fig2 = wordcloud1(df2)
            st.pyplot(fig2)


    return
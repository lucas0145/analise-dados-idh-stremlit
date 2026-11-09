import streamlit as st

from funcoes.alfabetizacao import grafico_alfabetizacao
from funcoes.pessoasIndigenas import grafico_pessoas_indigenas
from funcoes.rendimentoResposavel import grafico_rendimento_responsavel

st.set_page_config(layout="wide")

st.title("Projeto Integrado")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    _, conteudo, _ = st.columns([0.05, 0.9, 0.05])
    with conteudo:
        st.header("Indicador: Rendimento Responsável")
        st.pyplot(grafico_rendimento_responsavel(), width="stretch")

with col2:
    _, conteudo, _ = st.columns([0.05, 0.9, 0.05])
    with conteudo:
        st.header("Indicador: Pessoas Indígenas")
        st.pyplot(grafico_pessoas_indigenas(), width="stretch")

with col3:
    _, conteudo, _ = st.columns([0.05, 0.9, 0.05])
    with conteudo:
        st.header("Indicador: Alfabetização")
        st.pyplot(grafico_alfabetizacao(), width="stretch")
        
from typing import List, Dict
import networkx as nx
import streamlit as st
from views import *


@st.cache(allow_output_mutation=True)
def get_data() -> Dict:
    return {
        '2019': nx.read_graphml('data/air_traffic_2019.graphml'),
        '2020': nx.read_graphml('data/air_traffic_2020.graphml'),
        '2021': nx.read_graphml('data/air_traffic_2021.graphml'),
    }


def get_views() -> List:
    return [
        GraphView(),
        FoliumView(),
        # TODO Periphery
        # TODO Degree Centrality
        # TODO Betweenness Centrality
    ]


def format_mode(option: int):
    return MODES[option]


MODES = {
    1: 'Usar grafos existentes no app',
    2: 'Importar meu grafo',
}


def main():
    st.title("Brazil air traffic network analysis")
    IntroView().render()
    data = get_data()
    data_mode_selected = st.selectbox('Selecione a base', options=list(MODES.keys()), format_func=format_mode)
    graph = None

    if data_mode_selected == 1:
        graph_selected = st.selectbox('Selecione o ano', data.keys())
        graph = data[graph_selected]
    else:
        file_uploaded = st.file_uploader('Importe seu grafo', type='graphml')
        if file_uploaded:
            graph = nx.parse_graphml(file_uploaded.getbuffer())

    if graph:
        for page in get_views():
            page.render(graph)
            st.markdown('----------')


if __name__ == "__main__":
    main()

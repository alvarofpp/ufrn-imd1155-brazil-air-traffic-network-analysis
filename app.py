from typing import List, Dict
import networkx as nx
import streamlit as st
from views import IntroView, GraphView, FoliumView
from views.components import SelectComponent
from utils.constants import *


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


def main():
    st.title('Brazil air traffic network analysis')
    IntroView().render()
    data = get_data()

    st.sidebar.markdown('You can use a existent graph or import your graph to app.')
    data_mode_selected = SelectComponent({
        BASE_APP: 'Use existent graphs in the app',
        BASE_MY_GRAPH: 'Import my graph',
    }).render('Select the base')
    graph = None

    if data_mode_selected == BASE_APP:
        graph_selected = st.sidebar.selectbox('Select the year', data.keys())
        graph = data[graph_selected]
    else:
        file_uploaded = st.sidebar.file_uploader('Import your graph', type='graphml')
        if file_uploaded:
            graph = nx.parse_graphml(file_uploaded.getbuffer())

    if graph:
        for page in get_views():
            page.render(graph)
            st.markdown('----------')


if __name__ == "__main__":
    main()

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
    ]


def main():
    st.title("Brazil air traffic network analysis")
    IntroView().render()
    data = get_data()

    graph_selected = st.selectbox('Selecione o ano', data.keys())
    graph = data[graph_selected]

    for page in get_views():
        page.render(graph)
        st.markdown('----------')


if __name__ == "__main__":
    main()

from typing import List, Dict
import networkx as nx
import streamlit as st
from views import AirportsView, CoreDecompositionView, GraphView, IntroView, NodeRanking
from views.components import SelectComponent
from utils.constants import *


@st.cache(allow_output_mutation=True)
def get_data() -> Dict:
    return {
        '2019': nx.read_graphml('data/air_traffic_2019.graphml'),
        '2020': nx.read_graphml('data/air_traffic_2020.graphml'),
        '2021': nx.read_graphml('data/air_traffic_2021.graphml'),
    }


@st.cache()
def get_stub_graphml() -> str:
    with open('stubs/graphml.stub', mode='r') as stub:
        stub_content = stub.read()
    return stub_content


def get_views() -> List:
    return [
        GraphView(),
        AirportsView(),
        NodeRanking(),
        CoreDecompositionView(),
    ]


def mode_my_graph():
    graph = None
    stub_content = get_stub_graphml()
    file_uploaded = st.sidebar.file_uploader('Import your graph', type='graphml')
    graphml_expander = st.sidebar.beta_expander('Visualizar modelo de grafo')
    graphml_expander.text(stub_content)

    if file_uploaded:
        graph = nx.parse_graphml(file_uploaded.getbuffer())

    if graph:
        for page in get_views():
            page.render({
                'my_graph': graph,
            })
            st.markdown('----------')


def mode_app(data):
    graphs = {}
    st.sidebar.markdown('Select the year:')
    for year in data.keys():
        graphs[year] = st.sidebar.checkbox(year)

    if sum(graphs.values()) > 0:
        graphs_data = {year: data[year] for year, value in graphs.items() if value}

        for page in get_views():
            page.render(graphs_data)
            st.markdown('----------')


def main():
    st.set_page_config(
        page_title='Brazil air traffic network analysis',
        layout='wide'
    )
    st.title('Brazil air traffic network analysis')
    IntroView(render_component=st.sidebar).render()
    data = get_data()

    st.sidebar.markdown('You can use a existent graph or import your graph to app.')
    data_mode_selected = SelectComponent({
        BASE_APP: 'Use existent graphs in the app',
        BASE_MY_GRAPH: 'Import my graph',
    }, render_component=st.sidebar).render('Select the base')

    if data_mode_selected == BASE_APP:
        mode_app(data)
    else:
        mode_my_graph()


if __name__ == "__main__":
    main()

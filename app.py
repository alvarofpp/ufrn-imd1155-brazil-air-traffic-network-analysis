import copy
from typing import List, Dict
import networkx as nx
import streamlit as st
from views import AirportsView, CoreDecompositionView, GraphView, IntroView, NodeRankingView
from views.components import SelectComponent, GraphSelectComponent
from utils.constants import *
from utils.SessionState import SessionState


@st.cache()
def get_data() -> Dict:
    years = [2019, 2020, 2021]
    data = {}

    for year in years:
        with open('data/air_traffic_{}.graphml'.format(year), mode='r') as file:
            content = file.read()
            data[str(year)] = nx.parse_graphml(content)

    return data


@st.cache()
def get_stub_graphml() -> str:
    with open('stubs/graphml.stub', mode='r') as stub:
        stub_content = stub.read()
    return stub_content


def get_views() -> List:
    return [
        GraphView(),
        AirportsView(),
        NodeRankingView(),
        CoreDecompositionView(),
    ]


def render_pages():
    for page in get_views():
        page.render()
        st.markdown('----------')


def mode_my_graph():
    graph = None
    stub_content = get_stub_graphml()
    file_uploaded = st.sidebar.file_uploader('Import your graph', type='graphml')
    graphml_expander = st.sidebar.expander('View graph file template')
    graphml_expander.text(stub_content)

    if file_uploaded:
        graph = nx.parse_graphml(file_uploaded.getbuffer())

    if graph:
        SessionState.set_graphs_to_session({
            'my_graph': graph,
        })
    else:
        SessionState.set_graphs_to_session({})


def mode_app(data):
    graphs = {}
    st.sidebar.markdown('Select the year:')
    for year in data.keys():
        graphs[year] = st.sidebar.checkbox(year)

    if sum(graphs.values()) > 0:
        SessionState.set_graphs_to_session({year: data[year] for year, value in graphs.items() if value})


def main():
    st.set_page_config(
        page_title='Brazil air traffic network analysis',
        layout='wide'
    )
    # Delete all the items in Session state
    data = copy.deepcopy(get_data())

    st.title('Brazil air traffic network analysis')
    IntroView().render()

    st.sidebar.markdown("""
    # Select the graph that you want to analyze
    You can use a existent graph or import your graph to app.
    """)
    mode_selected = SelectComponent({
        BASE_APP: 'Use existent graphs in the app',
        BASE_MY_GRAPH: 'Import my graph',
    }, render_component=st.sidebar).render('Select the base')
    SessionState.change_mode(mode_selected)

    if mode_selected == BASE_APP:
        mode_app(data)
    else:
        mode_my_graph()

    if SessionState.can_render_pages():
        GraphSelectComponent(render_component=st.sidebar).render()
        render_pages()


if __name__ == "__main__":
    main()

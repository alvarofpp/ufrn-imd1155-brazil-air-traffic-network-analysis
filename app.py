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


def mode_my_graph():
    graph = None
    file_uploaded = st.sidebar.file_uploader('Import your graph', type='graphml')

    if file_uploaded:
        graph = nx.parse_graphml(file_uploaded.getbuffer())

    if graph:
        for page in get_views():
            page.render(graph)
            st.markdown('----------')


def mode_app(data):
    graphs = {}
    st.sidebar.markdown('Select the year:')
    for year in data.keys():
        graphs[year] = st.sidebar.checkbox(year)
    num_columns = sum(graphs.values())

    if num_columns > 0:
        st.markdown(graphs)
        st.markdown(num_columns)
        width = 100 / num_columns

        for page in get_views():
            cols = st.beta_columns(num_columns)
            if type(page) is FoliumView:
                page.width = width

            column_count = 0

            for year, value in graphs.items():
                if not value:
                    continue

                page.render_component = cols[column_count]
                page.render(data[year])
                column_count += 1
            st.markdown('----------')

        # for year, value in graphs.items():
        #     if not value:
        #         continue
        #
        #     for page in get_views():
        #         page.render_component = cols[column_count]
        #
        #         if type(page) is GraphView:
        #             page.width = width
        #
        #         page.render(data[year])
        #         cols[column_count].markdown('----------')
        #     column_count += 1


def main():
    st.set_page_config(
        page_title='Brazil air traffic network analysis',
        layout='wide'
    )
    st.title('Brazil air traffic network analysis')
    IntroView().render()
    data = get_data()

    st.sidebar.markdown('You can use a existent graph or import your graph to app.')
    data_mode_selected = SelectComponent({
        BASE_APP: 'Use existent graphs in the app',
        BASE_MY_GRAPH: 'Import my graph',
    }).render('Select the base')

    if data_mode_selected == BASE_APP:
        # graph_selected = st.sidebar.selectbox('Select the year', data.keys())
        mode_app(data)
    else:
        mode_my_graph()
    #     file_uploaded = st.sidebar.file_uploader('Import your graph', type='graphml')
    #     if file_uploaded:
    #         graph = nx.parse_graphml(file_uploaded.getbuffer())
    #
    # if graph:
    #     for page in get_views():
    #         page.render(graph)
    #         st.markdown('----------')


if __name__ == "__main__":
    main()

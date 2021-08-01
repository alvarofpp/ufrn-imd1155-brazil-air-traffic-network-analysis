from typing import List, Dict
import networkx as nx
import streamlit as st
from views import IntroView


@st.cache(allow_output_mutation=True)
def get_data() -> Dict:
    return {
        '2019': nx.read_graphml('/content/air_traffic_2019.graphml'),
        '2020': nx.read_graphml('/content/air_traffic_2020.graphml'),
        '2021': nx.read_graphml('/content/air_traffic_2021.graphml'),
    }


def get_pages() -> List:
    return [
        IntroView(),
    ]


def main():
    st.title("Brazil air traffic network analysis")

    for page in get_pages():
        page.render()


if __name__ == "__main__":
    main()

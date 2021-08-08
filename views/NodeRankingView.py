from .View import View
from views.components import TableComponent, PanelTabsBokehComponent
from utils.constants import METRICS
from views.charts import DegreeCentralityChart, ClosenessCentralityChart, \
    BetweennessCentralityChart, EigenvectorCentralityChart


class NodeRankingView(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Node Ranking 
        """)
        cols = self.render_component.columns(self._columns_width)

        # Column 1
        graph_selected = cols[1].selectbox('Select the graph', options=list(graphs.keys()), key='node_ranking')
        graph = graphs[graph_selected]

        TableComponent(
            render_component=cols[1],
            headers=TableComponent.metric_headers,
            values=[
                METRICS['degree_centrality'],
                METRICS['betweenness_centrality'],
                METRICS['closeness_centrality'],
                METRICS['eigenvector_centrality'],
            ]
        ).render()

        # Column 0
        PanelTabsBokehComponent(render_component=cols[0]) \
            .add_tab('Degree Centrality', DegreeCentralityChart().get(graph)) \
            .add_tab('Closeness Centrality', ClosenessCentralityChart().get(graph)) \
            .add_tab('Betweenness Centrality', BetweennessCentralityChart().get(graph)) \
            .add_tab('Eigenvector Centrality', EigenvectorCentralityChart().get(graph)) \
            .render()

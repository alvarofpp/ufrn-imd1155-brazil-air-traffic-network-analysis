from .View import View
from views.components import TableComponent, AirportsMapComponent


class AirportsView(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Airports visualization 
        """)
        cols = self.render_component.columns([6, 3, 3])

        # Column 1
        graph_selected = cols[1].selectbox('Select the graph', options=list(graphs.keys()), key='airports')
        graph = graphs[graph_selected]

        degrees = sorted(graph.degree, key=lambda x: x[1], reverse=True)
        degrees = list(degrees)
        cols[1].text('Top 5 airports with more degree:')
        TableComponent(render_component=cols[1],
                       headers=['Rank', 'Airport', 'Degree'],
                       values=[
                           [rank + 1, graph.nodes()[node]['name'], degree]
                           for rank, (node, degree) in enumerate(degrees[0:5])
                       ]).render()

        edges = sorted(graph.edges(data=True), key=lambda edge: edge[2].get('flight_count', 1), reverse=True)
        cols[2].text('Top 5 trips that happened the most:')
        TableComponent(render_component=cols[2],
                       headers=['Rank', 'Trip', 'Times'],
                       values=[
                           [rank + 1,
                            '{} - {}'.format(graph.nodes()[node_one]['name'], graph.nodes()[node_two]['name']),
                            data['flight_count']]
                           for rank, (node_one, node_two, data) in enumerate(edges[0:5])
                       ]).render()

        # Column 0
        map_component = AirportsMapComponent(render_component=cols[0])
        map_component.render(graph)

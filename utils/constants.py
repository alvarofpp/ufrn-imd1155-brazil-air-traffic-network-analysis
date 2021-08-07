BASE_APP = 1
BASE_MY_GRAPH = 2

MODE_RENDER = 1
MODE_MARKDOWN = 2

METRICS = {
    'diameter': [
        '`Diameter`',
        '[Diameter](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=5yquhZpJ1DaF&line=2&uniqifier=1) it is the **shortest** distance between the two most distant nodes in the network.',
    ],
    'degree_centrality': [
        '`Degree Centrality`',
        'Degree centrality assigns an importance score based simply on the number of links held by each node.'
    ],
    'betweenness_centrality': [
        '`Betweenness Centrality`',
        'Betweenness centrality measures the number of times a node lies on the shortest path between other nodes.'
    ],
    'closeness_centrality': [
        '`Closeness Centrality`',
        'Closeness centrality scores each node based on their ‘closeness’ to all other nodes in the network.'
    ],
    'eigen_vector_centrality': [
        '`Eigen Vector Centrality`',
        'Like degree centrality, EigenCentrality measures a node’s influence based on the number of links it has to other nodes in the network. EigenCentrality then goes a step further by also taking into account how well connected a node is, and how many links their connections have, and so on through the network.'
    ],
}

BASE_APP = 1
BASE_MY_GRAPH = 2

MODE_RENDER = 1
MODE_MARKDOWN = 2

METRICS = {
    # GraphView
    'diameter': [
        '`Diameter`',
        '[Diameter](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=5yquhZpJ1DaF&line=2&uniqifier=1) it is the **shortest** distance between the two most distant nodes in the network.',
    ],
    'radius': [
        '`Radius`',
        'The [Radius](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=eRnXKxUU2UUw&line=1&uniqifier=1) of a network is the **minimum** eccentricity.',
    ],
    # NodeRankingView
    'degree_centrality': [
        '`Degree Centrality`',
        '[Degree Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=GfPALZ3QUtlP&line=3&uniqifier=1) assigns an importance score based simply on the **number of links** held by each node.',
    ],
    'betweenness_centrality': [
        '`Betweenness Centrality`',
        '[Betweenness Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=vqlupG50r8Yf) shows which nodes are **"bridges"** between nodes in a network.',
    ],
    'closeness_centrality': [
        '`Closeness Centrality`',
        'The [Closeness Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=zXVhKitENj3D) scores each node based on their **"closeness"** to all other nodes in the network.',
    ],
    'eigenvector_centrality': [
        '`Eigenvector Centrality`',
        'The [Eigenvector Centrality](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=ix_GsVjVc_d4) measures a node’s influence based on the **number of links** it has to other nodes in the network.',
    ],
    # CoreDecompositionView
    'k_core': [
        '`K-core`',
        'A [k-core](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=vqlupG50r8Yf) in a network is a subset of its nodes in which all nodes have at least **k** connections to each other.',
    ],
    'k_shell': [
        '`K-shell`',
        'The [k-shell](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=PgYUzep5KqrU&line=5&uniqifier=1) of a graph G is the set of all nodes belonging to the k–core of G but not to the **(k+1)**–core.',
    ],
}

# ufrn-imd1155-brazil-air-traffic-network-analysis

PRIMEIRO GRUPO DE MÉTRICAS

- PERIFERIA
nx.periphery(g)

- DIAMETRO
# the diameter of networks is the maximum eccentricy
print("Diameter of network (g): {}".format(nx.diameter(g)))

# whom are in the diamter
print([k for k,v in nx.eccentricity(g).items() if v == nx.diameter(g)])

SEGUNDO GRUPO DE MÉTRICAS

4.1 Degree Centrality
4.3 Betweenness Centrality

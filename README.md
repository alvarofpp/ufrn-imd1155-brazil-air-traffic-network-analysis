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

# k-core of the network
# 1-core
# 2-core
# 3-core
set([v for k,v in nx.core_number(g).items()])
# 
# Change the variable core to visualize the nodes in k-core
# Note that 0-core is the all network
core = 3
for i in nx.k_core(g,core):
  print(i)
# 
# Change the variable shell to visualize the nodes in k-shell
# Note that vertices in k-shell are member of k-core, however they are not member of (k+1)-core
shell = 3
for i in nx.k_shell(g,shell):
  print(i)

# How many k-cores does this network have?
set([v for k,v in nx.core_number(g2).items()])
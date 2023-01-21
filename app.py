import networkx as nx
import matplotlib.pyplot as plt
import itertools


G = nx.read_edgelist('graph.txt', nodetype=int, data=(('weight', float),))
all_connected_subgraphs = []

# here we ask for all connected subgraphs that have at least 2 nodes AND have less nodes than the input graph
for nb_nodes in range(2, G.number_of_nodes()):
    for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, nb_nodes)):
        if nx.is_connected(SG):
            print(SG.nodes)
            with open('subgraphs.txt', 'a') as f:
                f.write(str(SG.nodes) + '\n')
                f.write('---------------------\n')
            all_connected_subgraphs.append(SG)

# draw graph itself
nx.draw(G, with_labels=True)
plt.show()

# draw all connected subgraphs
for SG in all_connected_subgraphs:
    nx.draw(SG, with_labels=True)
    plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import itertools


open('subgraphs.txt', 'w').close()

#G = nx.read_edgelist('graph.txt', nodetype=int, data=(('weight', float),))
print('Enter number of nodes: ')
n = int(input())
G = nx.Graph()
for i in range(n):
    G.add_node(i+1)
    
print('Enter edges (e.g. 1,2 --> it means a edge from node 1 to node 2) Press E to calculate subgraphs!')
while(True):
    inp = input()
    if inp =='E' or inp == 'e':
        break
    
    edges = inp.split(',')
    if not edges[0].isnumeric() or not edges[1].isnumeric():
        print ('***** Enter Input Correctly!')
        continue
    if int(edges[0]) > n or int(edges[0]) == 0 or int(edges[1]) > n or int(edges[1]) == 0:
        print('***** Wrong Edge Entered! TRY AGAIN')

    if int(edges[0]) == int(edges[1]):
        print('***** Not Possible! TRY AGAIN')

    
    G.add_edge(int(edges[0]), int(edges[1]))

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

all_connected_subgraphs = []

# here we ask for all connected subgraphs that have at least 2 nodes AND have less nodes than the input graph
for nb_nodes in range(1, G.number_of_nodes()+1):
    for SG in (G.subgraph(selected_nodes).to_undirected() for selected_nodes in itertools.combinations(G, nb_nodes)):
        print(SG.nodes)
        with open('subgraphs.txt', 'a') as f:
            f.write(str(SG.nodes) + '\n')
            f.write('---------------------\n')
        all_connected_subgraphs.append(SG)



counter = 221  
# draw all connected subgraphs
for i in range(len(all_connected_subgraphs)):
    # nx.draw_random(SG, with_labels=True)
    # plt.show()
    plt.subplot(counter)
    nx.draw(all_connected_subgraphs[i], with_labels=True, font_weight='bold')
    counter = counter + 1
    
    if (i+1)%4 == 0:
        counter = 221
        plt.show()
    if i == len(all_connected_subgraphs) - 1:
        plt.show()
    print(counter)

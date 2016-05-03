import matplotlib.pylab as plt
import numpy as np
import networkx as nx
from parse_inputs import parseInput
from parse_inputs import adjacencyList
import sys


def main(argv):
    if len(argv ) != 1:
        print("Usage Error, only expecting one input file")
    else:
        fileName = argv[0]

        graph, child = getGraph(fileName)
        showGraph(graph)



def getGraph(fileName):
    return parseInput(fileName)


def showGraph(graph):
    G_adj = adjacencyList(np.array(graph))
    G = nx.DiGraph(G_adj)
    # nx.write_adjlist(G_adj, )
    #initialze Figure
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(G, pos,  edge_color='b', arrows=True)
    plt.show()
if __name__ == '__main__':
    main(sys.argv[1:])
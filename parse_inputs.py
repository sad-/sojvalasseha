import sys
import numpy as np
from johnson import get_elementary_cycles

def main(argv):
    if len(argv) != 1:
        print("Usage Error: python parse_inputs.py inputfile")
    else:
        G, children = parseInput(argv[0])
        Gs, indices = breakDown(G)
        G_adj = [adjacencyList(mat) for mat in Gs]
        print G_adj[0]
        cycles = get_elementary_cycles(G_adj[0])
        #cycles = [get_elementary_cycles(G_in) for G_in in G_adj]
        print len(cycles)


def parseInput(filename):
    try:
        fin = open(filename, "r")
    except FileNotFoundError:
        return filename + " not found."

    n_v = int(fin.readline())
    children = map(int, fin.readline().split())
    G = [map(int, fin.readline().split()) for i in xrange(n_v)]
    return G, children

def breakDown(G, n_s=5):
    #G is the large graph
    #n_s is the number of subgraphs or partitions
    mat = np.array(G)
    indices = np.split(np.random.permutation(xrange(len(G))), n_s)
    Gs = [np.empty([len(indices[j]), len(indices[j])]) for j in xrange(n_s)]
    for j in xrange(n_s):
        for k in xrange(len(indices[j])):
            Gs[j][k,:] = mat[indices[j][k], indices[j]]
    return Gs, indices

def adjacencyList(mat):
    adj_lst = {}
    for i in xrange(mat.shape[0]):
     adj_lst[i] = tuple(np.nonzero(mat[i,:])[0].tolist())
    return adj_lst

def isChild(v):
    return v in children

if __name__ == '__main__':
    main(sys.argv[1:])
import sys
import numpy as np
from johnson import get_elementary_cycles
def main(argv):
    if len(argv) != 1:
        print("Usage Error: python parse_inputs.py inputfile")
    else:
        G, children = parseInput(argv[0])
        G_in = adjacencyList(G)

        cycles = get_elementary_cycles(G_in)
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

def adjacencyList(G):
    mat = np.array(G)
    adj_lst = {}
    for i in xrange(len(G)):
     adj_lst[i] = tuple(np.nonzero(mat[i,:])[0].tolist())
    print adj_lst[0]
    return adj_lst

def isChild(v):
    return v in children

if __name__ == '__main__':
    main(sys.argv[1:])
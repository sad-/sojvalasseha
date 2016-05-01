from __future__ import division
import sys
import os
import numpy as np
from johnson import get_elementary_cycles

def main(argv):
    if len(argv) != 1:
        print("Usage Error: python parse_inputs.py inputfile")
    else:
        G, children = parseInput(argv[0])
        if len(G) <= 40:
            G_adj = adjacencyList(np.array(G))
            cycles = get_elementary_cycles(G_adj)
            cycs = [[cyc for cyc in cycles if len(cyc) <= 5]]
        else:
            Gs, indices = breakDown(G)
            G_adj = [adjacencyList(mat) for mat in Gs]
            cycles = [get_elementary_cycles(G_in) for G_in in G_adj]
            cycs = revert(cycles, indices)
        pipeOutput(cycs, argv[0])


def parseInput(filename):
    try:
        fin = open(filename, "r")
    except FileNotFoundError:
        return filename + " not found."

    n_v = int(fin.readline())
    children = map(int, fin.readline().split())
    G = [map(int, fin.readline().split()) for i in xrange(n_v)]
    return G, children

def breakDown(G, n_s=None):
    #G is the large graph
    #n_s is the number of subgraphs or partitions
    if n_s == None:
        if len(G) > 200:
            n_s = int(np.ceil(len(G)/10))
        else:
            n_s = int(np.ceil(len(G)/20))
    mat = np.array(G)
    indices = np.array_split(np.random.permutation(xrange(len(G))), n_s)
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

def revert(cycs, idx):
    #converts the vertices of the subgraphs back to their original indexing
    return [[[idx[j][cycs[j][k][i]] for i in xrange(len(cycs[j][k]))] for k in xrange(len(cycs[j])) if len(cycs[j][k]) <= 5] for j in xrange(len(cycs))]


def pipeOutput(cycs, filein):
    parts = filein.split("/")
    path = 'results/'
    if not os.path.exists(path):
        os.mkdir(path)
    fname = parts[-1].replace(".in", ".cyc")
    fileout = path + fname
    print fileout
    fout = open(fileout, 'w+')
    for subgraph in cycs:
        for cyc in subgraph:
            line = ''
            for (i, vertex) in enumerate(cyc):
                if i == len(cyc)-1:
                    line += str(vertex) + '\n'
                else:
                    line += str(vertex) + ' '
            fout.write(line)

def isChild(v):
    return v in children

if __name__ == '__main__':
    main(sys.argv[1:])
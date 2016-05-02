from __future__ import division
import numpy as np
import pdb
import random

import math
from decimal import *
from sklearn import svm
import os
import sys
import csv
from parse_inputs import parseInput

def main(argv):
   if len(argv) != 2:
      print("Usage Error, Weiht Cycles expects a .in and a .cyc file")
   else:
      inFile, cycFile = argv
      children = readIn(inFile)
      print children
      cycList = readCyc(cycFile)
      cycleWeights = weightCyc(children, cycList)


def readIn(fileName):
   """ Return children from original input file"""
   children = parseInput(fileName, child = True)

def readCyc(fileName):
   return [map(int, line.split()) for line in open(fileName)] 

def weightCyc(children, cycList):
   weights = []
   for i in range(len(cycList)):
      curr = cycList[i]
      w = 0
      for el in curr:
         if el in children:
            w += 2
         else:
            w += 1
      weights[i] = w
   return weights

def selectCyc(cycles, cycleWeight):
   """Need to select cycles 
   which do not share vertices 
   Independent set or SCC
   First approach: greedily add cycles 
   """

   weights = np.array(cycleWeight)
   sortedIndices = np.argsort(weights)

   ind1 = sortedIndices[0]
   selectedVertices = np.array(cycles[ind1])
   selectedCycIndices = [0]
   i = 1

   while i < len(cycles):
      cycle = np.array(cycles[i])
      sharedVertices = np.in1d(cycle, selectedVertices)

      if not sharedVertices.any():
         selectedVertices.append(cycle)
         selectedCycIndices.append[i]
      i += 1
   return [cycles[index] for index in selectedCycIndices ]


def pipeOut(cycles):
   """ Write selected cycles to output file 
   in following format: 
   """


if __name__ == '__main__':
    main(sys.argv[1:])



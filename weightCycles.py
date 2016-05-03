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
from parse_inputs import pipeOutput

def main(argv):
   if len(argv) != 2:
      print("Usage Error, Weiht Cycles expects a .in and a .cyc file")
   else:
      inFile, cycFile = argv
      children = readIn(inFile)
      cycList = readCyc(cycFile)
      cycleWeights = weightCyc(children, cycList)
      finalCycs = selectCyc(cycList, cycleWeights)
      print len(finalCycs)
      print finalCycs
      pipeOutput(finalCycs, inFile, final=True)


def readIn(fileName):
   """ Return children from original input file"""
   return parseInput(fileName, child = True)

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
      weights.append(w)
   # weights = [len(cyc) + sum(np.array([w in children for w in cyc])) for cyc in cycList]
   return weights

def selectCyc(cycles, cycleWeight):
   """Need to select cycles 
   which do not share vertices 
   Independent set or SCC
   First approach: greedily add cycles 
   """

   weights = np.array(cycleWeight)
   sortedIndices = np.argsort(weights)[::-1]
   ind1 = sortedIndices[0]
   selectedVertices = np.array(cycles[ind1])
   selectedCycIndices = [ind1]
   i = 1

   while i < len(cycles):
      index = sortedIndices[i]
      cycle = np.array(cycles[index])
      sharedVertices = np.in1d(cycle, selectedVertices)
      if not sharedVertices.any():
         selectedVertices = np.append(selectedVertices, cycle)
         selectedCycIndices.append(index)
      i += 1
   return [cycles[index] for index in selectedCycIndices ]


def pipeOut(cycles):
   """ Write selected cycles to output file 
   in following format: 
   """


if __name__ == '__main__':


    main(sys.argv[1:])



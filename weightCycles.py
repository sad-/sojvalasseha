import numpy as np
import pdb
import random

import math
from decimal import *
from sklearn import svm
import os
import sys
import csv
from __future__ import division
from parse_inputs import parseInput

   def main(argv):
      if len(argv) != 2:
         print("Usage Error, Weiht Cycles expects a .in and a .cyc file")
      else:
         inFile, cycFile = argv
         children = readIn(inFile)
         cycList = readCyc(cycFile)
         cycleWeights = weightCyc(cycList)


   def readIn(fileName):
      """ Return children from original input file"""
      children = parseInput(fileName, child = True)

   def readCyc(fileName):
      return [map(int, line.split() for line in open(fileName))] 

   def weightCyc(children, cycList):


   def selectCyc(cycles, cycleWeight):
      """Need to select cycles 
      which do not share vertices 
      Independent set or SCC
      First approach: greedily add cycles 
      """


      selectedVertices = set()

      weights = np.array(cycleWeight)
      sortedIndices = np.argsort()
      
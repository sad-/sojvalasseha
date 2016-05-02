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

   def readIn(fileName):
      """ Return children from original input file"""
      children = parseInput(fileName, child = True)

   def readCyc(fileName):
      return cycleList = [map(int, line.split() for line in open(fileName)]

   def weightCyc(children, cycList):
      
import unittest
from weightCycles import *
import pdb
class cycleTest(unittest.TestCase):

	def test_selectCycle(self):
		cycles = [[1,2,3,4,5], [6,7,8], [8,9,10], [1,4,2], [4,8,0] ]
		weights = [1,3,2,4,0,]
		selected = selectCyc(cycles, weights)
		self.assertEqual(selected, [[1,4,2], [6,7,8]])

		cycles = [[1,2,3,5], [6,7], [9,10],  [44,8,0]]
		weights = [1,3,2,4]
		selected = selectCyc(cycles, weights)
		self.assertEqual(selected, [[44,8,0], [6,7], [9,10], [1,2,3,5]])

if __name__ == '__main__':
	unittest.main()
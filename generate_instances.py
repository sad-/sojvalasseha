import numpy as np

#generate the children vertices

def getChildren(num_Vertices, num_Children):
	return np.random.choice(xrange(num_Vertices), num_Children, replace=False)

def getAdjMatrix(num_Vertices):
	#generate erdos renyi random graph with p = 0.2
	p = 0.2
	matrix = np.empty([num_Vertices, num_Vertices], dtype=int)
	for i in xrange(matrix.shape[0]):
		for j in xrange(matrix.shape[1]):
			if i != j:
				if np.random.rand() <= p:
					matrix[i, j] = 1
			else:
				matrix[i, j] = 0

	#insert potential solutions i.e actual cycles of length cyclength
	cyclength = np.random.choice(xrange(3, 6))
	cyclic = np.random.choice(xrange(num_Vertices), cyclength)
	print cyclic
	for i in xrange(len(cyclic) -1):
		matrix[cyclic[i], cyclic[i+1]] = 1
	matrix[cyclic[-1], cyclic[0]]=1
	return matrix


num_Vertices = 200
num_Children = num_Vertices/4
firstline = str(num_Vertices) + '\n'

#print list of children to string for second line
def strFormatChildren(children):
	secondline = ''
	for i, child in enumerate(children):
		if i == len(children) - 1:
			secondline += str(child)
		else:
			secondline += str(child) + ' '
	secondline += '\n'
	return secondline


#print graph adjacency matrix to string:
def strFormatMatrix(matrix):
	matrix_str = ''
	for i in xrange(matrix.shape[0]):
		matrix_row = ''
		for j in xrange(matrix.shape[1]):
			if j == matrix.shape[1] - 1:
				matrix_row += str(matrix[i, j])
			else:
				matrix_row += str(matrix[i, j]) + ' '
		matrix_row += '\n'
		matrix_str += matrix_row
	return matrix_str


#write to file
f1 = open('sojvalasseha1.in', 'w+')
f1.write(firstline)
f1.write(strFormatChildren(getChildren(num_Vertices, num_Children)))
f1.write(strFormatMatrix(getAdjMatrix(num_Vertices)))

f2 = open('sojvalasseha2.in', 'w+')
f2.write(firstline)
f2.write(strFormatChildren(getChildren(num_Vertices, num_Children)))
f2.write(strFormatMatrix(getAdjMatrix(num_Vertices)))

f3 = open('sojvalasseha3.in', 'w+')
f3.write(firstline)
f3.write(strFormatChildren(getChildren(num_Vertices, num_Children)))
f3.write(strFormatMatrix(getAdjMatrix(num_Vertices)))
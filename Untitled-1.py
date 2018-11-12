#coding=utf-8

from MyMatrix import Matrix

def nado(text):
	pass

def getMatrixText():
	matrix = Matrix([ [5, 1, 2], [4, 3, 6], [12, 23, 18] ])
	s = [ [ str(matrix[i][j]) for j in range(len(matrix[i])) ] for i in range(len(matrix)) ]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	test = '\n'.join(table)
	return test.expandtabs()

print(getMatrixText())

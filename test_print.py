#!/usr/bin/env python3
#cpdong=utf-8

from MyMatrix import Matrix

def getMatrixText():
        a = Matrix([ [5, 1, 2], [4, 3, 6], [12, 23, 18] ])
        res = ''
        for i in range(len(a)):
                for j in range(len(a[i])):
                        res += str(a[i][j]) + ' '
                res += '\n'
        return res

matrix = Matrix([ [5, 1, 2], [4, 3, 6], [12, 23, 18] ])
s = [ [ str(matrix[i][j]) for j in range(len(matrix[i])) ] for i in range(len(matrix)) ]
print(s)
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
test = '\n'.join(table)
print(test)

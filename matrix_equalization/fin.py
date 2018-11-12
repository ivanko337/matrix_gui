#!/usr/bin/env python3
#coding=utf-8

from Gauss import Gauss
from InverseMatrix import InverseMatrix
from Cramer import Cramer
from MyMatrix import Matrix

def f():
	A = Matrix([ [2, 1, -1], [1, 3, 6], [3, -1, -1] ])
	B = Matrix([1, 2, 7])
	invMatr = InverseMatrix(A, B)
	cramer = Cramer(A, B)
	gauss = Gauss(A, B)
	print('Cramer: {}'.format(cramer.getResult()))
	print('Gauss: {}'.format(gauss.getResult()))
	print('Inverse Matrix: {}'.format(invMatr.getResult()))

if __name__ == '__main__':
	f()

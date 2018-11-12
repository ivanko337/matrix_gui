#!/usr/bin/env python3
#coding=utf-8

from MyMatrix import Matrix
from MatrixAlghoritms import toTriangleShape, addColumn
from copy import deepcopy

class Gauss:
	def __init__(self, a, b):
		assert isinstance(a, Matrix) and len(a) == len(b)
		self.A = deepcopy(a)
		self.B = deepcopy(b)

	def getResult(self):
		A = addColumn(self.A, self.B)
		m = len(A)
		assert all([len(row) == m + 1 for row in A[1:]]), "Matrix rows have non-uniform length"

		A = toTriangleShape(A)

		# Solve equation Ax=b for an upper triangular matrix A
		x = []
		for i in range(m - 1, -1, -1):
			x.insert(0, A[i][m] / A[i][i])
			for k in range(i - 1, -1, -1):
				A[k][m] -= A[k][i] * x[0]
		return x

	@classmethod
	def getResultStatic(self, A, B):
		res = Gauss(A, B)
		return res.getResult()

#!/usr/bin/env python3
#coding=utf-8

from MyMatrix import Matrix
import enterMatrix
import enterSize

class App:
	def __init__(self):
		self.matrixA = Matrix([])
		self.matrixB = Matrix([])
		self.a_size = (1, 0)
		self.b_size = self.a_size[0]
		self.x_size = self.b_size
		self.solution_method = None

	def test(self):
		data1 = enterSize.__main__()
		data2 = enterMatrix.__main__()
		print('{} {}'.format(data1, data2))

if __name__ == '__main__':
	test = App()
	test.test()

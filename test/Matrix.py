#coding=utf-8

import numpy as np
from random import randint

class Matrix:
    def __init__(self, input_list=[], random=False, triangle1=False, triangle2=False, row=0, column=0):
        if random:
            self.random(row, column)
        elif triangle1:
            self.fillTiangle1(row, column)
        elif triangle2:
            self.fillTiangle2(row, column)
        else:
            self.matrix = np.matrix(input_list)

    def item(self, row, column):
        return self.matrix[row].item(column)

    def add(self, second_matrix):
        return Matrix(self.matrix + second_matrix.matrix)

    def multiplicate(self, second_operand):
        if type(second_operand) == int:
            return Matrix(self.matrix * second_operand)
        return Matrix(self.matrix * second_operand.matrix)

    def substraction(self, second_matrix):
        return Matrix(self.matrix + second_matrix.multiplicate(-1).matrix)

    def equals(self, second_matrix):
        return self.toList() == second_matrix.toList()

    def random(self, row, column):
        m = []
        for i in range(row):
            tm = []
            for j in range(column):
                tm.append(randint(0, 100))
            m.append(tm)
            del tm
        self.matrix = np.matrix(m)

    def print_matrix(self):
        for i in range(self.matrix.shape[0]):
            temp = ''
            for j in range(self.matrix.shape[1]):
                temp += str(self.item(i, j)) +  ' '
            print(temp)
            del temp

    def rows(self):
        return self.matrix.shape[0]

    def columns(self):
        return self.matrix.shape[1]

    def toList(self):
        res = []
        for i in range(self.rows()):
            for j in range(self.columns()):
                res.append(self.item(i, j))
        return res

    def fillTiangle1(self, row, column):
        if row != column:
            print('Only for square matrix!')
            return 
        m = []
        for i in range(row):
            r = []
            for j in range(column):
                if j < i:
                    r.append(0)
                else:
                    r.append(randint(0, 100))
            m.append(r)
        self.matrix = np.matrix(m)

    def fillTiangle2(self, row, column):
        if row != column:
            print('Only for square matrix!')
            return 
        m = []
        for i in range(row):
            r = []
            for j in range(column):
                if j > i:
                    r.append(0)
                else:
                    r.append(randint(1, 100))
            m.append(r)
        self.matrix = np.matrix(m)

    def fillUnit(self, row, column):
        if row != column:
            print('Only for square matrix!')
            return 
        res = []
        for i in range(row):
            tr = []
            for j in range(column):
                if i == j:
                    tr.append(1)
                else:
                    tr.append(0)
            res.append(tr)
        self.matrix = np.matrix(res)

a = Matrix(random=True, row=5, column=5)
b = Matrix(random=True, row=5, column=5)
c = Matrix(['1 2 3', ' 4 5 6'])
d = Matrix('1 2 3 3; 4 5 6 3; 3 3 3 3; 3 3 3 3')
d.fillTiangle1(*d.matrix.shape)
d.print_matrix()
print()
d.fillTiangle2(*d.matrix.shape)
d.print_matrix()
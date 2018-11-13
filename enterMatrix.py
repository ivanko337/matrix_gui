#!/usr/bin/env python3
#coding=utf-8

import sys
from enterMatrix_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from MyMatrix import Matrix

class EnterMatrix(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.p)
		self.data = Matrix()

	def p(self):
		self.data = Matrix()
		count = self.verticalLayout.count()
		for i in range(count):
			if isinstance(self.verticalLayout.itemAt(i), QtWidgets.QWidgetItem):
				continue
			temp = self.verticalLayout.itemAt(i).count()
			temp_res = []
			for j in range(temp):
				if type(self.verticalLayout.itemAt(i).itemAt(j).widget()) == QtWidgets.QLabel:
					continue
				value = self.verticalLayout.itemAt(i).itemAt(j).widget().text()
				if value == '':
					temp_res.append(0.)
				else:
					temp_res.append(float(value))
			self.data.append(temp_res)

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = EnterMatrix()
	window.show()
	window.setFixedSize(window.width(), window.height())
	app.exec_()
	return window.data

if __name__ == '__main__':
	__main__()

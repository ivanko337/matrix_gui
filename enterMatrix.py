#!/usr/bin/env python3
#coding=utf-8

import sys
from enterMatrix_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

class EnterMatrix(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.p)
		self.data = []

	def p(self):
		help(self.horizontalLayout)

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = EnterMatrix()
	window.show()
	window.setFixedSize(window.width(), window.height())
	app.exec_()
	return window.data

if __name__ == '__main__':
	__main__()

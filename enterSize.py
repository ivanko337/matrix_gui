#!/usr/bin/env python3
#coding=utf-8

import sys
from enter_size_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from time import sleep

class EnterSize(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.enterButtonClicked)
		self.data = None

	def enterButtonClicked(self):
		equation_count = int(self.lineEdit.text())
		self.data = equation_count
		self.close()

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = EnterSize()
	window.show()
	window.setFixedSize(window.width(), window.height())
	app.exec_()
	return window.data

if __name__ == '__main__':
	__main__()
